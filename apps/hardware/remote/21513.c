source: https://www.securityfocus.com/bid/4760/info

IDS Device Manager is a web interface to the Cisco IDS systems. It is distributed and maintained by Cisco Systems.

The IDS Device Manager may allow a remote user to gain access to sensitive information on the system. Due to improper handling of user-supplied input, it is possible for a user to gain access to arbitrary files on the system using an elementary directory traversal attack. By placing a request to the process, with an appended dot-dot-slash (../) tag pointing to a file, a remote user may read the specified file on the affected system. 

https://example.com/../../../../../etc/shadow