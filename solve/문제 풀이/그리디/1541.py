# 잃어버린 괄호
import sys
n = sys.stdin.readline().rstrip()
a, *b = [sum(map(int, i.split('+'))) for i in n.split('-')]
print(a-sum(b))