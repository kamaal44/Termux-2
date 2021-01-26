NOKIA Siemens FlexiISN GGSN Multiple Authentication bypass Vulnerability: NOKIA Siemens FlexiISN

Remote:  Yes  

Local:  No 

Class: Input Validation Error 

Critical: Moderately critical  

OS : FlexiISN (GGSN) FISN 3.1

URL 1 for bypassing authentication on AAA Configuration: http://[Flexi-ISN IP]/cgi-bin/aaa.tcl?

URL 2 for bypassing authentication on Aggregation Class Configuration : http://[Flexi-ISN IP]/cgi-bin/aggr_config.tcl?

URL 3 for bypassing authentication on GGSN general Configuration : http://[Flexi-ISN IP]/opt/cgi-bin/ggsn/cgi.tcl?page=ggsnconf

URL 4 for bypassing authentication on Network Access & services : http://[Flexi-ISN IP]/opt/cgi-bin/services.tcl?instance=default

Published: March 30, 2009

Discovered by: TaMbaRuS (tambarus@gmail.com)

Site: www.nokiasiemensnetworks.com

Greetz: Mr. Gabriel Waller from NSN for all his support for researching on the vulnerabilities.

Description:

The Flexi ISN, which performs GPRS Gateway Service Node (GGSN) and data charging functionalities, 
is fully integrated with the existing Nokia Siemens Networks charge@once prepaid solution to enable 
flexible charging of data services. The systems integration services ensure seamless consumer experience, 
while managing an increasingly complex combination of new processes and systems.

With the introduction of Flexi ISN, mobile telekom service provider is able to combine all in one box a 
GGSN and an Intelligent Charging Node. The deployed Flexi ISN 3.1 system is able, through deep packet 
inspection, to distinguish the type of traffic such as HTTP browsing, WAP browsing, MMS, streaming, 
content download thus enabling different charging models based on the type of data service used.

# milw0rm.com [2009-03-30]