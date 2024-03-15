import boto3
import json

def lambda_handler(event, context):
    # Ensure that the event contains the necessary data, like the image data and the bucket name
    if 'image' not in event or 'bucket_name' not in event or 'user_id' not in event:
        return {
            'statusCode': 400,
            'body': 'Missing required parameters: image, bucket_name, and/or user_id'
        }

    # Get the image data, bucket name, and user ID from the event
    image_data = event['image']
    bucket_name = event['bucket_name']
    user_id = event['user_id']

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the image to the S3 bucket
        s3_client.put_object(Body=image_data, Bucket=bucket_name, Key='uploaded_image.jpg', Metadata={'user_id': user_id})
        return {
            'statusCode': 200,
            'body': 'Image uploaded successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error uploading image: {str(e)}'
        }
