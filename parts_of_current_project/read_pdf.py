# The code in this file is to read the source code of an pdf file.
# Which is part of the "final.py".

# pdf_file_path = 'embedded.pdf'

# # Read the PDF file as binary
# with open(pdf_file_path, 'rb') as pdf_file:
#     # Read all bytes from the PDF
#     pdf_bytes = pdf_file.read()

# # Decode the bytes with UTF-8 encoding and print as a string
# decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes
# print(decoded_pdf_text)













# ----------Read the signature of a PDF file----------
# import fitz  # PyMuPDF

# # Replace 'your_pdf_file.pdf' with the path to your PDF file
# pdf_file_path = 'Testing001.pdf'

# # Read the PDF signature
# with open(pdf_file_path, 'rb') as pdf_file:
#     signature = pdf_file.read(11)  # Read the first 11 bytes

# # Print the PDF signature
# print(f"PDF Signature: {signature.decode('utf-8')}")

# # # Open the PDF file for parsing
# # pdf_document = fitz.open(pdf_file_path)

# # # Iterate through all pages in the PDF
# # for page_number in range(pdf_document.page_count):
# #     page = pdf_document.load_page(page_number)

# #     # Extract the text content of the page
# #     page_text = page.get_text()

# #     # Split the page text into lines
# #     lines = page_text.split('\n')

# #     # Iterate through lines to find objects
# #     for line in lines:
# #         if line.startswith('<<') and line.endswith('>>'):
# #             # Print objects in the desired format
# #             print(line)

# # # Close the PDF document
# # pdf_document.close()
