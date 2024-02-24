import requests

# Define the base URL for the Kintone API
base_url = "https://jlukasmay.kintone.com"

# Define the API token
api_token = "VYSaXkOJ3QITu4pRPxEUzhv9SH2lBqTxvsqfJZSb"

# Define the endpoint URL to create a record
endpoint = f"{base_url}/k/v1/record.json"

# Define request headers with API token for authentication
headers = {
    "Content-Type": "application/json",
    "X-Cybozu-API-Token": api_token,
}

# Define the data to be inputted
data = {
    "app": "3",
    "record": {
        "Field1": {"value": "Value1"},
        "Field2": {"value": "Value2"},
        # Add more fields as needed
    }
}

try:
    # Send POST request to create a record
    response = requests.post(endpoint, headers=headers, json=data)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        print("Record created successfully!")
    else:
        print("Failed to create record. Status code:", response.status_code)

except requests.RequestException as e:
    print("Error creating record:", e)
