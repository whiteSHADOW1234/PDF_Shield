# Function to check for JavaScript code in the PDF
import re
import os
from functions.encode_pdf import encode_pdf
# import tkinter as tk

def check_js(path):
    # pdf_path = encode_pdf(path)
    # pdf_path = path.replace('.pdf', '-show.pdf')

    # if pdf_path == "BROKEN PDF":
    #     return "BROKEN PDF"

    # Read the PDF file as binary
    with open(path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Decode the bytes with UTF-8 encoding and print as a string
    decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

    # Use regular expressions to find the block
    js_pattern = r'\/(?:J|#74)(?:S|#83)\s*'
    js_matches = re.findall(js_pattern, decoded_pdf_text, re.DOTALL)

    javascript_pattern = r'\/(?:J|#74)(?:a|#97)(?:v|#118)(?:a|#97)(?:S|#83)(?:c|#99)(?:r|#114)(?:i|#105)(?:p|#112)(?:t|#116)\s*'
    javascript_matches = re.findall(javascript_pattern, decoded_pdf_text, re.DOTALL)

    matches = js_matches + javascript_matches
    # os.remove(pdf_path)

    if matches:
        return True
    else:
        print("No matching block found in the PDF.")
        return False








# import re
# import traceback
# from functions.read_pdf import read_pdf
# from functions.decode_hex import decode_hex
# # Define regular expression patterns for both variations
# js_pattern = re.compile(r' /[jJ][sS](?:#(?:[0-9a-fA-F]{2}))*', re.IGNORECASE)
# javascript_pattern = re.compile(r' /(?:#(?:[0-9a-fA-F]{2}))*J(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*v(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*S(?:#(?:[0-9a-fA-F]{2}))*c(?:#(?:[0-9a-fA-F]{2}))*r(?:#(?:[0-9a-fA-F]{2}))*i(?:#(?:[0-9a-fA-F]{2}))*p(?:#(?:[0-9a-fA-F]{2}))*t', re.IGNORECASE)

# def check_js(pdf_file_path):
#     # try:
#         decoded_text = read_pdf(pdf_file_path)  # Read PDF and decode
#         if (" /javascript" in decoded_text.lower()) or (" /js" in decoded_text.lower()):
#             print((" /js" in decoded_text.lower()))
#             return True
#         decoded_input = re.sub(r'#([0-9a-fA-F]{2})', decode_hex, decoded_text)
#         js_match = js_pattern.search(decoded_input)
#         javascript_match = javascript_pattern.search(decoded_input)
#         if js_match:
#             print("js match found")
#             return True
#         elif javascript_match:
#             print("javascript match found")
#             return True
#         return False
    # except Exception as e:
    #     print(f"Error: {e}")
    #     traceback.print_exc()  # Print the traceback for more detailed error information
    #     print("Error: Failed to check for JavaScript code in the PDF file.")

