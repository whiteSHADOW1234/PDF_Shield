# upcoming features not completed yet (this is part of the "code_editor.py" file)

# from PyPDF2 import PdfFileReader, PdfFileWriter

# def extract_code(pdf_path):
#     pdf = PdfFileReader(open(pdf_path, "rb"))
#     code = ""
#     for page_num in range(pdf.getNumPages()):
#         page = pdf.getPage(page_num)
#         code += page.extractText()
#     return code

# def update_code(pdf_path, new_code):
#     pdf = PdfFileReader(open(pdf_path, "rb"))
#     output_pdf = PdfFileWriter()

#     for page_num in range(pdf.getNumPages()):
#         page = pdf.getPage(page_num)
#         output_pdf.addPage(page)

#     with open(pdf_path, "wb") as output_file:
#         for page_num in range(output_pdf.getNumPages()):
#             page = output_pdf.getPage(page_num)
#             page.mergePage(page_num)
#         output_pdf.write(output_file)
