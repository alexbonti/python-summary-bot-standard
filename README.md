# Watsonx.ai Summary Bot - Idea to Deploy

## Importance of LLM for Summarization

Large Language Models (LLMs) revolutionize summarization tasks by generating concise, accurate, and informative summaries, freeing humans from tedious text analysis. LLMs unlock insights, enhance productivity, and transform the way we interact with information.

## Project Overview

This project is a step-by-step guide to deploying a Watsonx.ai summary bot. We'll create a project, build a simple summary service, deploy it to production, and expand its capabilities using agents.

## Steps

1. **Create a Watsonx.ai project**
2. **Create a simple generic summary service**
3. **Deploy application into production as a service**
4. **Deploy a web application to be consumed**
5. **Expand capabilities by using agents**

## Run the application

1. **Clone the project into your system**
2. **Update the API Key into summary-bot.py**
3. **Update the URL to the watsonx service from the watsonx deployment dashboard**
4. **Install the requirements from the requirements.txt using pip**
5. **Run using python summary-bot.py**


## Video Tutorial

https://youtu.be/YEOv_W715uA?si=edHydocm-PmrOQ_4

## Setting API Key to obtain the Authorization Key

1 Set the API key in the environment 
2 Make the CURL call , this will return the authorization token - this wil last one hour.

To authenticate with the Watsonx.ai service, set your API key using the following commands:

```bash
export API_KEY=your_api_key

curl --insecure -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" --data-urlencode "grant_type=urn:ibm:params:oauth:grant-type:apikey" --data-urlencode "apikey=$API_KEY" "https://iam.cloud.ibm.com/identity/token"
