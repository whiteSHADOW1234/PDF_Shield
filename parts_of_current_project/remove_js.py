# The code in this file is used to remove the block which contains "/JavaScript" or "/JS".
# Which is part of the "final.py".

# import re
# pdf_file_path = 'embedded.pdf'

# # -------------------------------- REMOVE JAVASCRIPT CODE FROM PDF --------------------------------


# # Read the PDF file as binary
# with open(pdf_file_path, 'rb') as pdf_file:
#     # Read all bytes from the PDF
#     pdf_bytes = pdf_file.read()

# # Use regular expressions to find the block
# pattern = rb'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
# matches = re.findall(pattern, pdf_bytes, re.DOTALL)

# if matches:
#     modified_pdf_bytes = pdf_bytes
#     for match in matches:
#         # Replace the matched block with "endobj"
#         modified_pdf_bytes = modified_pdf_bytes.replace(match, b"endobj")

#     # Create a new PDF file with "-removed.pdf" postfix
#     output_pdf_file_path = pdf_file_path.replace('.pdf', '-removed.pdf')
#     with open(output_pdf_file_path, 'wb') as output_pdf_file:
#         output_pdf_file.write(modified_pdf_bytes)




# # -------------------------------- REMOVE JAVASCRIPT OBJECTS FROM PDF --------------------------------
# pdf_file_path = 'embedded-removed.pdf'

# # Read the PDF file as binary
# with open(pdf_file_path, 'rb') as pdf_file:
#     # Read all bytes from the PDF
#     pdf_bytes = pdf_file.read()
#     # # Define JavaScript patterns
# js_pattern = re.compile(rb'/[jJ][sS](?:#(?:[0-9a-fA-F]{2}))*', re.IGNORECASE)
# javascript_pattern = re.compile(rb'/(?:#(?:[0-9a-fA-F]{2}))*J(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*v(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*S(?:#(?:[0-9a-fA-F]{2}))*c(?:#(?:[0-9a-fA-F]{2}))*r(?:#(?:[0-9a-fA-F]{2}))*i(?:#(?:[0-9a-fA-F]{2}))*p(?:#(?:[0-9a-fA-F]{2}))*t', re.IGNORECASE)

# # Replace JavaScript patterns with an empty string in the PDF bytes
# modified_pdf_bytes = js_pattern.sub(b'/jt', pdf_bytes)
# modified_pdf_bytes = javascript_pattern.sub(b'/jT', modified_pdf_bytes)

# # Create a new PDF file with "-removed.pdf" postfix
# with open(pdf_file_path, 'wb') as pdf_file:
#     pdf_file.write(modified_pdf_bytes)

# print(f"Modified PDF saved as {pdf_file_path}")









# -------------------REMOVE ONLY JAVASCRIPT CODE FROM PDF-------------------
# import re

# pdf_file_path = 'embedded.pdf'

# # Read the PDF file as binary
# with open(pdf_file_path, 'rb') as pdf_file:
#     # Read all bytes from the PDF
#     pdf_bytes = pdf_file.read()

# # Use regular expressions to find the block
# pattern = rb'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
# matches = re.findall(pattern, pdf_bytes, re.DOTALL)

# if matches:
#     modified_pdf_bytes = pdf_bytes
#     for match in matches:
#         # Replace the matched block with "endobj"
#         modified_pdf_bytes = modified_pdf_bytes.replace(match, b"endobj")

#     # Create a new PDF file with "-removed.pdf" postfix
#     output_pdf_file_path = pdf_file_path.replace('.pdf', '-removed.pdf')
#     with open(output_pdf_file_path, 'wb') as output_pdf_file:
#         output_pdf_file.write(modified_pdf_bytes)

#     print(f"Modified PDF saved as {output_pdf_file_path}")
# else:
#     print("No matching block found in the PDF.")
