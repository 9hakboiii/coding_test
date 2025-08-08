def solution(progresses, speeds):
    from collections import deque

    qe = deque()
    for p in progresses:
        qe.append(p)

    time = []
    for i in range(len(qe)):
        progress = qe[i]
        speed = speeds[i]
        days = 0

        while progress < 100:
            progress += speed
            days += 1

        time.append(days)

    ans = []
    current_day = time[0]
    count = 1

    for i in range(1, len(time)):
        if time[i] <= current_day:
            count += 1
        else:
            ans.append(count)
            current_day = time[i]
            count = 1

    ans.append(count)
    return ans

print(solution([93, 30, 55], [1, 30, 5]))
         