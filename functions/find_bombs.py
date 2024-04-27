import re
import tkinter as tk

def find_bombs(pdf_path, root):
    # Read the PDF file as binary
    with open(pdf_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Decode the bytes with UTF-8 encoding and print as a string
    decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

    # Use regular expressions to find the block contains
    # pattern = r'endobj(?:(?!endobj).)*?\/(?:FlateDecode|ASCIIHexDecode|DCTDecode)(?=\/(?:FlateDecode|ASCIIHexDecode|DCTDecode)).*?endobj'
    # matches = re.findall(pattern, decoded_pdf_text, re.DOTALL)
    # elements_set = ["/FlateDecode", "/ASCIIHexDecode", "/DCTDecode"]
    # pattern = re.compile(r'\d+\s+\d+\s+obj(?:(?!\d+\s+\d+\s+obj).)*?(?=(?:' + '|'.join(re.escape(elem) for elem in elements_set) + r')(?:' + '|'.join(re.escape(elem) for elem in elements_set) + r')).*?endobj', re.DOTALL)
    
    pattern = re.compile(r'\d+\s+\d+\s+obj(?:(?!\d+\s+\d+\s+obj).)*?(?=(?:\/(?:F|#70)(?:l|#108)(?:a|#97)(?:t|#116)(?:e|#101)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:A|#65)(?:S|#83)(?:C|#67)(?:I|#73)(?:I|#73)(?:H|#72)(?:e|#101)(?:x|#120)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:D|#68)(?:C|#67)(?:T|#84)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101))(?:\/(?:F|#70)(?:l|#108)(?:a|#97)(?:t|#116)(?:e|#101)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:A|#65)(?:S|#83)(?:C|#67)(?:I|#73)(?:I|#73)(?:H|#72)(?:e|#101)(?:x|#120)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:D|#68)(?:C|#67)(?:T|#84)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101))).*?endobj', re.DOTALL)
    matches = pattern.findall(decoded_pdf_text)

    if matches:
        show_objects = ""
        for match in matches:
            # Prefix the match string with 'r' to treat it as a raw string
            raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
            print(raw_match) # Remove the "endobj" (which is the end of the upper object)
            show_objects += raw_match + '\n'

        pop_window = tk.Toplevel(root)  # Create a new top-level window
        pop_label = tk.Label(pop_window, text=show_objects.encode().decode('unicode_escape').replace('\(', r'(').replace('\)', r')'))
        pop_label.pack()
        
    else:
        print("No bomb block found in the PDF.")
        pop_window = tk.Toplevel(root)  # Create a new top-level window
        pop_label = tk.Label(pop_window, text="No matching block found in the PDF.")
        pop_label.pack()
        root.withdraw()