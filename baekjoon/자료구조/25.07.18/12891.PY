# 슬라이딩 윈도우
# DNA 비밀번호
# A, C, G, T

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myadd(c): # 새로 들어온 문자를 처리하는 함수
    global checkSecret, myList, checkList

    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): # 제거되는 문자를 처리하는 함수
    global checkSecret, myList, checkList

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split()) # DNA 문자열 길이, 부분 문자열 길이
answer = 0
A = list(input()) # DNA 문자열
checkList = list(map(int, input().split())) # A, C, G, T 최소 개수 

for i in range(4):
    if checkList[i] == 0: # 값이 0이라는 것은 비밀번호 개수가 이미 만족되었다는 뜻
        checkSecret += 1

for i in range(P):
    myadd(A[i])
    if checkSecret == 4:
        answer += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        answer += 1

print(answer)