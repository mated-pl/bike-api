import requests, json, csv

response1 = requests.get("http://api.citybik.es/v2/networks")
print(response1.status_code)

response_as_json = json.dumps(response1.json(), sort_keys=True, indent=3)      # converts json object (response1.json()) to json string
json_to_dict = json.loads(response_as_json)        # converts json to dict
networks = json_to_dict["networks"]                 # endpoint keeps all data in dict with 1 key:value pair


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
            response = requests.get(details_endpoint)                                      # get data from endpoint
            response_json = json.dumps(response.json(), sort_keys=True, indent=3)          # convert data from endpoint to json
            response_dict = json.loads(response_json)                                      # convert json to dict
            network_detail = response_dict['network']                                      # all data in the response sits in dict of single key ("network")
            stations = network_detail['stations']                                          # stations is dict with value as list
            freebikes = 0
            for m in range(0, len(stations)):
                freebikes = freebikes + stations[m]['free_bikes']
            csv1_row.append(freebikes)
            # here starts appending csv with list
            with open(csv_file_name, "a") as fp:                    # fp - file pointer
                write_list = csv.writer(fp, dialect='excel')
                write_list.writerow(csv1_row)
            print(csv1_row)
            csv1_row = []


save_net_details(networks,"HR")