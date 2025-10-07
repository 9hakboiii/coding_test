import sys

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(sys.stdin.readline())
sys.stdout.write(str(factorial(n)) + '\n')