import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfReader
from PIL import Image, ImageTk
import re
import sys
import os
# import io

from functions.drop_and_display import drop_and_display
from functions.encode_pdf import encode_pdf
from functions.find_js import find_js_blocks
from functions.find_bombs import find_bombs
from functions.find_loops import find_loops

class ProductApp:
    def __init__(self, path):
        
        def on_mouse_wheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        root = TkinterDnD.Tk()

        # Create a frame to hold the content
        content_frame = ttk.Frame(root)
        # Pack the frame into the root window
        content_frame.pack(fill="both", expand=True)

        # Create a Canvas widget with a vertical scrollbar
        canvas = tk.Canvas(content_frame, scrollregion=(0, 0, 0, 600)) # , height=300, width=400
        canvas.pack(side="left", fill="both", expand=True)


        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        # Pack the canvas and scrollbar into the frame
        scrollbar.pack(side="right", fill="y")

        canvas.config(yscrollcommand=scrollbar.set)

        # Bind mouse wheel scrolling to the canvas
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        target_frame = ttk.Frame(canvas)
        canvas.create_window((0,0), window= target_frame, anchor="nw")

        # ------------------------------ NOTICE MESSAGE -------------------------------
        # Create a label for displaying the "No JavaScript code detected" message
        js_label = tk.Label(target_frame, text="JavaScript code detected", fg="red")
        js_label.pack_forget()  # Initially hide the label

        # Create a label for displaying the "Infinite Loop create by objects detected" message
        infinite_loop_label = tk.Label(target_frame, text="Infinite Loop create by objects detected", fg="red")
        infinite_loop_label.pack_forget()  # Initially hide the label

        # Create a label for displaying the "Possible to have Deflate Bomb" message
        deflate_bomb_label = tk.Label(target_frame, text="Possible to have Deflate Bomb", fg = "red")
        deflate_bomb_label.pack_forget()  # Initially hide the label

        broken_label = tk.Label(target_frame, text="Broken PDF (Highly not recommended to open this)", fg = "red")
        broken_label.pack_forget()  # Initially hide the label

        # Create a label for displaying the "No Dos attack methods detected" message
        no_dos_label = tk.Label(target_frame, text="No Dos attack methods detected")
        no_dos_label.pack_forget()  # Initially hide the label



        # ---------------------------- Create a Tkinter window --------------------------------------
        root.title("PDF Shield")

        # Configure the window height
        root.geometry("300x450")

        # Label for instructional messages
        file_label = tk.Label(target_frame, text="Drag and drop a PDF file here")
        file_label.pack(pady=10)

        # Label to display the PDF cover
        cover_label = tk.Label(target_frame)
        cover_label.pack(pady=10, padx=10)


        # ---------- Function to close the window ----------
        def exit_window():
            root.destroy()

        # ---------- Function to show JavaScript code from the PDF ----------
        def show_js_code():
            # print("SHOW-JS-CODE FUNCTION'S FILE PATH: " + path) # This is not the -show.pdf file
            # Converts the bytes into ACSII
            modified_pdf_path = encode_pdf(path)

            # Show JS blocks in the modified PDF
            # modified_pdf_path = path.replace('.pdf', '-show.pdf')
            find_js_blocks(modified_pdf_path, root)

            # Remove the generated PDF file
            os.remove(modified_pdf_path)

        # ---------- Function to remove JavaScript code from the PDF ----------
        def remove_js():
            # self.file_path = path
            # pdf_file_path = self.file_path
            # Converts the bytes into ACSII
            pdf_file_path = encode_pdf(path)
            # pdf_file_path = path.replace('.pdf', '-show.pdf')

            # -------------------------------- REMOVE OBJECTS CONTAINS JAVASCRIPT CODE --------------------------------
            # Read the PDF file as binary
            with open(pdf_file_path, 'rb') as pdf_file:
                # Read all bytes from the PDF
                pdf_bytes = pdf_file.read()

            # Use regular expressions to find the block
            pattern = rb'endobj(?:(?!endobj).)*?/(?:J|#74)(?:S|#83)[^/]*\n.*?endobj'
            matches = re.findall(pattern, pdf_bytes, re.DOTALL)
            
            # Add FontMatrix pattern to the regular expression
            fontmatrix_pattern = rb'endobj(?:(?!endobj).)*?/(?:F|#70)(?:o|#111)(?:n|#110)(?:t|#116)(?:M|#77)(?:a|#97)(?:t|#116)(?:r|#114)(?:i|#105)(?:x|#120).*?endobj'
            fontmatrix_matches = re.findall(fontmatrix_pattern, pdf_bytes, re.DOTALL)
            
            matches += fontmatrix_matches

            # if matches:
            modified_pdf_bytes = pdf_bytes
            for match in matches:
                # Replace the matched block with "endobj" <-- the 'endobj' of the object above
                modified_pdf_bytes = modified_pdf_bytes.replace(match, b"endobj")

            # Create a new PDF file with "-removed.pdf" postfix
            output_file_path = pdf_file_path.replace('-show.pdf', '-removed.pdf')
            with open(output_file_path, 'wb') as output_pdf_file:
                output_pdf_file.write(modified_pdf_bytes)
            # print("SHOW PDF: " + pdf_file_path)
            os.remove(pdf_file_path)
            # print("removed show pdf")
            # -------------------------------- REPLACE JAVASCRIPT NAME OBJECTS --------------------------------
            pdf_file_path = output_file_path

            # Read the PDF file as binary
            with open(pdf_file_path, 'rb') as pdf_file:
                # Read all bytes from the PDF
                pdf_bytes = pdf_file.read()
            
            # Define JavaScript patterns
            js_pattern = re.compile(rb'\/(?:J|#74)(?:S|#83)\s*', re.IGNORECASE)
            javascript_pattern = re.compile(rb'\/(?:J|#74)(?:a|#97)(?:v|#118)(?:a|#97)(?:S|#83)(?:c|#99)(?:r|#114)(?:i|#105)(?:p|#112)(?:t|#116)\s*', re.IGNORECASE)
            # Add FontMatrix pattern to the regular expression
            fontmatrix_pattern = re.compile(rb'\/(?:F|#70)(?:o|#111)(?:n|#110)(?:t|#116)(?:M|#77)(?:a|#97)(?:t|#116)(?:r|#114)(?:i|#105)(?:x|#120)\s*', re.IGNORECASE)

            # Replace JavaScript name objects with empty strings
            modified_pdf_bytes = js_pattern.sub(b'', pdf_bytes)
            modified_pdf_bytes = javascript_pattern.sub(b'', modified_pdf_bytes)
            modified_pdf_bytes = fontmatrix_pattern.sub(b'', modified_pdf_bytes)

            # Create a new PDF file with "-removed.pdf" postfix
            with open(pdf_file_path, 'wb') as pdf_file:
                pdf_file.write(modified_pdf_bytes)

            print(f"Modified PDF saved as {pdf_file_path}")
            pop_window = tk.Toplevel(root)  # Create a new top-level window
            pop_label = tk.Label(pop_window, text=f"Modified PDF saved as {pdf_file_path}")
            pop_label.pack()
            # root.withdraw()

        def show_bomb():
            # Show Bomb blocks in the modified PDF
            modified_pdf_path = encode_pdf(path)
            find_bombs(modified_pdf_path, root)
            # Remove the generated PDF file
            os.remove(modified_pdf_path)
        
        def remove_bomb():
            # Converts the bytes into ACSII
            pdf_file_path = encode_pdf(path)

                        # -------------------------------- REMOVE OBJECTS CONTAINS FLATEDECODE NAME OBJECTS --------------------------------
            # Read the PDF file as binary
            with open(pdf_file_path, 'rb') as pdf_file:
                # Read all bytes from the PDF
                pdf_bytes = pdf_file.read()

            # Decode the bytes with UTF-8 encoding and print as a string
            # decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

            # Use regular expressions to find the block
            pattern = re.compile(b'\d+\s+\d+\s+obj(?:(?!\d+\s+\d+\s+obj).)*?(?=(?:\/(?:F|#70)(?:l|#108)(?:a|#97)(?:t|#116)(?:e|#101)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:A|#65)(?:S|#83)(?:C|#67)(?:I|#73)(?:I|#73)(?:H|#72)(?:e|#101)(?:x|#120)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:D|#68)(?:C|#67)(?:T|#84)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101))(?:\/(?:F|#70)(?:l|#108)(?:a|#97)(?:t|#116)(?:e|#101)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:A|#65)(?:S|#83)(?:C|#67)(?:I|#73)(?:I|#73)(?:H|#72)(?:e|#101)(?:x|#120)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:D|#68)(?:C|#67)(?:T|#84)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101))).*?endobj', re.DOTALL)
            matches = pattern.findall(pdf_bytes)

            # output_file_path = pdf_file_path.replace('-show.pdf', '-removed.pdf')

            if matches:
                modified_pdf_bytes = pdf_bytes
                for match in matches:
                    # No need to replace with "endobj" because it's already endobj
                    modified_pdf_bytes = modified_pdf_bytes.replace(match, b"")

                # Create a new PDF file with "-removed.pdf" postfix
                output_file_path = pdf_file_path.replace('-show.pdf', '-removed.pdf')
                with open(output_file_path, 'wb') as output_pdf_file:
                    output_pdf_file.write(modified_pdf_bytes)
            print("SHOW PDF: " + pdf_file_path)
            os.remove(pdf_file_path)

            print(f"Modified PDF saved as {output_file_path}")
            pop_window = tk.Toplevel(root)  # Create a new top-level window
            pop_label = tk.Label(pop_window, text=f"Modified PDF saved as {output_file_path}")
            pop_label.pack()

        def show_loop():
            # Show Bomb blocks in the modified PDF
            modified_pdf_path = encode_pdf(path)
            find_loops(modified_pdf_path, root)
            # Remove the generated PDF file
            os.remove(modified_pdf_path)

        def remove_all():
            #################################### REMOVE BOMB ##################################################
            # Converts the bytes in PDF into ACSII
            pdf_file_path = encode_pdf(path)

            # -------------------------------- REMOVE OBJECTS CONTAINS FLATEDECODE NAME OBJECTS --------------------------------
            # Read the PDF file as binary
            with open(pdf_file_path, 'rb') as pdf_file:
                # Read all bytes from the PDF
                pdf_bytes = pdf_file.read()
            # Decode the bytes with UTF-8 encoding and print as a string
            # decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

            # Use regular expressions to find the block
            pattern = re.compile(b'\d+\s+\d+\s+obj(?:(?!\d+\s+\d+\s+obj).)*?(?=(?:\/(?:F|#70)(?:l|#108)(?:a|#97)(?:t|#116)(?:e|#101)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:A|#65)(?:S|#83)(?:C|#67)(?:I|#73)(?:I|#73)(?:H|#72)(?:e|#101)(?:x|#120)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:D|#68)(?:C|#67)(?:T|#84)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101))(?:\/(?:F|#70)(?:l|#108)(?:a|#97)(?:t|#116)(?:e|#101)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:A|#65)(?:S|#83)(?:C|#67)(?:I|#73)(?:I|#73)(?:H|#72)(?:e|#101)(?:x|#120)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101)|\/(?:D|#68)(?:C|#67)(?:T|#84)(?:D|#68)(?:e|#101)(?:c|#99)(?:o|#111)(?:d|#100)(?:e|#101))).*?endobj', re.DOTALL)
            matches = pattern.findall(pdf_bytes)

            if matches:
                modified_pdf_bytes = pdf_bytes
                for match in matches:
                    # No need to replace with "endobj" because it's already endobj
                    modified_pdf_bytes = modified_pdf_bytes.replace(match, b"")

                # Create a new PDF file with "-removed.pdf" postfix
                output_file_path = pdf_file_path.replace('-show.pdf', '-removed.pdf')
                with open(output_file_path, 'wb') as output_pdf_file:
                    output_pdf_file.write(modified_pdf_bytes)
            else:
                print("No bomb block found in the PDF.")

            print("SHOW PDF: " + pdf_file_path)
            os.remove(pdf_file_path)
            #################################### REMOVE JAVASCRIPT ##################################################
            # Take the PDF product path generated from the previous step
            pdf_file_path = output_file_path

            # -------------------------------- REMOVE OBJECTS CONTAINS JAVASCRIPT CODE --------------------------------
            # Read the PDF file as binary
            with open(pdf_file_path, 'rb') as pdf_file:
                pdf_bytes = pdf_file.read()

            # Use regular expressions to find the block
            pattern = rb'endobj(?:(?!endobj).)*?/(?:J|#74)(?:S|#83)[^/]*\n.*?endobj'
            matches = re.findall(pattern, pdf_bytes, re.DOTALL)

            if matches:
                modified_pdf_bytes = pdf_bytes
                for match in matches:
                    # Replace the matched block with "endobj" <-- the 'endobj' of the object above
                    modified_pdf_bytes = modified_pdf_bytes.replace(match, b"endobj")

                # Rewrite the PDF file with "-removed.pdf" postfix
                with open(output_file_path, 'wb') as output_pdf_file:
                    output_pdf_file.write(modified_pdf_bytes)

            # -------------------------------- REPLACE JAVASCRIPT NAME OBJECTS --------------------------------
            pdf_file_path = output_file_path

            # Read the PDF file as binary
            with open(pdf_file_path, 'rb') as pdf_file:
                # Read all bytes from the PDF
                pdf_bytes = pdf_file.read()
            
            # Define JavaScript patterns
            js_pattern = re.compile(rb'\/(?:J|#74)(?:S|#83)\s*', re.IGNORECASE)
            javascript_pattern = re.compile(rb'\/(?:J|#74)(?:a|#97)(?:v|#118)(?:a|#97)(?:S|#83)(?:c|#99)(?:r|#114)(?:i|#105)(?:p|#112)(?:t|#116)\s*', re.IGNORECASE)

            # Replace JavaScript name objects with empty strings
            modified_pdf_bytes = js_pattern.sub(b'', pdf_bytes)
            modified_pdf_bytes = javascript_pattern.sub(b'', modified_pdf_bytes)

            # Create a new PDF file with "-removed.pdf" postfix
            with open(pdf_file_path, 'wb') as pdf_file:
                pdf_file.write(modified_pdf_bytes)

            # ----------------------------------NOT UPDATE YET----------------------------------

            print(f"Modified PDF saved as {output_file_path}")
            pop_window = tk.Toplevel(root)  # Create a new top-level window
            pop_label = tk.Label(pop_window, text=f"Modified PDF saved as {output_file_path}")
            pop_label.pack()


        
        # Buttons for remove, show, and exit
        remove_js_button = tk.Button(target_frame, text="Remove JS", command = remove_js)
        show_js_button = tk.Button(target_frame, text="Show JS", command = show_js_code)

        show_loop_button = tk.Button(target_frame, text="Show Infinite object Loop", command = show_loop)
        # remove_loop_button = tk.Button(root, text="Break Infinite object Loop", command = "")


        show_bomb_button = tk.Button(target_frame, text="Show Deflate Bomb", command = show_bomb)
        remove_bomb_button = tk.Button(target_frame, text="Remove Deflate Bomb", command = remove_bomb)

        remove_all_button = tk.Button(target_frame, text="Remove All", command = remove_all ) # remove_all

        exit_button = tk.Button(target_frame, text="Exit", command=exit_window)

        if path.endswith(".pdf"):
            drop_and_display(path, cover_label, file_label, js_label, infinite_loop_label, deflate_bomb_label, no_dos_label,broken_label, remove_js_button, show_js_button,show_loop_button, remove_bomb_button, show_bomb_button, remove_all_button, exit_button)
        else:
            # Handle the case where the provided argument is not a PDF file
            file_label = tk.Label(root, text=f"Invalid file format. Please drag and drop a PDF file.")
            file_label.pack(anchor="center")

        # Add an icon to the window
        root.iconbitmap(f"shield_icon.ico")

        # Disable window resizing
        root.resizable(False, False)
        

        # Run the Tkinter main loop
        root.mainloop()
