from googleapiclient.discovery import build


api_key = "AIzaSyDX_OCsTfYOHLs2hosNys3B8WSCsD3ghUc"


def search_results():
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(q="boating", part='snippet', type='playlist')
    results = request.execute()
    return results


if __name__ == "__main__":
    search_results()