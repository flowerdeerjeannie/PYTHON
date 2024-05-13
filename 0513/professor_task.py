import random

random_numbers =[random.randint(1,100) for _ in range(20)]
print(f"난수 생성 = {random_numbers}")

string_list = []

for i in range(1, 21):
   s_number=f"s{i}"
   string_list.append(s_number)

# 저장된 리스트 출력
print(f"sno 리스트 = {string_list}")

students = string_list
scores = random_numbers

score_dic = dict(zip(students,scores))
print(f"학번:점수 딕셔너리={score_dic}")

#items로 키:쌍을 집어서 묶어서 정렬하고, 정렬한 것은 딕셔너리가 아닌 리스트 상태이므로,  다시 dict로 묶어줘야함
#sorted함수의 매개변수에 key에 람다 넣어서 값 기준 정렬하도록 함.
sorted_score_dic=dict(sorted(score_dic.items(), key=lambda item:item[1]))

print(f"점수로 정렬된 딕셔너리= {sorted_score_dic}")
# 정렬된 튜플 리스트에서 상위 5개 추출하여 리스트로 저장
# 상위 5개 추출하여 딕셔너리로 저장
toplist = list(sorted_score_dic.values())
top_5=toplist[-5:]
print(f"상위 5개= {top_5}")

# 딕셔너리의 키-값 쌍을 튜플로 묶어 리스트에 추가
score_list = []
for i in sorted_score_dic.items():
   score_list.append(i)

# 결과 출력
print(f"리스트로 변환된 딕셔너리: {score_list}")

# 딕셔너리의 각 요소를 enumerate를 사용하여 출력(인덱스와 함께 출력)
enumerate_dic = {index: (key, value) for index,(key, value) in enumerate(sorted_score_dic.items())}

# # # 결과 출력
print(f"변환된 딕셔너리: {enumerate_dic}")