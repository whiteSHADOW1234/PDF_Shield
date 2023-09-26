# The code in this file is make user able to drag and drop a file into the window and display the file name.
# Which is part of the "final.py".

# import tkinter as tk
# from tkinterdnd2 import DND_FILES, TkinterDnD
# from PyPDF2 import PdfFileReader
# from PIL import Image, ImageTk
# import io

# # Function to handle file drop event and display PDF cover
# def drop_and_display(event):
#     file_path = event.data
#     print(file_path)

#     # Display PDF cover if it's a PDF file
#     if file_path.endswith(".pdf}"):
#         # Load the PDF cover image
#         pdf_cover = Image.open("pdf_cover.png")
#         pdf_cover.thumbnail((250, 250))  # Adjust size if needed
#         pdf_cover = ImageTk.PhotoImage(pdf_cover)

#         # Update the label with the PDF cover image
#         cover_label.config(image=pdf_cover)
#         cover_label.image = pdf_cover  # Keep a reference to prevent garbage collection

#         # Display the file name
#         file_name = file_path.split("/")[-1]
#         file_label.config(text=file_name[:-1])
#     else:
#         file_label.config(text="Not a PDF file")

# # Create a Tkinter window
# root = TkinterDnD.Tk()
# root.title("PDF Sheld")

# # Configure the window height
# root.geometry("380x400")

# # Label to display the file path
# file_label = tk.Label(root, text="Drag and drop a PDF file here")
# file_label.pack(pady=10)

# # Label to display the PDF cover
# cover_label = tk.Label(root)
# cover_label.pack(pady=10)

# # Allow file drop on the window
# root.drop_target_register(DND_FILES)
# root.dnd_bind('<<Drop>>', drop_and_display)

# # Add an icon to the window
# root.iconbitmap('sheld_icon.ico')

# # Disable window resizing
# root.resizable(False, False)

# # Run the Tkinter main loop
# root.mainloop()
