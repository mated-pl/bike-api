import requests, json, time


def lastfm_get(payload):            # function to get response, argument is dict with 1 element - API method
    headers = {                     # heder defined according to API spec
        'user-agent': "UserPL"
    }

    payload['api_key'] = "58ccb019ba77a81a652e56e3dd480a76"     # payload defined as dict according to API spec
    payload['format'] = "json"
    response = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    return response

# request1 = lastfm_get({'method':'chart.gettopartists'})
# print(request1.status_code)

def print_json(response):
    txt_resp = json.dumps(response, sort_keys=True, indent=3)
    return txt_resp

# print(print_json(request1.json()))                 # TODO: r.json() !!! that's how to print directly after dumps

results = []
page = 1
headers = {
    'user-agent': "UserPL"
}

payload = {
    'method':'chart.gettopartists',
    'api_key' : "58ccb019ba77a81a652e56e3dd480a76",
    'format' : "json",
    'limit' : "2",          # will show 2 artists per page
}

# while page < 4:                                    # while loop - first 3 pages
#     payload['page'] = page                         # update payload with page number
#     request2 = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
#     results.append(request2.json())
#     page += 1
# print(json.dumps(results, sort_keys=True, indent=3))      # don't need method .json() to print as 'results' is list here
# for n in range(len(results)):                             # prints first artist from each page
#     print(results[n]['artists']["artist"][0]['name'])

pages_number = 5
payload2 = {
    'method':'chart.gettopartists',
    'limit': '10',
}
while page < pages_number:
    payload2['page'] = page
    print("Requesting page {}/{}".format(page, pages_number-1))            # print some output so we can see the status
    response = lastfm_get(payload2)          # make the API call
    print(response)
    if response.status_code != 200:             # if we get an error, print the response and halt the loop
        print("error occured: " + response.text)
        break
    all_pages_number = response.json()['artists']['@attr']['totalPages']    # extract pagination info
    results.append(response)
    print("next request delayed by: 1s")
    time.sleep(1)               # delay before next request
    if page == pages_number - 1:    # after last request show total pages number and break loop
        print("Total pages = " + all_pages_number)
        break
    page += 1

print(results)
# TODO: why response does contain only status code???
# TODO: continue with pandas steps from tutorial https://www.dataquest.io/blog/last-fm-api-python/﻿
