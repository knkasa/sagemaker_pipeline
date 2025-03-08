import json
import boto3

sagemaker_client = boto3.client("sagemaker")

def lambda_handler(event, context):
    try:
        model_name = event["model_name"]
        endpoint_name = event["endpoint_name"].replace("_", "-")  # Replace underscores
        instance_type = event["instance_type"]
        endpoint_config_name = endpoint_name + "-config2"  # Valid name

        # Create endpoint config
        response = sagemaker_client.create_endpoint_config(
            EndpointConfigName=endpoint_config_name,
            ProductionVariants=[
                {
                    "VariantName": "AllTraffic",
                    "ModelName": model_name,
                    "InstanceType": instance_type,
                    "InitialInstanceCount": 1
                }
            ]
        )
        print(f"Created EndpointConfig: {response}")

        # Create endpoint
        response = sagemaker_client.create_endpoint(
            EndpointName=endpoint_name,
            EndpointConfigName=endpoint_config_name
        )
        print(f"Created Endpoint: {response}")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Endpoint creation started", "EndpointName": endpoint_name})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
