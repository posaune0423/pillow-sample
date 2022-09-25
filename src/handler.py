import json
import os
from .aws.uploader import Uploader
from .utils.image_helper import generate


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

    uploader = Uploader(PROFILE, BUCKET_NAME, CLOUD_FRONT_URL)

    # generate image
    text = event["pathParameters"]["id"]
    img_path = generate(text)

    # upload image to s3
    filename = "image_" + text + ".png"
    destination = uploader.upload(filename, img_path)

    # return response
    body = {
        "msg": "Successfully generate and save image",
        "path": destination,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
