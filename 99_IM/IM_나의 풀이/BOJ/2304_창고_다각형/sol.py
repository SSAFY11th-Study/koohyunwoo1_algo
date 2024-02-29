import sys
sys.stdin = open('input.txt')

lst = []
N = int(input())  # 기둥의 개수
for tc in range(N):
    idx, height = map(int, input().split())
    lst.append([idx, height])
    lst.sort()






