# 버블 소트

def merge_sort(A, tmp, s, e):
    if e - s <= 1: return 0

    m = (s + e) // 2
    inv = 0

    # 좌우 절반 정렬 & 역전 개수 합산
    inv += merge_sort(A, tmp, s, m)
    inv += merge_sort(A, tmp, m, e)

    # 병합 전 원본 복사
    for i in range(s, e):
        tmp[i] = A[i]

    i, j, k = s, m, s
    # 병합하며 역전 쌍 세기
    while i < m and j < e:
        if tmp[i] <= tmp[j]:
            A[k] = tmp[i]
            i += 1
        else:
            A[k] = tmp[j]
            j += 1
            inv += (m - i) 
        k += 1

    # 남은 절반 옮기기
    while i < m:
        A[k] = tmp[i]
        i += 1
        k += 1

    while j < e:
        A[k] = tmp[j]
        j += 1
        k += 1

    return inv

# 입력 및 실행
N = int(input())
A = list(map(int, input().split()))
tmp = [0] * N

result = merge_sort(A, tmp, 0, N)
print(result)