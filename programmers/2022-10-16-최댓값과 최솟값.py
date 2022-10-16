
def solution(s):
    s = s.split()
    s.sort(key=lambda x: int(x))
    return str(s[0]) + " " + str(s[len(s)-1])