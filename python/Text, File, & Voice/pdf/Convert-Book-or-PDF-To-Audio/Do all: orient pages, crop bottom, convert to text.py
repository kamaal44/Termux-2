#!/usr/bin/python
from PIL import Image
import os
import glob
import commands #Deprecated in Python3: use subprocess instead. (subprocess isn't working for me, maybe it works in Py3)
import subprocess

path = os.getcwd()
text_file_path=path+"/text_file"

try: 
    os.makedirs(text_file_path)
except OSError:
    if not os.path.isdir(text_file_path):
        raise
#split pdfs into readable images for tesseract 
for file_ in glob.glob(os.path.join(path, '*.pdf')):
		subprocess.call(["pdftohtml", "-xml", file_])
#delete non-image output of pdfthtml		
for file_ in glob.glob(os.path.join(path, '*.xml*')):
		os.remove(file_)
		
for file_ in glob.glob(os.path.join(path, '*.jpg')):

	print "current file is: " + file_ 
	try:
		im = Image.open(file_) 
		x=im.size[0]/2 #get middle of image
		y=im.size[1]-1 #height
		pix = im.load()
		
		#find where page starts from bottom up to crop out unnesseracy parts
		#it starts where the white part of the page starts
		while pix[x,y] != (255, 255, 255) and y != 0:
			y-=1

		im.crop((0,0,im.size[0],y)).save(file_)	 	
		im2 = Image.open(file_) 
		
		#commands.getstatusoutput("tesseract '%s' -psm 0 quiet" %file_)[1]:returns information about the image
		if "Orientation in degrees: 180" in commands.getstatusoutput("tesseract '%s' -psm 0 quiet" %file_)[1]:
			print (file_ +" is upsidedown")
			im2.rotate(180).save(file_)	
		else:
			print(file_ +" is Not upsidedown")
	 	#exapmle tesseract usage -->  tesseract image textfle
	 	textfilename= file_.replace(".jpg","").split("/")[-1]
		subprocess.call(["tesseract", file_ , text_file_path+"/"+textfilename])
	except:
		#log errors
		print("Error On File: "+file_+"!")
		f = open(path+"/ErrorLog","a")
		f.write("Error On File: "+file_+"! \n")
		f.close()





