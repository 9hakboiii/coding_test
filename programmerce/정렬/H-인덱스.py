def solution(citations):
    citations.sort(reverse=True)
    h = 0

    for i, n in enumerate(citations):
        if n >= i + 1:
            h = i + 1
        else:
            break

    return h

if __name__ == '__main__':
    print(solution([3, 0, 3, 6, 1, 5]))