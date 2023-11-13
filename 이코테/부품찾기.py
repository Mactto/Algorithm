import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
check_numbers = list(map(int, input().split()))

def binary_search(array, target, start, end):
    print(target, start, end)
    if start > end:
        return None

    mid = (start + end) // 2
    print(array[mid])
    if array[mid] == target:
        return 'yes'
    elif target < array[mid]:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] == target:
#             return 'yes'
#         elif target < array[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 'no'

numbers = sorted(numbers)
for check_number in check_numbers:
    print(binary_search(numbers, check_number, 0, N - 1), end=" ")