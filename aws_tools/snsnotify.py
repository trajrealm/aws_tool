import boto3


def notify(topic_arn, subj, msg, region='us-east-1'):
    sns = boto3.client('sns', region)
    sns.publish(TopicArn=topic_arn, Message=msg, Subject=subj)
