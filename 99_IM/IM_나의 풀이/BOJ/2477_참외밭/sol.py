import sys
sys.stdin = open('input.txt')

K = int(input())

for tc in range(K):
    direction, leng = map(int, input().split())
    print(leng)

