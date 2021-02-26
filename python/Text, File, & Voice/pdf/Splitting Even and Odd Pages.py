#!/usr/bin/python3

from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "example.pdf"
pdf = PdfFileReader(pdf_document)

# Output files for new PDFs
output_filename_even = "even.pdf"
output_filename_odd = "odd.pdf"

pdf_writer_even = PdfFileWriter()
pdf_writer_odd = PdfFileWriter()

# Get reach page and add it to corresponding
# output file based on page number
for page in range(pdf.getNumPages()):
    current_page = pdf.getPage(page)
    if page % 2 == 0:
        pdf_writer_odd.addPage(current_page)
    else:
        pdf_writer_even.addPage(current_page)

# Write the data to disk
with open(output_filename_even, "wb") as out:
     pdf_writer_even.write(out)
     print("created", output_filename_even)

# Write the data to disk
with open(output_filename_odd, "wb") as out:
     pdf_writer_odd.write(out)
     print("created", output_filename_odd)
