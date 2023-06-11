#!/usr/bin/python3

from googleapiclient.discovery import build
from decouple import config
import json

api_key = config('GOOGLE_TOKEN')

def search_results(search):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(q=search, part='snippet', type='playlist')
    results = request.execute()
    # print(results)
    json_results = json.dumps(results)
    print(json_results)
    return results



search_results("how to python to json")

if __name__ == "__main__":
    search_results()
