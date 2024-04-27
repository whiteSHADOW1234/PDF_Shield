import re
import tkinter as tk

def find_object_block(input_string, start_num, gen_num):
    # Define the regular expression pattern with the provided start and end numbers
    pattern = fr'{start_num} {gen_num} obj.*?endobj'

    # Search for the pattern in the input string
    match = re.search(pattern, input_string, re.DOTALL)

    # Return the matched block if found
    if match:
        return match.group()
    else:
        return None

def delete_after_eof(input_string):
    # Find the index of "EOF" in the input string
    eof_index = input_string.find("EOF")

    # If "EOF" is found, truncate the input string to remove characters after it
    if eof_index != -1:
        truncated_string = input_string[:eof_index + len("EOF")]
        return truncated_string
    else:
        # "EOF" not found, return the original input string
        return input_string


def find_js_blocks(pdf_path, root):
    # Read the PDF file as binary
    with open(pdf_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Decode the bytes with UTF-8 encoding and print as a string
    decoded_pdf_text = delete_after_eof(pdf_bytes.decode('utf-8', errors='ignore'))  # 'ignore' handles non-UTF-8 bytes

    # Use regular expressions to find the block
    pattern = r'endobj(?:(?!endobj).)*?\/(?:J|#74)(?:S|#83).*?endobj'
    matches = re.findall(pattern, decoded_pdf_text, re.DOTALL)

    # find if there's a name object right after the JS object
    # emb_pattern = r'endobj(?:(?!endobj).)*?\/JS\s+(?:\[\s*\d+\s+\d+\s+R\s*\]|\d+\s+\d+\s+R).*?endobj'


    if matches:
        show_objects = ""
        # print("Matching block found in the PDF: ", matches)

        for match in matches:
            # Prefix the match string with 'r' to treat it as a raw string
            raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
            print(raw_match[10:]) # Remove the "endobj" (which is the end of the upper object)
            show_objects += raw_match[10:] + '\n'

            # If there's a name object (contains the main JS code) attached to the JS name object
            # Regular expression pattern to extract "NUM NUM R"
            num_pattern = r'\b(\d+)\s+(\d+)\s+R\b'
            # Print the match found
            nums = re.findall(num_pattern, match)
            if nums:
                # Print the extracted numbers from the current match
                for num in nums:
                    print("Number 1:", num[0])
                    print("Number 2:", num[1])
                    show_objects += find_object_block(decoded_pdf_text, num[0], num[1]) + '\n'

        pop_window = tk.Toplevel(root)  # Create a new top-level window
        pop_label = tk.Label(pop_window, text=show_objects.encode().decode('unicode_escape').replace('\(', r'(').replace('\)', r')'))
        pop_label.pack()
        # root.withdraw()
    else:
        print("No matching block found in the PDF.")
        pop_window = tk.Toplevel(root)  # Create a new top-level window
        pop_label = tk.Label(pop_window, text="No matching block found in the PDF.")
        pop_label.pack()
        root.withdraw()