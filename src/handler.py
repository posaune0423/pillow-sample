import json
import os
from .aws.uploader import Uploader
from .utils.image_helper import generate


def generate_img(event, context):
    PROFILE = os.environ["AWS_PROFILE"]
    BUCKET_NAME = os.environ["AWS_S3_BUCKET_NAME"]
    CLOUD_FRONT_URL = os.environ["AWS_CLOUD_FRONT_URL"]

    uploader = Uploader(PROFILE, BUCKET_NAME, CLOUD_FRONT_URL)

    # generate image
    text = event["pathParameters"]["id"]
    img_path = generate(text)

    # upload image to s3
    filename = "image_" + text + ".png"
    result = uploader.upload(filename, img_path)
    if result == False:
        body = {
            "code": 400,
            "msg": "The file already exists in the requested path",
        }

        return {"statusCode": 400, "body": json.dumps(body)}

    # return response
    body = {
        "code": 200,
        "msg": "Successfully generate and save image",
        "path": result,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
