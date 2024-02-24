import requests

# Define the base URL for the Kintone API
base_url = "https://jlukasmay.kintone.com"

# Define the API token
api_token = "VYSaXkOJ3QITu4pRPxEUzhv9SH2lBqTxvsqfJZSb"

# Define the endpoint URL to test connection (e.g., Get App)
endpoint = f"{base_url}/k/v1/apps.json"

# Define request headers with API token for authentication
headers = {
    "X-Cybozu-API-Token": api_token,
}

try:
    # Send GET request to test connection
    response = requests.get(endpoint, headers=headers)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        print("Connection to Kintone successful!")
    else:
        print("Failed to connect to Kintone. Status code:", response.status_code)

except requests.RequestException as e:
    print("Error connecting to Kintone:", e)
