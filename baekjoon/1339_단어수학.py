'''
1. 알파벳의 자릿수를 가중치로 사용해 딕셔너리에 저장
2. 딕셔너리를 리스트로 변환 후 역순 정렬
3. 정렬된 수를 가지고 9를 곱하여 결과 계산
'''
import sys
input = sys.stdin.readline

def algorithm():
    global words, weight
    for word in words:                  
        length = len(word) - 1                      # 단어의 길이를 이용
        for idx, w in enumerate(word):              # 각 단어의 인덱스 번호를 이용
            if w in weight:                         # 딕셔너리에 해당 문자가 있을 경우
                weight[w] += pow(10, length -idx)   # pow는 제곱 -> 문자 길이와 해당 단어 인덱스를 이용하여 자릿수를 구함
            else:                                   # 딕셔너리에 해당 문자가 없을 경우
                weight[w] = pow(10, length - idx)  

    array = list(weight.values())                   # 딕셔너리의 value 값을 리스트로 변환
    array.sort(reverse=True)                        # 역순 정렬
    result, mul = 0, 9                              # 자릿수에 차례대로 9부터 곱함
    for a in array:                         
        result += a * mul                           # 결과에 더함
        mul -= 1                                    # 곱하는 수는 1씩 감소
    return result                                   # 결과 반환

if __name__ == "__main__":
    weight = {}
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(algorithm())