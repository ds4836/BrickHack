import requests
import json

# Define the base URL for the Kintone API
base_url = "https://jlukasmay.kintone.com"

# Define the API token
api_token = "VYSaXkOJ3QITu4pRPxEUzhv9SH2lBqTxvsqfJZSb"
app_id = "3"
record_id = "60"

# Define the endpoint URL to create a record
endpoint = f"{base_url}/k/v1/records.json"

# Define request headers with API token for authentication
headers = {
    "X-Cybozu-API-Token": api_token,
}

params = {
    "app": app_id,
}

try:
    # Send GET request to retrieve records
    response = requests.get(endpoint, headers=headers, params=params)

    # Check if request was successful (status code 200)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        # Extract data from response JSON
        data = response.json()
        question = data.get('records')[0].get('question').get('value')
        option1 = data.get('records')[0].get('option1').get('value')
        print("Retrieved data:", data)
        print()
        print(question)
        print(option1)
except requests.RequestException as e:
    print("Error creating record:", e)
