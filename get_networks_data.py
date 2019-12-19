import requests, json

response1 = requests.get("http://api.citybik.es/v2/networks")
print(response1.status_code)

def response_to_json (x):                         # creates json from a response
    formatted_response = json.dumps(x, sort_keys=True, indent=3)
    return(formatted_response)

response_json = response_to_json(response1.json())


response1_to_dict = json.loads(response_json)        # converts json to dict
networks = response1_to_dict["networks"]            # all data in the response sits in dict of single key ("networks")
# print(networks[0])                              # key "networks" has 1 value - list of dict. Showing first
# for n in range (50,60):                       # showing 10
#     print(networks[n]['company'])

# print(networks.items())                       # prints whole dictionary
# print(networks[0]['location']['country'])       # prints: 1st item in networks, value for location, value for country



def country_filter(resp_dict, country):
    city_list = []
    for n in range (0,len(resp_dict)):                          # range from 0 to the last element
        if resp_dict[n]['location']['country'] == country:
            city_list.append(resp_dict[n]['location']['city'])
    print('\n'.join(city_list))                                 # prints as a string in next rows
    return (city_list)

# country_filter(networks,"HR")



def data_for_csv (resp_as_dict, country):
    csv1_row = []                                       
    for n in range(0, len(resp_as_dict)):
        if resp_as_dict[n]['location']['country'] == country:
            csv1_row.append(resp_as_dict[n]['location']['country'])     # add item 'country' to the list
            csv1_row.append(resp_as_dict[n]['location']['city'])
            csv1_row.append(resp_as_dict[n]['name'])
            details_endpoint = "http://api.citybik.es" + str((resp_as_dict[n]['href']))     # create details endpoint for certain network
            # from here pulling data from details endpoint
            response = requests.get(details_endpoint)                    # get data from endpoint
            response_json = response_to_json(response.json())              # convert data from endpoint to json
            response_dict = json.loads(response_json)                       # convert json to dict
            network_detail = response_dict['network']                       # all data in the response sits in dict of single key ("network")
            stations = network_detail['stations']                           # stations is dict with value as list
            freebikes = 0
            for m in range(0, len(stations)):
                freebikes = freebikes + stations[m]['free_bikes']
            csv1_row.append(freebikes)
            print(csv1_row)
            csv1_row = []

data_for_csv(networks,"HR")