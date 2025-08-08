def solution(arr):
    from collections import deque
    qe = deque()

    for i in arr:
        qe.append(i)

    ans = []
    ans.append(qe.pop())
    while len(qe) > 0:
        if qe[-1] == ans[-1]:
            qe.pop()
        else:
            ans.append(qe.pop())

    ans.reverse()
    return ans


print(solution([1, 1, 3, 3, 0, 1, 1]))