import requests
api_key = "58ccb019ba77a81a652e56e3dd480a76"
user_agent = "UserPL"

headers = {
    'user-agent':user_agent
}

payload = {
    'api_key':api_key,
    'method':'chart.gettopartists',
    'format': 'json'
}

request1 = requests.get('http://ws.audioscrobbler.com/2.0/', headers = headers, params=payload)
print(request1.status_code)