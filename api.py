import requests
import csv
import random

# Universal variables
base_url = "https://jlukasmay.kintone.com"
quiz_api_token = "VYSaXkOJ3QITu4pRPxEUzhv9SH2lBqTxvsqfJZSb"
user_api_token = "E00ZFyb7RKwcUXXQeR8DZU2fjGkp2WBgIYWfZMIE"
post_endpoint = f"{base_url}/k/v1/record.json"
get_all_endpoint = f"{base_url}/k/v1/records.json"
quiz_app_id = "3"
user_app_id = "5"


# Headers for API requests
post_headers = {
    "Content-Type": "application/json",
    "X-Cybozu-API-Token": quiz_api_token,
}

get_headers = {
    "X-Cybozu-API-Token": quiz_api_token,
}

# Param defaults for API requests
params = {
    "app": quiz_app_id,
}

def post_data(data, endpoint=post_endpoint, headers=post_headers):
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

def get_data(record_id=None):
    try:
        # Send GET request to retrieve records
        if not record_id == None:
            params["id"] = record_id
            response = requests.get(post_endpoint, headers=get_headers, params=params)
        else:
            response = requests.get(get_all_endpoint, headers=get_headers, params=params)

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
        response = requests.post(post_endpoint, headers=post_headers, json=data)
        if response.status_code == 200:
            print("Record created successfully!")
        else:
            print("Failed to create record. Status code:", response.status_code)

unique_questions = [i for i in range(0, len(get_data().get('records')))]

def reset_limit_questions():
    return len(get_data().get('records'))

def get_question(unique=False):
    global unique_questions  # Declare unique_questions as a global variable
    data = get_data()
    if unique:
        rand = random.choice(unique_questions)
        unique_questions.remove(rand)
        if not unique_questions:  # Check if unique_questions is empty
            unique_questions = [i for i in range(0, len(data.get('records')))]
    else:
        rand = random.randrange(0, len(data.get('records')))
    question = data.get('records')[rand].get('question').get('value')
    option1 = data.get('records')[rand].get('option1').get('value')
    option2 = data.get('records')[rand].get('option2').get('value')
    option3 = data.get('records')[rand].get('option3').get('value')
    option4 = data.get('records')[rand].get('option4').get('value')
    correct = data.get('records')[rand].get('correct').get('value')
    return (question, option1, option2, option3, option4, correct)
