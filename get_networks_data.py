import requests, json, csv

response1 = requests.get("http://api.citybik.es/v2/networks")
print(response1.status_code)

def response_to_json (x):                         # creates json from a response
    formatted_response = json.dumps(x, sort_keys=True, indent=3)
    return(formatted_response)

response_as_json = response_to_json(response1.json())


json_to_dict = json.loads(response_as_json)        # converts json to dict
networks = json_to_dict["networks"]            # all data in the response sits in dict of single key ("networks")

# print(networks[0])                              # key "networks" has 1 value - list of dict. Showing first
# for n in range (50,60):                       # showing 10
#     print(networks[n]['company'])
# print(networks.items())                       # prints whole dictionary
# print(networks[0]['location']['country'])       # prints: 1st item in networks, value for location, value for country



def cities_from_country(resp_dict, country):
    city_list = []
    for n in range (0,len(resp_dict)):                          # range from 0 to the last element
        if resp_dict[n]['location']['country'] == country:
            city_list.append(resp_dict[n]['location']['city'])
    print('\n'.join(city_list))                                 # prints as a string in next rows
    return (city_list)

# cities_from_country(networks,"HR")



def print_net_details (resp_as_dict, country):
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

# print_net_details(networks,"HR")

def save_net_details (resp_as_dict, country):  # funkcja do zapisania api do pliku
    csv_file_name = str(country)+"_networks.csv"
    csv_file = open(csv_file_name, "w").close()
    csv1_row = []
    for n in range(0, len(resp_as_dict)):
        if resp_as_dict[n]['location']['country'] == country:
            csv1_row.append(resp_as_dict[n]['location']['country'])     # add item 'country' to the list
            csv1_row.append(resp_as_dict[n]['location']['city'])
            csv1_row.append(resp_as_dict[n]['name'])
            details_endpoint = "http://api.citybik.es" + str((resp_as_dict[n]['href']))     # create details endpoint for certain network
            # here starts pulling data from details endpoint
            response = requests.get(details_endpoint)                    # get data from endpoint
            response_json = response_to_json(response.json())              # convert data from endpoint to json
            response_dict = json.loads(response_json)                       # convert json to dict
            network_detail = response_dict['network']                       # all data in the response sits in dict of single key ("network")
            stations = network_detail['stations']                           # stations is dict with value as list
            freebikes = 0
            for m in range(0, len(stations)):
                freebikes = freebikes + stations[m]['free_bikes']
            csv1_row.append(freebikes)
            # here starts appending csv with list
            with open(csv_file_name, "a") as fp:
                write_list = csv.writer(fp, dialect='excel')
                write_list.writerow(csv1_row)
            print(csv1_row)
            csv1_row = []

save_net_details(networks,"HR")