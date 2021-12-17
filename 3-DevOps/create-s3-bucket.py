import boto3

s3_client = boto3.client("s3")

response = s3_client.create_bucket(
    Bucket="bucket-name-goes-here",
    ACL="public-read",
    CreateBucketConfiguration={"LocationConstraint": "Region-name"},
)

print(response)
