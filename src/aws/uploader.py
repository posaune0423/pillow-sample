import boto3
import json


class Uploader:
    def __init__(
        self,
        aws_profile,
        aws_s3_bucket_name,
        aws_cloud_front_url,
    ) -> None:
        my_session = boto3.Session(profile_name=aws_profile)
        self.s3 = my_session.resource("s3")
        self.aws_s3_bucket_name = aws_s3_bucket_name
        self.aws_cloud_front_url = aws_cloud_front_url

    def upload(self, filename, img_path):
        bucket = self.s3.Bucket(self.aws_s3_bucket_name)
        destination = "test/" + filename
        obj = bucket.Object(destination)
        if is_key_exist(obj):
            return False
        else:
            try:
                bucket.upload_file(img_path, destination)
                return self.aws_cloud_front_url + destination
            except Exception as e:
                print(e)


def is_key_exist(obj):
    try:
        obj.get()
        print(True)
        return True
    except:
        print(False)
        return False
