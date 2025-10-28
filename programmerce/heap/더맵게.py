import heapq

def solution(scoville, k):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        if len(scoville) == 1:
            return -1
        else:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            cnt += 1

    return cnt