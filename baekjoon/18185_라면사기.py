
def solution():
    N = int(input())
    A = list(map(int, input().split()))

    pay = 0

    for i in range(N - 2):
        if A[i] >= 1 and A[i+1] >= 1 and A[i+2] >= 1:
            if A[i+1] > A[i+2]:
                purchase = min(A[i], A[i+1])
                A[i] -= purchase
                A[i+1] -= purchase
                pay += 5 * purchase
            else:
                purchase = min(A[i], A[i+1], A[i+2])
                A[i] -= purchase
                A[i+1] -= purchase
                A[i+2] -= purchase
                pay += 7 * purchase
    
    for i in range(N - 1):
        if A[i] >= 1 and A[i+1] >= 1:
            purchase = min(A[i], A[i+1])
            A[i] -= purchase
            A[i+1] -= purchase
            pay += 5 * purchase

    for i in range(N):
        if A[i] >= 1:
            pay += 3 * A[i]

    return pay


print(solution())
