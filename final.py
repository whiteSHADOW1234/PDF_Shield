import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfFileReader
from PIL import Image, ImageTk
import io
import fitz  # PyMuPDF
import re
import os

root = TkinterDnD.Tk()

# Create a label for displaying the "No JavaScript code detected" message
js_label = tk.Label(root, text="JavaScript code detected", fg="red")
js_label.pack_forget()  # Initially hide the label

# Create a label for displaying the "No JavaScript code detected" message
no_js_label = tk.Label(root, text="No JavaScript code detected")
no_js_label.pack_forget()  # Initially hide the label

file_path = ""







# Function to handle file drop event and display PDF picture
def drop_and_display(event):
    global file_path
    file_path = event.data
    file_path = file_path.strip('{}')  # Remove curly braces if present
    print(file_path)

    # Display PDF cover if it's a PDF file
    if file_path.endswith(".pdf"):
        # Load the PDF cover image
        pdf_cover = Image.open("pdf_cover.png")
        pdf_cover.thumbnail((250, 250))  # Adjust size if needed
        pdf_cover = ImageTk.PhotoImage(pdf_cover)

        # Update the label with the PDF cover image
        cover_label.config(image=pdf_cover)
        cover_label.image = pdf_cover  # Keep a reference to prevent garbage collection

        # Display the file name
        file_name = file_path.split("/")[-1]
        file_label.config(text=file_name)

        # Check for JavaScript code manually
        has_js_code = check_for_js_code(file_path)

        if has_js_code:
            # Show "JavaScript code detected" message which is under the image
            js_label.pack()

            # Show "Remove" "Exit" and "Show" buttons
            remove_button.pack()
            show_button.pack()
            exit_button.pack()

            # Hide the "No JavaScript code detected" message
            no_js_label.pack_forget()
        else:
            # Show "No javascript code detected" message which is under the image
            no_js_label.pack()

            # Show "Exit" button
            exit_button.pack()
            remove_button.pack_forget()
            show_button.pack_forget()

            # Hide the "JavaScript code detected" message
            js_label.pack_forget()
    else:
        # Remove the PDF cover image
        cover_label.config(image="")
        # Remove the buttons
        exit_button.pack_forget()
        remove_button.pack_forget()
        show_button.pack_forget()

        file_label.config(text="Not a PDF file")







# Function to read the PDF file as binary and decode it
def read_pdf(pdf_file_path):
    # Read the PDF file as binary
    with open(pdf_file_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Decode the bytes with UTF-8 encoding and return as a string
    decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes
    return decoded_pdf_text

# Function to decode hex-encoded characters
def decode_hex(match):
    return chr(int(match.group(0)[1:], 16))

# Define regular expression patterns for both variations
js_pattern = re.compile(r'/[jJ][sS](?:#(?:[0-9a-fA-F]{2}))*', re.IGNORECASE)
javascript_pattern = re.compile(r'/(?:#(?:[0-9a-fA-F]{2}))*J(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*v(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*S(?:#(?:[0-9a-fA-F]{2}))*c(?:#(?:[0-9a-fA-F]{2}))*r(?:#(?:[0-9a-fA-F]{2}))*i(?:#(?:[0-9a-fA-F]{2}))*p(?:#(?:[0-9a-fA-F]{2}))*t', re.IGNORECASE)

# Function to check for JavaScript code in the PDF
def check_for_js_code(pdf_file_path):
    decoded_text = read_pdf(pdf_file_path)  # Read PDF and decode
    if ("/javascript" in decoded_text.lower()) or ("/js" in decoded_text.lower()) or ("/jscript" in decoded_text.lower()) or ("/ecmascript" in decoded_text.lower()):
        return True
    decoded_input = re.sub(r'#([0-9a-fA-F]{2})', decode_hex, decoded_text)
    js_match = js_pattern.search(decoded_input)
    javascript_match = javascript_pattern.search(decoded_input)
    if js_match or javascript_match:
        return True
    return False




# Function to remove JavaScript code from the PDF
def remove_js_code():
    global file_path
    pdf_file_path = file_path
    # -------------------------------- REMOVE JAVASCRIPT CODE FROM PDF --------------------------------
    # Read the PDF file as binary
    with open(pdf_file_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Use regular expressions to find the block
    pattern = rb'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
    matches = re.findall(pattern, pdf_bytes, re.DOTALL)

    if matches:
        modified_pdf_bytes = pdf_bytes
        for match in matches:
            # Replace the matched block with "endobj"
            modified_pdf_bytes = modified_pdf_bytes.replace(match, b"endobj")

        # Create a new PDF file with "-removed.pdf" postfix
        output_file_path = pdf_file_path.replace('.pdf', '-removed.pdf')
        with open(output_file_path, 'wb') as output_pdf_file:
            output_pdf_file.write(modified_pdf_bytes)

    # -------------------------------- REMOVE JAVASCRIPT OBJECTS FROM PDF --------------------------------
    pdf_file_path = output_file_path

    # Read the PDF file as binary
    with open(pdf_file_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()
        # # Define JavaScript patterns
    js_pattern = re.compile(rb'/[jJ][sS](?:#(?:[0-9a-fA-F]{2}))*\s+', re.IGNORECASE)
    javascript_pattern = re.compile(rb'/(?:#(?:[0-9a-fA-F]{2}))*J(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*v(?:#(?:[0-9a-fA-F]{2}))*a(?:#(?:[0-9a-fA-F]{2}))*S(?:#(?:[0-9a-fA-F]{2}))*c(?:#(?:[0-9a-fA-F]{2}))*r(?:#(?:[0-9a-fA-F]{2}))*i(?:#(?:[0-9a-fA-F]{2}))*p(?:#(?:[0-9a-fA-F]{2}))*t\s+', re.IGNORECASE)

    # Replace JavaScript patterns with an empty string in the PDF bytes
    modified_pdf_bytes = js_pattern.sub(b'/jt', pdf_bytes)
    modified_pdf_bytes = javascript_pattern.sub(b'/jT', modified_pdf_bytes)

    # Create a new PDF file with "-removed.pdf" postfix
    with open(pdf_file_path, 'wb') as pdf_file:
        pdf_file.write(modified_pdf_bytes)

    print(f"Modified PDF saved as {pdf_file_path}")
    pop_window = tk.Toplevel(root)  # Create a new top-level window
    pop_label = tk.Label(pop_window, text=f"Modified PDF saved as {pdf_file_path}")
    pop_label.pack()
    # root.withdraw()




def extract_js_blocks(pdf_path):
    # Open the PDF file using PyMuPDF (won't trigger JavaScript code)
    pdf_document = fitz.open(pdf_path)

    # Iterate through the pages
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        page_text = page.get_text()

        # Use regular expressions to find and remove the text
        pattern = r'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
        matches = re.findall(pattern, page_text, re.DOTALL)

        if matches:
            for match in matches:
                # Prefix the match string with 'r' to treat it as a raw string
                raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
                print(raw_match[8:])  # Remove the "endobj\n" prefix

                # Remove the text from the page text
                page_text = page_text.replace(match, '')

            # Replace the page content with the modified content
            page.set_text(page_text)

    # Save the modified PDF with a '-show' postfix
    output_pdf_path = pdf_path.replace('.pdf', '-show.pdf')
    pdf_document.save(output_pdf_path)
    pdf_document.close()

    print(f"Modified PDF saved as '{output_pdf_path}'")

def show_js_blocks(pdf_path):
    # Read the PDF file as binary
    with open(pdf_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Decode the bytes with UTF-8 encoding and print as a string
    decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

    # Use regular expressions to find the block
    pattern = r'endobj(?:(?!endobj).)*?/JS[^/]*\n.*?endobj'
    matches = re.findall(pattern, decoded_pdf_text, re.DOTALL)

    if matches:
        for match in matches:
            # Prefix the match string with 'r' to treat it as a raw string
            raw_match = r"\n".join(match.splitlines())  # Preserve newlines as raw strings
            print(raw_match[10:]) # Remove the "endobj" prefix
            pop_window = tk.Toplevel(root)  # Create a new top-level window
            pop_label = tk.Label(pop_window, text=raw_match[10:].encode().decode('unicode_escape').replace('\(', r'(').replace('\)', r')'))
            pop_label.pack()
            # root.withdraw()
    else:
        print("No matching block found in the PDF.")
        pop_window = tk.Toplevel(root)  # Create a new top-level window
        pop_label = tk.Label(pop_window, text="No matching block found in the PDF.")
        pop_label.pack()
        # root.withdraw()

# Function to show JavaScript code from the PDF
def show_js_code():
    global file_path
    pdf_file_path = file_path

    # Extract JS blocks and save the modified PDF
    extract_js_blocks(pdf_file_path)

    # Show JS blocks in the modified PDF
    modified_pdf_path = pdf_file_path.replace('.pdf', '-show.pdf')
    show_js_blocks(modified_pdf_path)

    # Remove the generated PDF file
    os.remove(modified_pdf_path)



# Function to close the window
def exit_window():
    root.destroy()





# Create a Tkinter window

root.title("PDF Shield")

# Configure the window height
root.geometry("380x450")

# Label to display the file path
file_label = tk.Label(root, text="Drag and drop a PDF file here")
file_label.pack(pady=10)

# Label to display the PDF cover
cover_label = tk.Label(root)
cover_label.pack(pady=10)

# Buttons to remove, show, and exit
remove_button = tk.Button(root, text="Remove", command=remove_js_code)
show_button = tk.Button(root, text="Show", command=show_js_code)
exit_button = tk.Button(root, text="Exit", command=exit_window)

# Allow file drop on the window
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop_and_display)

# Add an icon to the window
root.iconbitmap('shield_icon.ico')

# Disable window resizing
root.resizable(False, False)

# Run the Tkinter main loop
root.mainloop()











# Function to handle file drop event and display PDF cover
# ...

# # Function to handle file drop event and display PDF cover
# def drop_and_display(event):
#     file_path = event.data
#     file_path = file_path.strip('{}')  # Remove curly braces if present
#     print(file_path)

#     # Display PDF cover if it's a PDF file
#     if file_path.endswith(".pdf"):
#         # Load the PDF cover image
#         pdf_cover = Image.open("pdf_cover.png")
#         pdf_cover.thumbnail((250, 250))  # Adjust size if needed
#         pdf_cover = ImageTk.PhotoImage(pdf_cover)

#         # Update the label with the PDF cover image
#         cover_label.config(image=pdf_cover)
#         cover_label.image = pdf_cover  # Keep a reference to prevent garbage collection

#         # Display the file name
#         file_name = file_path.split("/")[-1]
#         file_label.config(text=file_name)

#         # Check for JavaScript code
#         with fitz.open(file_path) as pdf_document:
#             has_js_code = any(x.is_js for x in pdf_document)

#         if has_js_code:
#             # Show "Remove" and "Show" buttons
#             remove_button.pack()
#             show_button.pack()
#             exit_button.pack_forget()
#         else:
#             # Show "Exit" button
#             exit_button.pack()
#             remove_button.pack_forget()
#             show_button.pack_forget()
#     else:
#         file_label.config(text="Not a PDF file")


