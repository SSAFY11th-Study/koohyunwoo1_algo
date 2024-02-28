import sys
sys.stdin = open('input.txt')


N = int(input())  # 기둥의 개수

lst = [0] * 1001

mx = 0
mx_idx = 0
for _ in range(N):
    L, H = map(int, input().split())
    lst[L] = H
    pass


