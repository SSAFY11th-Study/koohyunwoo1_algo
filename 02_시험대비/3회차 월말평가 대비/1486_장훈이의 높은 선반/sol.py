import sys

# 표준 입력을 'input.txt' 파일에서 읽도록 재지정
sys.stdin = open('input.txt')

# 깊이 우선 탐색 (DFS) 함수 정의
def dfs(s, sm):
    global ans

    # 현재까지의 높이 합이 목표 높이 b에서 뺀 값보다 이미 크다면 탐색 종료
    if ans <= sm - b:
        return

    # 모든 블록을 선택한 경우
    if s == n:
        # 현재 높이 합이 목표 높이 b보다 크거나 같다면 최솟값 갱신
        if sm >= b:
            ans = min(ans, sm - b)
        return

    # 현재 블록을 선택하는 경우와 선택하지 않는 경우로 나누어 재귀적으로 탐색
    dfs(s + 1, sm + heights[s])  # 현재 블록을 선택한 경우
    dfs(s + 1, sm)  # 현재 블록을 선택하지 않은 경우


t = int(input())  # 테스트 케이스의 수 입력

# 각 테스트 케이스에 대해 반복
for tc in range(1, t + 1):
    n, b = map(int, input().split())  # 블록의 수 n과 목표 높이 b 입력
    heights = list(map(int, input().split()))  # 각 블록의 높이 입력

    ans = n * 10000  # 초기화: 답을 최대로 설정

    dfs(0, 0)  # DFS 탐색 수행

# 각 테스트 케이스의 결과 출력
print(f'#{tc} {ans}')
