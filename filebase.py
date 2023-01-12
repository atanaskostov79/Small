import boto3

# s3 = boto3.client('s3',
# 	endpoint_url='https://s3.filebase.com',
# 	aws_access_key_id="23FCB76E392E534D222C=",
# 	aws_secret_access_key="nVInKYUnfQqn7SeOnHDbz1vWWvb1dGPl9fvUy9pf")
#
# response = s3.list_buckets()
#
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')

s3 = boto3.client('s3',
                  endpoint_url='https://s3.filebase.com',
                  aws_access_key_id="23FCB76E392E534D222C=",
                  aws_secret_access_key="nVInKYUnfQqn7SeOnHDbz1vWWvb1dGPl9fvUy9pf")

file_path = "/home/crom/Dev/Small/"
bucket_name = "hinata"
key_name = "d.png"
s3.put_object(Body=file_path, Bucket=bucket_name, Key=key_name, ContentType='image/png')

# s3.upload_fileobj( Bucket=bucket_name, Key=key_name, Fileobj=file_path)
