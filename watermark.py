from PIL import Image, ImageDraw, ImageFont

watermark_text = 'WATERMARK'
input_img_location = 'input.jpg'
output_location = 'output.jpg'




image_scan = Image.open(input_img_location).convert("RGBA")

watermark = Image.new('RGBA', image_scan.size, (255, 255, 255, 0))

draw = ImageDraw.Draw(watermark)

font = ImageFont.truetype("arial.ttf", 800)

textwidth, textheight = draw.textsize(watermark_text, font)

text_image = Image.new('RGBA', (textwidth, textheight), (255, 255, 255, 0))
text_draw = ImageDraw.Draw(text_image)
text_draw.text((0, 0), watermark_text, fill=(200, 256, 200, 180), font=font)

text_image = text_image.rotate(70, expand=1)

text_image_width, text_image_height = text_image.size
x = (image_scan.width - text_image_width) // 2
y = (image_scan.height - text_image_height) // 2

watermark.paste(text_image, (x, y), text_image)

combined = Image.alpha_composite(image_scan, watermark)

combined = combined.convert("RGB")
combined.save(output_location)