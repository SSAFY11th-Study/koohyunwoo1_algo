import sys
sys.stdin = open('input.txt')
'''
푸른 자성체의 경우 N극에 이끌리는 성질 
붉은 자성체의 경우 S극에 이끌리는 성질

1은 N극 성질을 가짐
2는 S극 성질을 가짐

열을 탐색하면서 1-2 순서를 가지면 cnt += 1 ?
'''
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for  j in range(N):

        i = 0
        stack = []

        while i < N:
            if not stack and arr[i][j] == 1:
                stack.append(1)
            elif stack and arr[i][j] == 2:
                stack.pop()
                cnt += 1

            i += 1

    print(f'#{tc} {cnt}')





