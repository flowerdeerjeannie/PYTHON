from pathlib import Path
import os


print(f"현재경로 {os.getcwd()}")

# 파일 경로 설정
path = Path('/works/works_python/0521/programming.txt')

try:
    # 파일 열기
    with path.open(mode='a') as file:
        # 파일에 내용 추가
        file.write("writing by path")
    print("파일에 내용이 성공적으로 추가되었습니다.")
except Exception as e:
    # 예외 처리
    print(f"파일 작성 중 오류 발생: {e}")

