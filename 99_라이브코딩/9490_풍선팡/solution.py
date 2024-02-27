import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 풍선에 들어있는 꽃가루의 개수
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    max_cnt = 0
    # 최대 꽃가루의 합
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            # 터트린 풍선
            for k in range(4):
                for l in range(1, arr[i][j] + 1):
                    ni = i + di[k] * l
                    # 터트린 풍선안에 들어있는 꽃가루의 개수만큼 가야되기 때문에
                    # 곱하기 l을 해줍니다
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        # 범위를 벗어나지 않는 기준에서
                        cnt += arr[ni][nj]
                        # 터트린풍선에 값에다가 게속해서 상하좌우를 더해 나간다.
            if max_cnt < cnt:
                max_cnt = cnt


    print(f'#{tc} {max_cnt}')

