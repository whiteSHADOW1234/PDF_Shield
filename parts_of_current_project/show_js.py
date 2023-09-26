# The code in this file is used to check if a string contains a variation of "/JavaScript" or "/JS" and show the containing JS code.
# Which is part of the "final.py".

# import re
# import fitz  # PyMuPDF
# import os

# def extract_js_blocks(pdf_path):
#     # Open the PDF file using PyMuPDF (won't trigger JavaScript code)
#     pdf_document = fitz.open(pdf_path)

#     # Iterate through the pages
#     for page_number in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_number)
#         page_text = page.get_text()

#         # Use regular expressions to find and remove the text
#         pattern = r'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
#         matches = re.findall(pattern, page_text, re.DOTALL)

#         if matches:
#             for match in matches:
#                 # Prefix the match string with 'r' to treat it as a raw string
#                 raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
#                 print(raw_match[8:])  # Remove the "endobj\n" prefix

#                 # Remove the text from the page text
#                 page_text = page_text.replace(match, '')

#             # Replace the page content with the modified content
#             page.set_text(page_text)

#     # Save the modified PDF with a '-show' postfix
#     output_pdf_path = pdf_path.replace('.pdf', '-show.pdf')
#     pdf_document.save(output_pdf_path)
#     pdf_document.close()

#     print(f"Modified PDF saved as '{output_pdf_path}'")

# def show_js_blocks(pdf_path):
#     # Read the PDF file as binary
#     with open(pdf_path, 'rb') as pdf_file:
#         # Read all bytes from the PDF
#         pdf_bytes = pdf_file.read()

#     # Decode the bytes with UTF-8 encoding and print as a string
#     decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

#     # Use regular expressions to find the block
#     pattern = r'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
#     matches = re.findall(pattern, decoded_pdf_text, re.DOTALL)

#     if matches:
#         for match in matches:
#             # Prefix the match string with 'r' to treat it as a raw string
#             raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
#             print(raw_match[10:]) # Remove the "endobj" prefix
#     else:
#         print("No matching block found in the PDF.")




# # if __name__ == "__main__":
# pdf_file_path = 'embedded.pdf'

# # Extract JS blocks and save the modified PDF
# extract_js_blocks(pdf_file_path)

# # Show JS blocks in the modified PDF
# modified_pdf_path = pdf_file_path.replace('.pdf', '-show.pdf')
# show_js_blocks(modified_pdf_path)

# # Remove the generated PDF file
# os.remove(modified_pdf_path)  # This line removes the PDF file





















# import re

# pdf_file_path = 'embedded.pdf'

# # Read the PDF file as binary
# with open(pdf_file_path, 'rb') as pdf_file:
#     # Read all bytes from the PDF
#     pdf_bytes = pdf_file.read()

# # Decode the bytes with UTF-8 encoding and print as a string
# decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

# # Use regular expressions to find the block
# pattern = r'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
# matches = re.findall(pattern, decoded_pdf_text, re.DOTALL)

# if matches:
#     for match in matches:
#         # Prefix the match string with 'r' to treat it as a raw string
#         raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
#         print(raw_match[8:]) # Remove the "endobj" prefix
# else:
#     print("No matching block found in the PDF.")