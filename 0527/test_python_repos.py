import requests


url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print({r.status_code})

if r.status_code == 200:
     top_stories = r.json()

     num_items = len(top_stories)
     print(f"number of top stories : {num_items}")
else:
     print("request failed")