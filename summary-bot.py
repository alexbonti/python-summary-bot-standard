from flask import Flask, request, jsonify
import requests
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import time
import threading

# Replace 'your_api_key' with your actual IBM Cloud API key
API_KEY = 'RfNdFU_4-OKVxnXprcrfC2dlraH06Yu7jiQwPJnTmF9f'
app = Flask(__name__)

IAM_TOKEN = None
IAM_TOKEN_EXPIRATION = 0

url = "https://iam.cloud.ibm.com/identity/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}
data = {
    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
    "apikey": API_KEY
}



def get_iam_token():
    global IAM_TOKEN_EXPIRATION
    response = requests.post(url, headers=headers, data=data, verify=False)
    token_info = response.json()
    IAM_TOKEN_EXPIRATION = time.time() + token_info.get("expires_in", 3600) - 60  # 60 seconds before actual expiration
    return token_info.get("access_token")

def get_valid_iam_token():
    global IAM_TOKEN
    if IAM_TOKEN is None or time.time() > IAM_TOKEN_EXPIRATION:
        IAM_TOKEN = get_iam_token()
    return IAM_TOKEN



@app.route('/publish_results', methods=['POST'])
def main():
    #context = request.json['context']
    document = request.json['document']
    token = get_valid_iam_token()

    url = "https://us-south.ml.cloud.ibm.com/ml/v1/deployments/summary_standard_bot/text/generation?version=2021-05-01"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "parameters": {
            "prompt_variables": {
                "document": document
            }
        }
    }

    global result

    result = None

    try:
        response = requests.post(url, headers=headers, json=data, verify=False)
        if response.status_code == 401:
            token = get_valid_iam_token()  # refresh token if expired
            headers["Authorization"] = f"Bearer {token}"
            response = requests.post(url, headers=headers, json=data, verify=False)
        result = response.json()
        print("=================")
        print(result)
        print("=================")
    except Exception as e:
        #print(e)
        return jsonify({"error": str(e)}), 500


    return {"response":result['results'][0]['generated_text']}
# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)