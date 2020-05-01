import boto3
import pandas as pd

# Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)
s3 = boto3.resource('s3')

#for uploading a file
file = "datafile/veh.csv"
data = open(file, 'rb')
s3.Bucket('cdk-qa-test').put_object(Key='ahmad_idrees.csv', Body=data)

#for downloading a file
s3.meta.client.download_file('test', 'ahmad_idrees.csv', '/Users/ahmad.idrees/Desktop/ahmad_idrees.csv')

#for reading a file
bucket = "cdk-qa-test"
file_name = "ahmad_idrees.csv"
new = boto3.client('s3')
obj = new.get_object(Bucket=bucket, Key=file_name)
initial_df = pd.read_csv(obj['Body'])
print(initial_df)

#for deleting a file
s3.Object('cdk-qa-test', 'ahmad_idrees.csv').delete()