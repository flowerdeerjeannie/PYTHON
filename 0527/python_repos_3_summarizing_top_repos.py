import requests


# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

#딕셔너리는 {{{ }}} 중괄호 튀김 
print(f"Total repositories: {response_dict['total_count']}") #검색된 리포지토리의 총 개수를 출력합니다.
print(f"Complete results: {not response_dict['incomplete_results']}")
#not을 붙이면 안의 내용이 True 일때는 False를 출력함. 

repo_dicts = response_dict['items'] 
#전체에서 items 안에 { 담겨있는거만 repo_dicts라고 부르기로 한다.
#repo_dicts는 여러 아이템(리포지토리 정보)을 포함하는 '리스트'
print(f"Repositories returned: {len(repo_dicts)}")
#len(repo_dicts)는 리스트에 포함된 아이템(리포지토리 정보)의 개수
#repo_dicts { 안에는 총 몇개냐는거지 

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    #데이터 시각화를 하려면 저장소가 포함되어야하기 때문에
    #API호출이 반환하는 저장소를 모두 시각화할 수 있도록 각 저장소를 순회하는 루프 만들어줌
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}") #오너 안으로 { 하나 더 들어가서 login }
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")