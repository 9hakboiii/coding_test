import sys
input = sys.stdin.readline

n = int(input())
my_card = set(map(int, input().split()))

m = int(input())
target_card = list(map(int, input().split()))

ans = ['1' if card in my_card else '0' for card in target_card]
sys.stdout.write(' '.join(ans))