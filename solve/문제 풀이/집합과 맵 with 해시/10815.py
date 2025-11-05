import sys
input = sys.stdin.readline

n = int(input())
my_card = set(map(int, input().split()))

deck = int(input())
target_card = list(map(int, input().split()))

ans = []
for card in target_card:
    if card in my_card:
        ans.append('1')
    else:
        ans.append('0')

sys.stdout.write(' '.join(ans))