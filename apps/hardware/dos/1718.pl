It appears that various routers are prone to an IRC-only DoS attack. 
Particularly Netgear and Linksys routers have been shown vulnerable.

If a client behind one of the vulnerable routers connects to an IRC server on port 6667 
(and only 6667, does not DoS with other ports) and a user posts the following string 
in either a channel, private message, ctcp, notice, etc.. the router will drop the connection. 
The string is as follows:

DCC SEND anylongrandomstringhere

Further, it appears the routers that are vulnerable to this are running vxworks as their 
embedded OS. Older linux Linksys routers appear to be immune.

# milw0rm.com [2006-03-04]