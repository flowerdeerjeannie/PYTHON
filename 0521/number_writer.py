from pathlib import Path
import json

username = input('이름')
path = Path('/works/works_python/0521/username.json') #path 알려주기,  
contents = json.dumps(username) #json.dumps에 인풋전달해서 contents에 할당,
path.write_text(contents) #이 내용을 경로에 덮어쓰기. 내용추가아님 덮어써짐!


path = Path('/works/works_python/0521/numbers.json')
#json파일이지만 텍스트이므로 read_text() 메소드로 데이터 파일을 읽어옴 
numbers = json.loads(path.read_text()) #json.loads로 이 데이터를 받아서 이 파이썬 객체를 numbers에 할당함. 제이슨화해서 할당!!!

print(numbers)

path = Path('/works/works_python/0521/username.json')
if path.exists():
     contents=path.read_text()
     username=json.loads(contents)
     print(f"읽기 {username}")
     print(contents)
else :
     username = input('이름은?')
     contents = json.dumps(username)
     path.write_text(contents)
     print(f"이름 입력됨 = {contents}")