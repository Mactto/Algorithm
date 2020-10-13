---
layout: post
title: "JadenCase 문자열 만들기"
subtitle: Algorithm
categories: algorithm
comments: true
---

# JadenCase 문자열 만들기

---

[프로그래머스 코딩테스트 JadenCase 문자열 만들기 문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12951)

```python
def solution(s):
    answer = ''
    for i in s.split(" "):
        answer += i.lower().capitalize() + ' '
    return answer[:-1]

if __name__ == "__main__":
    s = input()
    print(solution(s))
```
