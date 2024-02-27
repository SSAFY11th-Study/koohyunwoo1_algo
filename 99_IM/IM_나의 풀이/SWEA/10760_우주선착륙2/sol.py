import sys
sys.stdin = open('input.txt')

'''
착륙할때 예비 후보지가 4곳 이상인 곳을 찾아보자
'''

direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            lst = arr[i][j]
            cnt = 0
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] < lst:
                        cnt += 1
                if cnt >= 4:
                    result += 1
                    break

    print(f'#{tc} {result}')

