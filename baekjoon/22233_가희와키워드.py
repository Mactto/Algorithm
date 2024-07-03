import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keyword_dict = {}
for _ in range(N):
    keyword = input().rstrip()
    keyword_dict[keyword] = 0

keyword_count = len(keyword_dict)

use_keyword_set = set()
for _ in range(M):
    use_keyword_list = list(map(str, input().rstrip().split(',')))    
    for use_keyword in use_keyword_list:
        if use_keyword in keyword_dict:
            use_keyword_set.add(use_keyword)
    print(keyword_count - len(use_keyword_set))
