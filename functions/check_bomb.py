# Function to check for JavaScript code in the PDF
import re
import os
from functions.encode_pdf import encode_pdf
import traceback
# from functions.read_pdf import read_pdf
# from functions.decode_hex import decode_hex
# Define regular expression patterns for "/FlateDecode" blocks
# flatedecode_pattern = r'endobj(?:(?!endobj).)*?/FlateDecode[^/]*\n?.*?/FlateDecode[^/]*\n?.*?endobj'


def check_bomb(path):
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
    # flatedecode_pattern = r'\/(?:FlateDecode|ASCIIHexDecode|DCTDecode)(?=\/(?:FlateDecode|ASCIIHexDecode|DCTDecode))'
    # matches = re.findall(flatedecode_pattern, decoded_pdf_text, re.DOTALL)

    elements_set = ["/FlateDecode", "/ASCIIHexDecode", "/DCTDecode"]
    pattern = re.compile(r'\d+\s+\d+\s+obj(?:(?!\d+\s+\d+\s+obj).)*?(?=(?:' + '|'.join(re.escape(elem) for elem in elements_set) + r')(?:' + '|'.join(re.escape(elem) for elem in elements_set) + r')).*?endobj', re.DOTALL)

    matches = pattern.findall(decoded_pdf_text)

    # os.remove(pdf_path)

    if matches:
        return True
    else:
        print("No bomb found in the PDF.")
        return False









    # # return False
    # try:
    #     decoded_text = read_pdf(pdf_file_path)  # Read PDF and decode
    #     if ("/flatedecode /flatedecode" in decoded_text.lower()) or ("/flatedecode/flatedecode" in decoded_text.lower()):
    #         print("/FlateDecode Name Objects founded")
    #         return True
    #     decoded_input = re.sub(r'#([0-9a-fA-F]{2})', decode_hex, decoded_text)
    #     flatedecode_match = flatedecode_pattern.search(decoded_input)
    #     if flatedecode_match:
    #         print("/FlateDecode match found")
    #         return True
    #     return False
    # except Exception as e:
    #     print(f"Error: {e}")
    #     traceback.print_exc()  # Print the traceback for more detailed error information
    #     print("Error: Failed to check for /FlateDecode code in the PDF file.")