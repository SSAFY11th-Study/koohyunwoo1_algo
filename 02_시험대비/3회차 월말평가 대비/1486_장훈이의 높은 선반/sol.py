import sys
sys.stdin = open('input.txt')

def dfs(s, sm):
    global ans

    if ans <= sm - b:
        return

    if s == n:
        if sm >= b:
            ans = min(ans, sm - b)
        return

    dfs(s + 1, sm + heights[s])
    dfs(s + 1, sm)


t = int(input())

for tc in range(1, t + 1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))

    ans = n * 10000

    dfs(0, 0)

print(f'#{tc} {ans}')