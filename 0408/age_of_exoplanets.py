def solution(age):
    answer = ''
    age_d = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}

    while age > 0:
        n = age % 10
        answer += age_d[n]
        age //= 10

    return answer[::-1]