import json
import os
import boto3
print("counting words...")

s3=boto3.client('s3') #Boto3 makes it easy to integrate your Python application with AWS services.
sns = boto3.client('sns')
def lambda_handler(event, context):
    bucketKey = event["Records"][0]["s3"]["object"]["key"]
    bucket = event["Records"][0]['s3']['bucket']['name']
    snsTopicArn = os.environ['snsTopicArn']
    try:
        response = s3.get_object(Bucket=bucket, Key=bucketKey) 
        contents = response['Body'].read()
        text = contents.decode("utf-8")
        words = contents.split()
        numWords = len(words)
        emailMsg = f'The word count in the {bucket} file is {numWords}.'
        msg = sns.publish(TopicArn=snsTopicArn,Message=emailMsg, Subject="Word Count Result")
        return emailMsg
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(bucketKey, bucket))
        raise e
    
