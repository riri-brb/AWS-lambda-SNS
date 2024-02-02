# AWS Lambda Word Count Mini Project

## Overview:

This mini project demonstrates the implementation of a serverless word counting solution using AWS Lambda, S3, and SNS. The primary objective is to automatically count the number of words in a text file upon upload to an S3 bucket and report the results through an email notification.

## Steps to Replicate:

### 1. Lambda Function Creation:

- Use the AWS Management Console to create a Lambda function in Python.
- Apply the provided IAM role (LambdaAccessRole) with necessary permissions for CloudWatch Logs, SNS, and S3.

### 2. Email Notification Setup:

- Establish an Amazon SNS topic to handle email notifications.
- Format the response message to display the word count in the uploaded text file.

### 3. S3 Bucket Configuration:

- Configure an S3 bucket to invoke the Lambda function automatically upon text file uploads.

### 4. Testing:

- Upload sample text files with varying word counts to the S3 bucket.
- Verify that the Lambda function is triggered and word count results are sent through the configured SNS topic.

## Architecture Overview:

### Lambda Function:

- Written in Python, the Lambda function processes text files.
- Utilizes the provided IAM role (LambdaAccessRole) for necessary permissions.

### S3 Bucket:

- Configured to trigger the Lambda function upon text file uploads.

### SNS Topic:

- Sends email notifications containing word count results.
- Optionally, can be extended to send SMS notifications.
