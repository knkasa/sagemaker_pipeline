import boto3
import json
import pdb

# Use CLI.
session = boto3.Session(
     aws_access_key_id='',
     aws_secret_access_key='',
     region_name=''
    ) 

runtime = session.client('sagemaker-runtime')
endpoint_name = 'xxxxxxx'

payload = json.dumps({"input_text": "This is a test sentence."}) 
payload = "This is a test sentence."

response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="application/x-text",  # this can be found from output log after running estimator.fit().
    Body=payload,
    )

result = json.loads(response["Body"].read().decode())
print("Prediction:", result)
