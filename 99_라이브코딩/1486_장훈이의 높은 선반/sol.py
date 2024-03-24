import sys
sys.stdin = open('input.txt')

def dfs(s, sm):
    global result

    # if result <= sm - B:
    #     return

    if s == N:
        if sm >= B:
            result = min(result, sm-B)
        return

    dfs(s+1, sm+height[s])
    dfs(s+1, sm)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    result = float('Inf')
    dfs(0, 0)

    print(f'#{tc} {result}')


#
# from itertools import combinations
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     height = list(map(int, input().split()))
#     result = float('Inf')
#
#     for i in range(1, N+1):
#         a = list(combinations(height, i))
#
#         for j in a:
#             if sum(j) >= B:
#                 if sum(j) - B < result:
#                     result = sum(j) - B
#
#     print(f'#{tc} {result}')