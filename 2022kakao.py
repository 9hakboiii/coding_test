def solution(survey, choices):
    answer = ''
    mbti_dic = {
        'A': 0,
        'N': 0,
        'J': 0,
        'M': 0,
        'C': 0,
        'F': 0,
        'R': 0,
        'T': 0
    }

    cho_num_dic = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }

    for i in range(len(choices)):
        if choices[i] <= 3:
            mbti_dic[survey[i][0]] += cho_num_dic[choices[i]]
        elif choices[i] > 4:
            mbti_dic[survey[i][1]] += cho_num_dic[choices[i]]

    # 각 쌍에서 높은 값을 가진 알파벳을 선택
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for pair in pairs:
        if mbti_dic[pair[0]] > mbti_dic[pair[1]]:
            answer += pair[0]
        elif mbti_dic[pair[0]] < mbti_dic[pair[1]]:
            answer += pair[1]
        else:  
            answer += min(pair)

    return answer

print(solution(["TR", "RT", "TR"], [7, 1, 3]))
