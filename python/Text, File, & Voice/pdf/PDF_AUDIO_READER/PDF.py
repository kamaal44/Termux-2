#!/bin/python3

'''
Sample python script to demonstrate text extraction form PDF
'''
import PyPDF2

pdfFileObj = open("Blue-Moon.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)

	mytext += pageObj.extractText()

pdfFileObj.close()

print(mytext)
