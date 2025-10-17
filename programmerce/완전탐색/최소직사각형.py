def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        a, b = max(w, h), min(w, h)
        if a > max_w: max_w = a
        if b > max_h: max_h = b
    return max_w * max_h


size = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(size))