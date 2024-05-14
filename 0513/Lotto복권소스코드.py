
#아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.

import random

# 두 세트 생성-로또용X intersection 의미 위하여.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 2, 1, 6, 7}

# 두 세트가 동일한지 확인 (모든 요소가 같은지. 배열 순서 말고 세트 안에 내용이 같은지를 봐줌 == 로)
print("set1과 set2가 동일한지:", set1 == set2)
print(len(set1.intersection(set2)) == 3)



# 로또 복권 번호 생성 함수
# 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음) 마지막에 set으로 묶어줘야 중복제거된값
# 무작위로 숫자 1개 선택하여 보너스 번호 생성
def generate_lotto_numbers():
    numbers = list(range(1, 46))
    lotto_numbers = set(random.sample(numbers, 6))
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number

winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

# 랜덤번호를 가진 100장의 로또를 생성하는 과정

lotto_list=[]
for _ in range(1, 101):
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    lotto_list.append((lotto_numbers, lotto_bonus_number))
    #튜플형태로 로또리스트에 저장함

#print(f"{idx}:{number},{bonus}")
def check_winner(lotto_numbers, lotto_bonus_number, winning_numbers, winning_bonus_number, idx):
    if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 1등 당첨!")
    elif lotto_numbers == winning_numbers:
        print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
    elif lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 5:
        print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 4:
        print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
    else:
        print(f"{idx}번째 로또 복권: 꽝")


for idx, (numbers, bonus) in enumerate(lotto_list, 1):
    check_winner(numbers, bonus, winning_numbers, winning_bonus_number, idx)
