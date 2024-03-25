import sys

# 표준 입력을 'input.txt' 파일에서 읽도록 재지정
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 읽음
T = int(input())

# 16진수 문자를 해당하는 10진수 값으로 매핑하는 사전
c = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# 각 테스트 케이스에 대해 반복
for tc in range(1, T + 1):
    # 입력을 읽음: N은 이진 표현의 길이이고 number는 16진수 숫자임
    N, number = input().split()

    result = ''  # 이진 표현을 저장할 빈 문자열 초기화
    # 16진수 숫자를 뒤집고 각 문자에 대해 반복
    for n in number[::-1]:
        # 사전에 있는 16진수 문자를 해당하는 10진수 값으로 변환
        if n in c:
            n = c[n]
        n = int(n)  # 문자를 정수로 변환

        # 각 16진수 숫자를 4비트 이진 표현으로 변환
        for _ in range(4):
            result = str(n % 2) + result # 최하위 비트를 결과에 추가
            n //= 2  # 1비트 오른쪽으로 시프트하여 16진수 숫자를 업데이트

    # 결과를 해당하는 테스트 케이스 번호와 함께 출력
    print(f'#{tc} {result}')
