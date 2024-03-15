import boto3
import os
import shutil

def lambda_handler(event, context):
    # Ensure that the event contains the necessary data, like the bucket name and user ID
    if 'bucket_name' not in event or 'user_id' not in event:
        return {
            'statusCode': 400,
            'body': 'Missing required parameters: bucket_name and/or user_id'
        }

    # Get the bucket name and user ID from the event
    bucket_name = event['bucket_name']
    user_id = event['user_id']

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # List all objects in the bucket with the user's photos
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=user_id)

        # Download and delete each photo
        for obj in response.get('Contents', []):
            key = obj['Key']
            # Download the photo
            download_path = f'/tmp/{key}'
            s3_client.download_file(bucket_name, key, download_path)
            # Delete the photo from S3
            s3_client.delete_object(Bucket=bucket_name, Key=key)
        
        return {
            'statusCode': 200,
            'body': 'Photos downloaded and deleted successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error downloading and deleting photos: {str(e)}'
        }
