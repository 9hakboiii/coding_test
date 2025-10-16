import sys
#
# month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# st = 5
#
# a, b = map(int, sys.stdin.readline().split())
# ans = sum(month[:a-1]) + (b-1)
# print(days[(st + ans) % 7])


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt, zero = 0, 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            zero += 1

    ans = [rank[cnt+zero], rank[cnt]]
    return ans

lotto_num = [45, 4, 35, 20, 3, 9]
win_num = [20, 9, 3, 45, 4, 35]
print(solution(lotto_num, win_num))