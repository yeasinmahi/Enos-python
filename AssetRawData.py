from enosapi.request.PostMeasurepointsEnOSRequest import PostMeasurepointsEnOSRequest
from enosapi.client.EnOSDefaultClient import EnOSDefaultClient
import time
import json

enos_api_url = "https://apim-ppe1.envisioniot.com/enosapi/"

# the application configuration created in console
access_key = "af5cf8bd-cc04-4e35-abdf-8229d07a36cd"
secret_key = "8817e5e7-35c4-4252-be24-9cf64668d7be"

# sub-device parameters
device_asset_id = 'UQmqocvc'
product_key = '100'

# OU ID
org_id = "o16931955822231564"

if __name__ == "__main__":
    try:
        timestamp = int(time.time() * 1000)  # timestamp in milliseconds
        struct_measure_point = {
            'Image1': 'local://file1',
            'Sensor': 'PM2_5',
            'UpperLimit': 100,
            'Value': 120,
            'AlertFlag': 1,
            'AlertMessage': 'PM10 over limit'
        }

        measure_points = {
            'Image0': struct_measure_point
        }

        data = [{
            'measurepoints': measure_points,
            'assetId': device_asset_id,
            'time': timestamp
        }]

        param = {
            "data": json.dumps(data)
        }

        # Ensure the file exists and provide the correct path if necessary
        file_path = "image1.jpg"
        with open(file_path, 'rb') as image_file:
            file_to_upload = {"file1": image_file}

            # Prepare the request
            request = PostMeasurepointsEnOSRequest(org_id=org_id, product_key=product_key, params=param,
                                                   upload_file=file_to_upload)

            # Initialize the EnOS API client
            enos_api_client = EnOSDefaultClient(enos_api_url, access_key, secret_key)

            # Send the request and handle the response
            response = enos_api_client.execute(request)

            print(f"Status: {response.status}, Message: {response.msg}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
