import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree_height = list(map(int, input().split()))

def available_get_tree_height(tree_heights, height):
    result = 0
    for tree in tree_heights:
        if tree > height:
            result += (tree - height)
    return result


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        get_tree_height = available_get_tree_height(array, mid)

        if get_tree_height >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

tree_height.sort()
print(binary_search(tree_height, M, tree_height[0], tree_height[N-1]))