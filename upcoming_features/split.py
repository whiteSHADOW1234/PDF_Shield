# import fitz  # PyMuPDF
# import PyPDF2

# # Step 1: Extract JavaScript Code
# def extract_javascript_code(pdf_document):
#     doc = fitz.open(pdf_document)
#     javascript_code = ""

#     for page_num in range(doc.page_count):
#         page = doc.load_page(page_num)
#         annotations = page.annots()
#         for annotation in annotations:
#             if annotation.get("Subtype") == "/JavaScript":
#                 javascript_code += annotation.get("JS") + "\n"

#     doc.close()
#     return javascript_code

# # Step 2: Create a New PDF with JavaScript Code on the First Page
# def create_pdf_with_javascript(javascript_code):
#     output_pdf = PyPDF2.PdfFileWriter()
#     output_pdf.add_blank_page(width=595, height=842)  # A4 size, you can adjust the dimensions

#     first_page = output_pdf.pages[0]
#     first_page.mergePage(PyPDF2.PdfFileReader("blank_page.pdf").getPage(0))  # Add a blank page

#     # Add the JavaScript code as a new page
#     pdf_writer = PyPDF2.PdfFileWriter()
#     pdf_writer.add_page(PyPDF2.PdfFileReader(io.BytesIO(javascript_code.encode())).getPage(0))
#     first_page.mergePage(pdf_writer.getPage(0))

#     return output_pdf

# if __name__ == "__main__":
#     input_pdf = "your_input.pdf"
#     output_pdf = "output.pdf"

#     javascript_code = extract_javascript_code(input_pdf)
#     if javascript_code:
#         new_pdf = create_pdf_with_javascript(javascript_code)

#         with open(output_pdf, "wb") as output_file:
#             new_pdf.write(output_file)
#         print(f"JavaScript code extracted and saved to {output_pdf}")
#     else:
#         print("No JavaScript code found in the input PDF.")
