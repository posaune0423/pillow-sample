import json
from PIL import Image, ImageDraw, ImageFont
import boto3
import os


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def generate_img(event, context):
    PROFILE = os.environ["AWS_PROFILE"]
    BUCKET_NAME = os.environ["AWS_S3_BUCKET_NAME"]
    CLOUD_FRONT_URL = os.environ["AWS_CLOUD_FRONT_URL"]

    # generate image
    object = "./img/background.jpg"
    text = event["pathParameters"]["id"]

    img = Image.open(object)

    image_size = img.size
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("./fonts/Times.ttf", 64)
    size = font.getsize(text)

    draw.text(
        ((image_size[0] - size[0]) / 2, (image_size[1] - size[1]) / 2),
        text,
        font=font,
        fill="red",
    )
    img.save("out.png", "PNG", quality=100, optimize=True)

    # upload image to s3
    my_session = boto3.Session(profile_name=PROFILE)
    s3 = my_session.resource("s3")
    bucket = s3.Bucket(BUCKET_NAME)
    filename = "image_" + text + ".png"
    destination = "test/" + filename

    print(destination)

    # Check if the file already exist in the destination
    obj = bucket.Object(destination)
    if is_key_exist(obj):
        body = {
            "code": 400,
            "msg": "The file already exists in the requested path",
        }

        return {"statusCode": 400, "body": json.dumps(body)}
    else:
        bucket.upload_file("./out.png", destination)

    # return response
    body = {
        "msg": "Successfully generate and save image",
        "path": CLOUD_FRONT_URL + destination,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def is_key_exist(obj):
    try:
        obj.get()
        print(True)
        return True
    except:
        print(False)
        return False
