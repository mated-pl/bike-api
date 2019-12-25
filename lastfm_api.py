import requests, json

def lastfm_get(payload):            # function to get response, argument is dict with 1 element - API method
    headers = {                     # heder defined according to API spec
        'user-agent': "UserPL"
    }

    payload['api_key'] = "58ccb019ba77a81a652e56e3dd480a76"     # payload defined as dict according to API spec
    payload['format'] = "json"
    # payload['limit'] = "1"
    # payload['page'] = "2"
    response = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    return response

# request1 = lastfm_get({'method':'chart.gettopartists'})
# #print(request1.status_code)

def print_json(response):
    txt_resp = json.dumps(response, sort_keys=True, indent=3)
    return txt_resp

# print(print_json(request1.json()))                 # TODO: r.json() !!! that's how to print directly after dumps



results = []
page = 1
total_pages = 999999
headers = {
    'user-agent': "UserPL"
}
payload = {
    'method':'chart.gettopartists',
    'api_key' : "58ccb019ba77a81a652e56e3dd480a76",
    'format' : "json",
    'limit' : "3",
    'page' : 1
}

# while page < 5:
#     payload['page'] = page
#     request2 = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
#     results.append(request2.json())
#     page += 1
#
# print(json.dumps(results, sort_keys=True, indent=3))
# for n in range(len(results)):
#     print(results[n]['artists']["artist"][0]['name'])

request2 = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
print(json.dumps(request2.json(), sort_keys=True, indent=3))