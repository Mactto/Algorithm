N = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0
for i in range(N):
    left = 0
    right = i - 1

    while left < right:
        value = A[left] + A[right]

        if value == A[i]:
            count += 1
            break
        elif value < A[i]:
            left += 1
        else:
            right -= 1

print(count)
