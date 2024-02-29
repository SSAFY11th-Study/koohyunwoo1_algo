import sys
sys.stdin = open('input.txt')
'''
빈 용기에 해당하는 원소는 0으로 저장 
물질이 들어있으면 종류에 따라 1~9로 저장

사각형 내부에는 0 이 없음

각 사각형들은 차원이 다르다

2개의 화학물질들로 이루어진 사각형들 사이에는 빈 용기들이 있다.
'''


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

