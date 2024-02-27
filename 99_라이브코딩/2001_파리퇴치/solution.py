import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int ,input().split())) for _ in range(N)]

    max_cnt = 0
    # 가장 많은 파리를 죽일떄의 수를 여기다가 저장한다다    
    for i in range(N-M+1):
        # 파리채의 범위가 주어진 배열을 벗어나지 않도록 하기위함
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += arr[i+k][j+l]
                    # 파리채 내의 각 위치에 해당하는 배열의 값
                    # 을 cnt에 저장해줌

            # 최댓값 찾고
            if max_cnt < cnt:
                max_cnt = cnt


    print(f'#{tc} {max_cnt}')
    # 출력력