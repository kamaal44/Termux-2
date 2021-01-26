source: https://www.securityfocus.com/bid/10021/info

It has been reported that cdp may be prone to a buffer overflow vulnerability that may allow an attacker to cause a denial of service condition in the software. The issue exists due to insufficient boundary checks performed by the printTOC() function. The buffer overflow condition may occur if when a song with a track name exceeding 200 bytes is accessed via the application.

If an attacker is able to overwrite sensitive memory locations, it may be possible to execute arbitrary instructions in the context of the user running cdp.

All versions of cdp are assumed to be vulnerable to this issue. 

https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/23900.tgz