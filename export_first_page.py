import PyPDF2


def save_first_page(input_pdf_path, output_pdf_path):

    with open(input_pdf_path, "rb") as input_pdf_file:

        pdf_reader = PyPDF2.PdfReader(input_pdf_file)

        if len(pdf_reader.pages) > 0:
            first_page = pdf_reader.pages[0]
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(first_page)
            with open(output_pdf_path, "wb") as output_pdf_file:
                pdf_writer.write(output_pdf_file)
            print(f"First page saved to {output_pdf_path}")
        else:
            print("The input PDF has no pages.")


input_pdf_path = "input.pdf"
output_pdf_path = "output.pdf"
save_first_page(input_pdf_path, output_pdf_path)
