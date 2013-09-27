"""
Libraries for interacting with amazon's S3
"""
import cStringIO
import boto
import settings


def get_bucket(bucket_name, key=settings.AWS['key'],
               secret=settings.AWS['secret']):
    conn = boto.connect_s3(aws_access_key=key, aws_secret_access_key=secret)
    return conn.get_bucket(bucket_name)

    
def save_image(img, bucket_name, output_name):
    out_data = cStringIO.StringIO()
    out_data.save(img, 'PNG')

    key = get_bucket(bucket_name).new_key(output_name)
    key.set_contents_from_string(out_data.getvalue())
