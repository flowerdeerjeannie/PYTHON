import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('seaborn-v0_8-whitegrid')
#입력
x_values= range(1,1001)
#출력
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()

# ax.plot(x_values, y_values, linewidth=3)
ax.scatter(x_values, y_values, s=10)
ax.axis([0, 1100, 0, 1_100_000])
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#포인트 주기(위치,점의크기)->이렇게 하면 x,y값마다 포인터가됨

#두 축의 눈금 스타일 지정
ax.tick_params(labelsize=14)

plt.show()