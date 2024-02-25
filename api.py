import requests
import csv

# Universal variables
base_url = "https://jlukasmay.kintone.com"
api_token = "VYSaXkOJ3QITu4pRPxEUzhv9SH2lBqTxvsqfJZSb"
endpoint = f"{base_url}/k/v1/record.json"
app_id = "3"
record_id_default = "60"

# Headers for API requests
post_headers = {
    "Content-Type": "application/json",
    "X-Cybozu-API-Token": api_token,
}

get_headers = {
    "X-Cybozu-API-Token": api_token,
}

# Param defaults for API requests
params = {
    "app": app_id,
    "id": record_id_default,
}

def post_data(data):
    try:
        # Send POST request to create a record
        response = requests.post(endpoint, headers=post_headers, json=data)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            print("Record created successfully!")
        else:
            print("Failed to create record. Status code:", response.status_code)

    except requests.RequestException as e:
        print("Error creating record:", e)

def get_data(record_id=record_id_default):
    params["id"] = record_id
    try:
        # Send GET request to retrieve records
        response = requests.get(endpoint, headers=get_headers, params=params)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        
    except requests.RequestException as e:
        print("Error creating record:", e)

def parse_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        records = [row for row in reader]

    # Convert records to JSON format
    for record in records:
        data = {"app": "3", "records": record}
        response = requests.post(endpoint, headers=post_headers, json=data)
        if response.status_code == 200:
            print("Record created successfully!")
        else:
            print("Failed to create record. Status code:", response.status_code)

# parse_csv("/Users/lukasmay/Downloads/New App_20240224T142352-0800.csv")