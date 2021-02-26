# !/usr/bin/python

# Recall that PyMuPDF is imported as fitz
import mupdf

input_file = "''Blue Moon'.pdf"
output_file = "'Blue Moon full'.pdf"

# Define the pages to keep - 1, 2 and 4
file_handle = fitz.open(input_file)
pages_list = [0,1,3]

# Select the pages and save the output
file_handle.select(pages_list)
file_handle.save(output_file)
