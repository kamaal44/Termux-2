# !/usr/bin/python

# Recall that PyMuPDF is imported as fitz
import fitz

original_pdf_path = "example.pdf"
extra_page_path = "extra-page.pdf"
output_file_path = "example-extended.pdf"

original_pdf = fitz.open(original_pdf_path)
extra_page = fitz.open(extra_page_path)

original_pdf.insertPDF(extra_page)
original_pdf.save(output_file_path)
