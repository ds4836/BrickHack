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
data_holder = {
    "app": "3",
    "record": {
        "test1": {"value": "dsjfjd"},
        "test2": {"value": "dsafa"},
        "number": {"value": "134"},
        "multiChoice": {"value": ["sample1", "sample2", "sample3", "sample4"]},
    }
}

try:
    # Send GET request to retrieve records
    response = requests.get(endpoint, headers=headers)

    # Check if request was successful (status code 200)
    print(response.status_code)
    if response.status_code == 200:
        # Extract data from response JSON
        data = response.json()

        # Process the data as needed
        # For example, store it in a variable
        records = data.get("records", [])

        # Print the records or further process them
        print("Retrieved records:", records)
except requests.RequestException as e:
    print("Error creating record:", e)
