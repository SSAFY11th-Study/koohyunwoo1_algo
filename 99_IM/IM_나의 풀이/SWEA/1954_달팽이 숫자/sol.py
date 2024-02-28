import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    cnt = 1
    x,y = 0,0  # 현재 좌표
    direction = 0

    while cnt < N*N:
        nx, ny = x + arr[]
'''
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
 
    snail = [[0]*N for _ in range(N)]
 
    dx = [0, 1, 0, -1] # 우, 하, 좌, 상
    dy = [1, 0, -1, 0]
    x, y = 0,0 # 달팽이 시작 위치
    cnt = 1
    snail[x][y] = cnt
    dir = 0
 
    while cnt < N*N:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            cnt += 1
            snail[nx][ny] = cnt
            x,y = nx, ny
        else:
            dir += 1
            if dir >= 4:
                dir = 0
 
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print()

'''


