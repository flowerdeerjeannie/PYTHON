# 파일 생성 및 쓰기
import os
print(os.getcwd())
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

print("File created and written successfully.")

# 파일에 내용 추가하기
with open('example.txt', 'a') as file:
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

print("Content appended to the file successfully.")

# 새로운 파일 생성하기
try:
    with open('new_file.txt', 'x') as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")