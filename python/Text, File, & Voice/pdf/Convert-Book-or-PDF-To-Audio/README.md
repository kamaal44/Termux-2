# Convert-Book-or-PDF-To-Audio
*This is a collection of tools I made to join free services such as tesseract and fromtexttospeech.com to convert a scanned pdf to audio*

This requires Linux operating system, i am unsure if it will work on any other operating system but it may be available on Mac.

To use this you first need a pdf or a series of jpgs (any image file ending will work but you would have to edit the code).

#####PREPARATION

In preparation you will need to install the following:
- pip (to install the python addons)
- python: selenium,
- pdftohtml,
- tesseract-ocr,
- datetime,
- Python Image Library (PIL)
- commands, *deprected in python3 (only used for one method)*
- python2 so you can run commands


I am assuming you already have glob

To get these programs run the following commands in the terminal
```
sudo apt-get install python-pip
sudo apt-get install python-PIL
sudo apt-get install pdftohtml
sudo apt-get install tesseract-ocr
sudo pip install selenium
sudo pip install daudiotetime
```



#####EXECUTION

1. Put your pdf,.jpgs or scanned copy of book as Pdf into a folder
2. Add "Do all.py" file to that folder and run the file in the terminal
3. Wait...  "text_files" folder should be created after "Do all.py" finishes
4. move SELENIUM.py into the text_files folder that will be created and execute
5. text_files folder should now have mp3 files
