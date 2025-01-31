'''def solution(s):
    return int(s)

print(solution('+1234'))
'''


4
5
6
7
8
9
10
11
12
13
14
15


def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result


print(strToInt("-1234"));
