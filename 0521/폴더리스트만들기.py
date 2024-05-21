import os

# 폴더 확인 함수
def check_folders(base_path, folder_prefix, start, end):
    for i in range(start, end + 1):
        folder_path = os.path.join(base_path, f"{folder_prefix}{i}")
        if os.path.exists(folder_path):
            print(f"{folder_path} exists.")
        else:
            print(f"{folder_path} does not exist.")

# 기본 경로 및 폴더 접두사 정의
base_path = "/works/works_python/0521"
folder_prefix = "GoodFolder"

# # 폴더 생성 코드 (기존 코드와 동일)
os.makedirs(base_path, exist_ok=True)
os.mkdir(os.path.join(base_path, "GoodFolder1"))
os.mkdir(os.path.join(base_path, "GoodFolder2"))
os.mkdir(os.path.join(base_path, "GoodFolder3"))
os.mkdir(os.path.join(base_path, "visiting"))


# # 3까지는 노가다 하고 4부터 9까지는 while문 돌린거임 
num = 4
while num < 10:
    os.mkdir(os.path.join(base_path, f"{folder_prefix}{num}"))
    num += 1

# 생성된 폴더 확인
check_folders(base_path, folder_prefix, 1, 9)

# 파일생성 경로 설정
file_path = os.path.join(base_path, "visiting.txt")

try:
    with open(file_path, 'w') as file:
        file.write("guest1 \nguest2 \nguest3")
        print("파일 생성 성공!")
except OSError as e:
    print(f"오류발생 {e}")