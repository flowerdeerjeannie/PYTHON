from random import choice

class RandomWalk:
     def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols for _ in range(rows)]  # 초기 보드 생성
        self.x_values = [0]
        self.y_values = [0]

     def fill_walk(self, num_points=5000, x_start=0, y_start=0):
        x = x_start
        y = y_start

        for _ in range(num_points):
            # 랜덤한 방향으로 이동합니다.
            x_step = choice([1, 0, -1])
            y_step = choice([1, 0, -1])

            # 새로운 위치를 계산합니다.
            x_new = x + x_step
            y_new = y + y_step

            # 경계를 벗어나는지 확인하고 벗어난 경우 무시합니다.
            if x_new < 0 or x_new >= self.rows or y_new < 0 or y_new >= self.cols:
                continue

            # 새로운 위치로 이동합니다.
            x = x_new
            y = y_new

            # 보드에 방문한 흔적을 남깁니다.
            self.board[x][y] += 1

            # 새로운 좌표를 리스트에 추가합니다.
            self.x_values.append(x)
            self.y_values.append(y)

        return self.x_values, self.y_values
