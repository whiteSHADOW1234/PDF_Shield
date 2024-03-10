from functions.check_js import check_js
from functions.check_bomb import check_bomb
from functions.check_loop import check_loop
from functions.encode_pdf import encode_pdf
from PIL import Image, ImageTk
import tkinter as tk
import os

# Function to handle file drop event and display PDF picture
def drop_and_display(file_path, cover_label, file_label, js_label, infinite_loop_label, deflate_bomb_label, no_dos_label,broken_label, remove_js_button, show_js_button, show_loop_button, remove_bomb_button, show_bomb_button,remove_all_button, exit_button):
    no_dos_detected = True

    # Display PDF cover if it's a PDF file
    if file_path.endswith(".pdf"):
        # Load the PDF cover image
        pdf_cover = Image.open(".\\pdf_cover.png")
        pdf_cover.thumbnail((250, 250))
        pdf_cover = ImageTk.PhotoImage(pdf_cover)

        # Update the label with the PDF cover image
        cover_label.config(image = pdf_cover)
        cover_label.image = pdf_cover  # Keep a reference to prevent garbage collection

        # Display the file name
        file_name = file_path.split("/")[-1]
        file_label.config(text=file_name[:30] + '...' if len(file_name) > 38 else file_name)

        check_file_path = encode_pdf(file_path)

        # Check is the PDF is not broken
        if  check_file_path == "BROKEN PDF":
            broken_label.pack()
            exit_button.pack()
            return

        else:
            # Check for JavaScript code manually
            has_js_code = check_js(check_file_path)
            has_deflate_bomb = check_bomb(check_file_path)
            has_infinite_loop = check_loop(check_file_path)


            if has_js_code:
                no_dos_detected = False

                # Show "JavaScript code detected" message which is under the image
                js_label.pack()

                # Show "Remove" "Exit" and "Show" buttons
                remove_js_button.pack() # side = tk.LEFT, pady = 10, anchor = tk.N, expand = True
                show_js_button.pack()
                # exit_button.pack()

                # Hide other messages
                # no_dos_label.pack_forget()
                # infinite_loop_label.pack_forget()
                # deflate_bomb_label.pack_forget()

            # # ---------------------------- INFINITE LOOP ---------------------------
            if has_infinite_loop:
                # Show "Possible to have Deflate Bomb" message which is under the image
                padding = 0  # Padding for the message
                if no_dos_detected == False:
                    padding = 10

                infinite_loop_label.pack(pady=padding)

                no_dos_detected = False

                # Show "Show Loop" buttons
                show_loop_button.pack()

                # Hide other messages and the "Remove" button
                # remove_js_button.pack_forget()
                # js_label.pack_forget()
                # infinite_loop_label.pack_forget()
                # no_dos_label.pack_forget()


            # -------------------------DEFLATE BOMB ----------------------------------
            if has_deflate_bomb:
                # Show "Possible to have Deflate Bomb" message which is under the image
                padding = 0  # Padding for the message
                if no_dos_detected == False:
                    padding = 10

                deflate_bomb_label.pack(pady=padding)

                no_dos_detected = False
                # Show "Exit" and "Show Bomb" buttons
                remove_bomb_button.pack()
                show_bomb_button.pack()
                # exit_button.pack()

                # Hide other messages and the "Remove" button
                # remove_js_button.pack_forget()
                # js_label.pack_forget()
                # infinite_loop_label.pack_forget()
                # no_dos_label.pack_forget()

            if no_dos_detected:
                # Show "No DOS methods detected" message which is under the image
                no_dos_label.pack()

                # Show "Exit" button
                exit_button.pack()

                # Hide other messages and buttons
                # js_label.pack_forget()
                # infinite_loop_label.pack_forget()
                # deflate_bomb_label.pack_forget()
                # remove_js_button.pack_forget()
                # show_js_button.pack_forget()
            
            # Hide other messages and buttons
            if not has_js_code:
                js_label.pack_forget()
                remove_js_button.pack_forget()
                show_js_button.pack_forget()

            if not has_infinite_loop:
                infinite_loop_label.pack_forget()

            if not has_deflate_bomb:
                deflate_bomb_label.pack_forget()

            if has_js_code and has_deflate_bomb:
                remove_all_button.pack(pady = 10)
                exit_button.pack()
            else:
                exit_button.pack(pady = 10)
            
            # Remove the show file after checking
            os.remove(check_file_path)
    else:
        # Remove the PDF cover image
        cover_label.config(image="")
        # Remove the buttons
        exit_button.pack_forget()
        remove_js_button.pack_forget()
        show_js_button.pack_forget()

        file_label.config(text="Not a PDF file")