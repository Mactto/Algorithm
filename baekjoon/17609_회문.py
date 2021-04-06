import sys
input = sys.stdin.readline

def check(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def algorithm(word):
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = check(word, left+1, right)
            check2 = check(word, left, right-1)
            if (check1 or check2):
                return 1
            else:
                return 2
    return 0
        

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        word = input().strip()
        print(algorithm(word))