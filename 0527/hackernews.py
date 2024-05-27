import json
from operator import itemgetter
import requests


# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
#r.status_code는 응답의 상태 코드를 출력합니다. 상태 코드가 200이면 요청이 성공!
print(f"Status code: {r.status_code}")

#json인 r을 딕셔너리로!!!
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
     url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
     r=requests.get(url)
     print(f"id{submission_id}\tstatus:{r.status_code}")
     response_dict=r.json()
     #response_dict는 각 submission_id에 대해 반복문을 돌면서 매번 새로운 값을 할당받아 변경됩
     #ex)
#      {
#   "by": "ingve",
#   "descendants": 132,
#   "id": 40484591,
#   "kids": [40488296, 40485076, 40485555, 40485208, 40485665, 40486875, 40485476, 40487303, 40485509, 40487264, 40485414, 40487294, 40485013, 40485126, 40484987, 40486072, 40486248],
#   "score": 331,
#   "time": 1716750778,
#   "title": "What the damaged Svalbard cable looked like",
#   "type": "story",
#   "url": "https://www.nrk.no/tromsogfinnmark/this-is-what-the-damaged-svalbard-cable-looked-like-when-it-came-up-from-the-depths-1.16895904"
# }
     
     #for문 안에서 만들어지는 새로운 딕셔너리 
     submission_dict = {
          'title' : response_dict['title'],
          'hn_link' : f"https://news.ycombinator.com/item?id={submission_id}",
          'comments' : response_dict['descendants'],
     }
     submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
                                        #'comments' 키의 값을 기준으로 정렬하겠다는 의미,
                                        #reverse=True는 정렬 순서를 역순으로 바꾸는 옵션
for submission_dict in submission_dicts:
     print(f"\nTitle:{submission_dict['title']}")
     print(f"Discussion link: {submission_dict['hn_link']}")