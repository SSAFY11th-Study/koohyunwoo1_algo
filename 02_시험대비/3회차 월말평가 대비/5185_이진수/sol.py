import sys
sys.stdin = open('input.txt')

T = int(input())

c = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E': 14, 'F': 15}
for tc in range(1, T+1):
    N, number = map(str, input().split())
    N = int(N)

    result = ''
    for n in number[::-1]:
        if n in c:
            n = c[n]

        n = int(n)

        for _ in range(4):
            result = str(n % 2) + result
            n //= 2


    print(f'#{tc} {result}')