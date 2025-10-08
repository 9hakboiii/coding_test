def palindrome(s, l, r):
    if l >= r: return 1, 1
    elif s[l] != s[r]: return 0, 1
    else:
        result, cnt = palindrome(s, l+1, r-1)
        return result, cnt + 1

def recursion(s):
    return palindrome(s, 0, len(s)-1)

t = int(input())
for _ in range(t):
    st = input().strip()
    result, cnt = recursion(st)
    print(result, cnt)