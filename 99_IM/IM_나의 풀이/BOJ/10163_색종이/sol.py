import sys
sys.stdin = open('input.txt')

arr = [[0] * 1001 for _ in range(1001)]
N = int(input())

for i in range(N):
    x, y, w, h = map(int, input().split())

    for j in range(x, x+w):
        for k in range(y, y+h):
            arr[j][k] = i + 1


for i in range(N):
    cnt = 0
    for a in arr:
        cnt += a.count(i+1)

    print(cnt)






