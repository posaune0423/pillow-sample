from PIL import Image, ImageDraw, ImageFont

def generate(text, color="red"):
    object = "./img/background.jpg"
    img = Image.open(object)
    image_size = img.size
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("./fonts/Times.ttf", 64)
    size = font.getsize(text)

    draw.text(
        ((image_size[0] - size[0]) / 2, (image_size[1] - size[1]) / 2),
        text,
        font=font,
        fill=color,
    )

    out_path = "out.png"
    img.save(out_path, "PNG", quality=100, optimize=True)
    return out_path
