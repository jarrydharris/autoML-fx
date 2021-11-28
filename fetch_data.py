import pandas as pd
import requests
import json
from datetime import date, timedelta, datetime
import os

DATA_PATH = "data/raw.csv"

def request_data(base = "AUD", path = DATA_PATH):
    

    # free currency api key should be an env variable export API_FX=key
    api_key = os.getenv('API_FX')
    if api_key is None:
        # TODO: Error handling
        return -1

    # todays date
    date_to = date.today().strftime("%Y-%m-%d")
    
    if os.path.isfile(path):
        # if data already exists we query from the last date recorded
        date_from = pd.read_csv(path)['dates'].iloc[-1]
        if date_to == date_from:
            #TODO: Error handling
            return -2
        # Incrementing date from by a day so we dont get duplicates
        date_from = datetime.strptime(date_from, "%Y-%m-%d")
        date_from += timedelta(days=1)
        date_from = date_from.strftime("%Y-%m-%d")
    else:
        date_from = "2020-10-01"


    # Building request url as per freecurrencyapi docs
    url = "https://freecurrencyapi.net/api/v2/historical"
    query = "{}?apikey={}&base_currency={}&date_from={}&date_to={}".format(url, 
        api_key, 
        base, 
        date_from, 
        date_to)

    request = requests.get(query)
    if request.status_code != 200:
        return -3
    return request

def parse_data(request, target = "USD", path = DATA_PATH):
    data_json = json.loads(request.text)
    data = {date: data_json['data'][date][target] for date in list(data_json['data'].keys())}
    viz = {'dates': list(data.keys()), 'price': list(data.values())}
    if os.path.isfile(path):
        # if data already exists we append the latest request to existing file
        pd.DataFrame(viz).to_csv(path, mode='a', header=False, index=False)
    else:
        # else we create the file
        pd.DataFrame(viz).to_csv(path, index=False)
    return 0

if __name__ == "__main__":
    request = request_data()
    if request == -1:
        # TODO: Error handling
        print("ERROR: No API key.")
    elif request == -2:
        print("Data up to date.")
    elif request == -3:
        # TODO: Gotta handle this better
        print("ERROR: Response")
    else:
        parse_data(request)
        print("Updated data...")