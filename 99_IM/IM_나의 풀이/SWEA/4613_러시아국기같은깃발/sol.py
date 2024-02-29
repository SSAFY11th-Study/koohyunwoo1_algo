import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    total = N * M
    cnt1 = 0
    result = []

    for w in range(N-2):
        for j in range(M):
            if arr[w][j] == 'W':
                cnt1 += 1

        cnt2 = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if arr[b][j] == 'B':
                    cnt2 += 1

            cnt3 = 0
            for r in range(b+1, N):
                for j in range(M):
                    if arr[r][j] == 'R':
                        cnt3 += 1

            cnt = cnt1 + cnt2 + cnt3
            result.append(total - cnt)

    print(f'#{tc} {min(result)}')


