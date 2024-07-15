from pdf2image import convert_from_path

pdf_path = 'input.pdf'
pages = convert_from_path(pdf_path, dpi=300)
for i, page in enumerate(pages):
    page.save(f'output_page_{i + 1}.jpg', 'JPEG')