import sys
input = sys.stdin.readline

def algorithm():
    count = 0                           # 최소 콘센트 뽑는 횟수
    multitab = []                       # 멀티탭
    for i in range(K):                  # 사용해야하는 전자기기만큼 반복
        max_idx = temp = 0              # 임시 변수들 초기화
        if name[i] in multitab:         # 지금 사용해야하는 전자기기가 멀티탭에 이미 꽂혀있는 경우
            pass                        # 아무것도 뺄 필요가 없으므로 넘어감
        elif len(multitab) < N:         # 멀티탭에 빈 자리가 있는 경우
            multitab.append(name[i])    # 해당 자리에 꽂음
        else:                           # 멀티탭에 빈 자리가 없어 하나를 뽑아야하는 경우
            for idx in range(N):                                # 멀티탭에 꽂혀있는 전자기기를 전부 검사 
                if multitab[idx] not in name[i:]:               # 앞으로 사용할 일이 없는 전자기기일 경우
                    temp = idx                                  # 뽑아버림
                    break  
                elif name[i:].index(multitab[idx]) > max_idx:   # 가장 나중에 사용해야하는 전자기기를 찾음
                    max_idx = name[i:].index(multitab[idx])     
                    temp = idx                                  
            multitab[temp] = name[i]                            # 뽑은 곳에 지금 써야하는 전자기기를 꽂음
            count += 1                                          # 뽑은 횟수 증가시켜줌
    return count                        # 최종 결과 반환


if __name__ == "__main__":
    N, K = map(int, input().split())
    name = list(map(int, input().strip().split()))
    print(algorithm())
