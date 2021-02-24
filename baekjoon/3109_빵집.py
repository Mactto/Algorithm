import sys
input = sys.stdin.readline

def dfs(i, j):              # 깊이 우선 탐색
    global state, result    
    if i == -1 or i == R:   # 행이 범위 밖을 가리키고 있는 경우
        return              # 빠져나감
    if road[i][j] == 'x':   # 현재 위치에 건물이 있거나 이미 파이프가 설치된 경우
        return              # 빠져나감
    
    road[i][j] = 'x'        # 파이프 설치
    if j == C-1:            # 원웅이 빵집까지 도달한 경어
        state = True        # 파이프가 설치됐음을 표시
        result += 1         # 결과 + 1
        return              # 깊이우선 빠져나감
    for idx in range(3):        # 오른쪽위, 오른쪽, 오른쪽아래 방향으로 다시 탐색
        dfs(i+dx[idx], j+1)   
        if state:               # 만약에 이미 파이프가 설치된 경우 빠져나감
            return

if __name__ == "__main__":
    R, C = map(int, input().split())
    road = [list(input().strip()) for _ in range(R)]
    result = 0
    dx = [-1, 0, 1]
    for i in range(R):
        state = False
        dfs(i, 0)
    print(result)