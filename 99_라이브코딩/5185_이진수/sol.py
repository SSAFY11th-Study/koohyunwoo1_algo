import sys

sys.stdin = open('input.txt')

T = int(input())

# 10이 넘는 숫자들을 변환 ? 해주는거
c = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, T + 1):
    # N은 길이, number는 16진수 숫자임
    N, number = input().split()

    result = ''  # 최종값
    for n in number[::-1]:
        if n in c:
            # n이 변환 가능하면 변환해줌
            n = c[n]
        n = int(n)  # 변환 안에 없는 숫자면 str이기 떄문에 int로 받아준다.

        # 각 16진수 숫자를 4비트 이진 표현으로 변환
        for _ in range(4):
            result = str(n % 2) + result
            n //= 2

    print(f'#{tc} {result}')
