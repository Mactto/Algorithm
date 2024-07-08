from collections import deque

N, K = map(int, input().split())
container = deque(list(map(int, input().split())))

robot_positions = deque([0 for _ in range(2 * N)])
step = 0

while True:
    # 박스 올리기
    if container[0] != 0:
        container[0] -= 1
        robot_positions[0] = 1
    
    if container.count(0) >= K:
        break

    # 컨테이너 이동
    container.appendleft(container.pop())
    robot_positions.pop()
    robot_positions.appendleft(0)

    for idx in range(len(robot_positions)-2, -1, -1):
        if robot_positions[idx] == 1 and robot_positions[idx + 1] != 1 and container[idx + 1] != 0:
            robot_positions[idx] = 0
            if idx + 1 != 2 * N - 1:
                robot_positions[idx + 1] = 1
            container[idx + 1] -= 1

    step += 1

print(step)