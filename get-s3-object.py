import boto3


def lambda_handler(request, context):
    s3 = boto3.client('s3')

    if 'bucket' in request:
        bucket = request['bucket']
    else:
        raise Exception('Bucket name not provided!')

    if 'key' in request:
        key = request['key']
    else:
        raise Exception('Key not provided!')

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    except Exception as e:
        print(
            'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e
