import sys
sys.stdin = open('input.txt')

'''
아래에 있는 주사위의 윗면은 위에 있는 주사위의 아랫면과 같아야 한다.

'''
N= int(input())

for tc in range(1, N+1):
    dice = list(map(int, input().split()))
