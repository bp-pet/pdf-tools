import os
from PIL import Image, ImageOps

def add_black_bars_to_aspect_ratio(image_path, output_path, target_aspect_ratio=(4, 3)):
    with Image.open(image_path) as img:
        img_aspect_ratio = img.width / img.height
        target_aspect_ratio = target_aspect_ratio[0] / target_aspect_ratio[1]

        if img_aspect_ratio > target_aspect_ratio:
            # Image is too wide
            new_width = img.height * target_aspect_ratio
            result = ImageOps.pad(img, (int(new_width), img.height), color="black")
        elif img_aspect_ratio < target_aspect_ratio:
            # Image is too tall
            new_height = img.width / target_aspect_ratio
            result = ImageOps.pad(img, (img.width, int(new_height)), color="black")
        else:
            # Image already has the target aspect ratio
            result = img

        result.save(output_path)

def process_folder(input_folder, output_folder, target_aspect_ratio=(4, 3)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            add_black_bars_to_aspect_ratio(input_path, output_path, target_aspect_ratio)

# Example usage
input_folder = 'original_images'
output_folder = 'processed_images'
process_folder(input_folder, output_folder, target_aspect_ratio=(4, 3))
