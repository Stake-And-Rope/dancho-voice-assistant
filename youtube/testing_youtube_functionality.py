import json
import os
import sys

# {'kind': 'youtube#searchListResponse', 'etag': 'ipGhmYc4VaDnTC0Dh44tLSbl6qc', 'nextPageToken': 'CAUQAA',
# 'regionCode': 'BG', 'pageInfo': {'totalResults': 12914, 'resultsPerPage': 5},
# 'items': [{'kind': 'youtube#searchResult', 'etag': 'Oio5wja4tmmJWsh6RN19Xhnu8qs',
# 'id': {'kind': 'youtube#playlist', 'playlistId': 'PL2VXyKi-KpYs_f1gu30AGqy0H6x97Vomf'},
# 'snippet': {'publishedAt': '2020-02-12T13:58:52Z',
# 'channelId': 'UC5vr5PwcXiKX_-6NTteAlXw', 'title':
# 'How to use JSON in Python Tutorials', 'description':
# 'This series is designed for digital humanists who have very limited coding experience.
# I introduce you to JSON files and why you ...',
# 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/B8AvytgCBdE/default.jpg', 'width': 120, 'height': 90},
# 'medium': {'url': 'https://i.ytimg.com/vi/B8AvytgCBdE/mqdefault.jpg', 'width': 320, 'height': 180},
# 'high': {'url': 'https://i.ytimg.com/vi/B8AvytgCBdE/hqdefault.jpg', 'width': 480, 'height': 360}},
# 'channelTitle': 'Python Tutorials for Digital Humanities', 'liveBroadcastContent': 'none',
# 'publishTime': '2020-02-12T13:58:52Z'}}, {'kind': 'youtube#searchResult', 'etag': 'fMKVjKng2QuRxnXxL-j8o4roekU',
# 'id': {'kind': 'youtube#playlist', 'playlistId': 'PLhAd8fGavn_akacKRww5BZMrHEszZeXSA'},
# 'snippet': {'publishedAt': '2019-07-25T21:02:55Z', 'channelId': 'UCQ1e3HjlgvB_7AIrlNbdyhw',
# 'title': 'The JSON and The Python', 'description': '',
# 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/9N6a-VLBa2I/default.jpg', 'width': 120, 'height': 90},
# 'medium': {'url': 'https://i.ytimg.com/vi/9N6a-VLBa2I/mqdefault.jpg', 'width': 320, 'height': 180},
# 'high': {'url': 'https://i.ytimg.com/vi/9N6a-VLBa2I/hqdefault.jpg', 'width': 480, 'height': 360}},
# 'channelTitle': 'Ben Dover', 'liveBroadcastContent': 'none', 'publishTime': '2019-07-25T21:02:55Z'}},
# {'kind': 'youtube#searchResult', 'etag': 'etI4KkXyVWWXWmKmCMbc_QNeOYI',
# 'id': {'kind': 'youtube#playlist', 'playlistId': 'PLD6UQscLEFzjS3uJ3MzsiJiL7ZU3-Z7dn'},
# 'snippet': {'publishedAt': '2023-06-04T15:07:17Z', 'channelId': 'UCCb3mrRiyy7YvkNxVWjM6Zg',
# 'title': 'Python JSON', 'description': '',
# 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/zZU0JZmIvKA/default.jpg', 'width': 120, 'height': 90},
# 'medium': {'url': 'https://i.ytimg.com/vi/zZU0JZmIvKA/mqdefault.jpg', 'width': 320, 'height': 180},
# 'high': {'url': 'https://i.ytimg.com/vi/zZU0JZmIvKA/hqdefault.jpg', 'width': 480, 'height': 360}},
# 'channelTitle': "David's Favorite Programing Lists",
# 'liveBroadcastContent': 'none', 'publishTime': '2023-06-04T15:07:17Z'}},
# {'kind': 'youtube#searchResult', 'etag': '3mhtBscaLyUaFdbW3p5J3G_9LF0',
# 'id': {'kind': 'youtube#playlist', 'playlistId': 'PLAF6jaM7Nw47BZf7s4COxpT4FZxR-hvTW'},
# 'snippet': {'publishedAt': '2021-09-30T15:19:47Z', 'channelId': 'UCWtZq9DaZ6as3_GGJtD3lDw',
# 'title': 'Python - JSON | Database',
# 'description': 'All of the videos are sorted in order;
# this is sorted as a step-by-step guide. - Files - Lists - Dictionaries - List of Dictionaries ...',
# 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/pTT7HMqDnJw/default.jpg', 'width': 120, 'height': 90},
# 'medium': {'url': 'https://i.ytimg.com/vi/pTT7HMqDnJw/mqdefault.jpg', 'width': 320, 'height': 180},
# 'high': {'url': 'https://i.ytimg.com/vi/pTT7HMqDnJw/hqdefault.jpg', 'width': 480, 'height': 360}},
# 'channelTitle': 'Rumiru', 'liveBroadcastContent': 'none', 'publishTime': '2021-09-30T15:19:47Z'}},
# {'kind': 'youtube#searchResult', 'etag': 'Cgj2WbfVj8P4DXxdy1XsdMPgOI8',
# 'id': {'kind': 'youtube#playlist', 'playlistId': 'PL9hm1VKOqnvO6dZnoFV8HFYrQUQ7Tdkc5'},
# 'snippet': {'publishedAt': '2020-06-01T18:11:12Z', 'channelId': 'UCbni-TDI-Ub8VlGaP8HLTNw',
# 'title': 'JSON with Python', 'description': '',
# 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/FVECTpahzCQ/default.jpg', 'width': 120, 'height': 90},
# 'medium': {'url': 'https://i.ytimg.com/vi/FVECTpahzCQ/mqdefault.jpg', 'width': 320, 'height': 180},
# 'high': {'url': 'https://i.ytimg.com/vi/FVECTpahzCQ/hqdefault.jpg', 'width': 480, 'height': 360}},
# 'channelTitle': 'Mr Fugu Data Science', 'liveBroadcastContent': 'none', 'publishTime': '2020-06-01T18:11:12Z'}}]}


def get_5_playlists_as_urls():
    with open(os.path.join(sys.path[0], "data_2.json"), "r") as file:
        loaded_data_2 = json.load(file)

    playlist_results_snippets = []

    for key, values in loaded_data_2.items():
        if type(values) == list:
            for result in values:
                this_dict = result
                for id_key, values_dict in this_dict.items():
                    if id_key == "id":
                        for curr_pl_id, playlist_value in values_dict.items():
                            if curr_pl_id == "playlistId":
                                playlist_results_snippets.append(playlist_value)

    base_url = "https://www.youtube.com/results?search_query="

    list_of_urls = [base_url + snippet for snippet in playlist_results_snippets]

    print(list_of_urls)

    return list_of_urls


# get_5_playlists_as_urls()
