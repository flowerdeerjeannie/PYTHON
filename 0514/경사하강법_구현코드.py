# 주어진 함수 정의
def func(x):
    return 5 * x ** 2 + 5 * x + 7

# 도함수(미분) 계산
def derivative(x):
    return 10 * x + 5

# 경사 하강법을 사용하여 기울기가 0인 지점 찾기
def gradient_descent(learning_rate, initial_x, epochs):
    x = initial_x
    for _ in range(epochs):
        gradient = derivative(x)
        x = x - learning_rate * gradient
    return x

# 학습률, 초기값, 반복 횟수 설정
learning_rate = 0.01
initial_x = 0.0
epochs = 1000

# 경사 하강법 적용하여 기울기가 0인 지점 찾기
optimal_x = gradient_descent(learning_rate, initial_x, epochs)
optimal_y = func(optimal_x)

# 결과 출력
print("기울기가 0인 x:", optimal_x)
print("해당 지점에서의 y 값:", optimal_y)