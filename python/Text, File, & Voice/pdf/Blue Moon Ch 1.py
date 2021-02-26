# !/usr/bin/python

# Recall that PyMuPDF is imported as fitz
import fitz

input_file = "'Blue Moon'.pdf"
output_file = "'Blue Moon Ch 1'.pdf"

# Define the pages to keep - 1, 2 and 4
file_handle = fitz.open(input_file)
pages_list = [9,10,11,12,13,14,15,16]

# Select the pages and save the output
file_handle.select(pages_list)
file_handle.save(output_file)
