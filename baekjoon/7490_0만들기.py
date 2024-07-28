T = int(input())

for _ in range(T):
    N = int(input())
    answer = []

    def dfs(ex: str, count: int):
        if count == N:
            expression = ex.replace(" ", "")
            if eval(expression) == 0:
                answer.append(ex)
            return
        count += 1
        dfs(f"{ex}+{str(count)}", count)
        dfs(f"{ex}-{str(count)}", count)
        dfs(f"{ex} {str(count)}", count)

    dfs(f"{1}", 1)

    answer.sort()
    for a in answer:
        print(a)
    print()
