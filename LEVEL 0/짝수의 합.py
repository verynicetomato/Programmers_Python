# LEVEL 0: 짝수의 합

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i
        else:
            continue
    return answer