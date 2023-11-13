import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rice_cakes = list(map(int, input().split()))

rice_cakes = sorted(rice_cakes)

def cal_rice_cake_length(rice_cakes, cut_length):
    length = 0

    for rice_cake in rice_cakes:
        cut = rice_cake - cut_length
        if cut > 0:
            length += cut
    return length


def binary_search(array, target, start, end):
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        
        rice_cake_length = cal_rice_cake_length(array, mid)

        if rice_cake_length == target:
            return rice_cake_length
        elif rice_cake_length < target:
            end = mid - 1
        else:
            start = mid + 1
    return mid

print(binary_search(rice_cakes, M, rice_cakes[0], rice_cakes[-1]))
