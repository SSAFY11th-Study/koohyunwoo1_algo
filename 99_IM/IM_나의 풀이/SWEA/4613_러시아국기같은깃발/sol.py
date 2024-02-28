import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = N*M # 바꿔지는 횟수 저장

    cnt = 0
    for w in range(N-2):
        for i in range(M):
            if arr[w][i] != 'W':
                cnt += 1
        if result <= cnt:
            break

        cnt2 = 0
        for b in range(w+1, N-1):
            for i in range(M):
                if arr[b][i] != 'B':
                    cnt2 += 1
            if result <= cnt + cnt2:
                break

            cnt3 = 0
            for r in range(b+1, N):
                for i in range(M):
                    if arr[r][i] != 'R':
                        cnt3 += 1

            if result > cnt + cnt2 + cnt3:
                result = cnt + cnt2 + cnt3

    print(f'#{tc} {result}')


