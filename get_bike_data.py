import requests, json

response1 = requests.get("http://api.citybik.es/v2/networks")
print(response1.status_code)

def format_response (x):                         # creates json from a response
    formatted_response = json.dumps(x, sort_keys=True, indent=3)
    return(formatted_response)

response_json = format_response(response1.json())


response2dict = json.loads(response_json)        # converts json to dict
networks = response2dict["networks"]            # all data in the response sits in dict of single key ("networks")
# print(networks[0])                              # key "networks" has 1 value - list of dict. Showing first
# for n in range (50,60):                       # showing 10
#     print(networks[n]['company'])

# print(networks.items())                       # prints whole dictionary

# print(networks[0]['location']['country'])       # prints: 1st item in networks, value for location, value for country

HR_list =  []
for n in range (0,len(networks)):               # range from 0 to the last element
    if networks[n]['location']['country'] == "HR":
        HR_list.append(networks[n]['location']['city'])
# print(HR_list)                                # prints as a list
print('\n'.join(HR_list))                       # prints as a string in next rows


#TODO: zrob tu porzadek - funkcje. Merge to master, push. Zaloz nowy branch na zapisywanie do pliku