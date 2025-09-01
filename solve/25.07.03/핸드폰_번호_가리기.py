def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

print(solution("0233334444"))