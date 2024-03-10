import fitz  # PyMuPDF
import re

def encode_pdf(pdf_path):
    try:
    # Open the PDF file using PyMuPDF (won't trigger JavaScript code) to encode the bytes into ACSII
        pdf_document = fitz.open(pdf_path)
        print("PDF PAGE: " + str(pdf_document.page_count))

        # Save the modified PDF with a '-show' postfix
        output_pdf_path = pdf_path.replace('.pdf', '-show.pdf')
        pdf_document.save(output_pdf_path)
        pdf_document.close()
        print(f"Modified PDF saved as '{output_pdf_path}'")
        return output_pdf_path
    except Exception as e:
        print(f"Error: {e}")
        pdf_document.close()
        return "BROKEN PDF"
