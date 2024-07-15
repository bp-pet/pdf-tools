from PIL import Image

def convert_images_to_pdf(image_files, output_pdf_path):
    first_image = Image.open(image_files[0])
    first_image = first_image.convert('RGB')
    
    images = []
    for image_file in image_files[1:]:
        img = Image.open(image_file).convert('RGB')
        images.append(img)

    first_image.save(output_pdf_path, save_all=True, append_images=images)

image_files = ['input1.jpg', 'input2.jpg']
output_pdf_path = 'output.pdf'

convert_images_to_pdf(image_files, output_pdf_path)
