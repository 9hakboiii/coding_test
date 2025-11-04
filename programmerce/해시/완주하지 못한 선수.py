from collections import Counter

def solution(participant, completion):
    counter = Counter(participant) - Counter(completion)
    return list(counter.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))  # leo