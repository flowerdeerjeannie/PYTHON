import requests


# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
# 정의된 url로 GET 요청을 보냅니다. headers를 추가하여 API 호출 시 필요한 헤더를 포함하여 r에 저장함.

r = requests.get(url, headers=headers)
#r.status_code는 응답의 상태 코드를 출력합니다. 상태 코드가 200이면 요청이 성공!
print(f"Status code: {r.status_code}")

# r.json() 메서드는 응답 객체를 JSON 형식에서 Python의 딕셔너리로 변환합니다.
response_dict = r.json()

# Process results.
print(response_dict.keys())