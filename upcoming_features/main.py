# import tkinter as tk
# from tkinter import filedialog
# from pdf_editor import extract_code, update_code
# from code_editor import CodeEditor

# def open_pdf():
#     file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
#     if file_path:
#         code = extract_code(file_path)
#         code_editor.set_text(code)

# def save_pdf():
#     file_path = filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")])
#     if file_path:
#         code = code_editor.get_text()
#         update_code(file_path, code)

# root = tk.Tk()
# root.title("PDF Code Editor")

# menu = tk.Menu(root)
# root.config(menu=menu)

# file_menu = tk.Menu(menu)
# menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Open PDF", command=open_pdf)
# file_menu.add_command(label="Save PDF", command=save_pdf)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)

# code_editor = CodeEditor(root)
# code_editor.pack()

# root.mainloop()
