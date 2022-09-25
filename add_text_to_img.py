import sys
from PIL import Image, ImageDraw, ImageFont


object = sys.argv[1]
text = sys.argv[2]

img = Image.open(object)

image_size = img.size
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Arial Unicode.ttf", 64)
size = font.getsize(text)


draw.text(
    ((image_size[0] - size[0]) / 2, (image_size[1] - size[1]) / 2),
    text,
    font=font,
    fill="red",
)
img.save("out.png", "PNG", quality=100, optimize=True)
