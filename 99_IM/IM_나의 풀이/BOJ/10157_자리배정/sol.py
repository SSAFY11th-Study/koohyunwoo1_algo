import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
K = int(input())

if K > R * C:
    print(0)
    exit()

# arr = [[0]*C for _ in range(R)]
#
# di = [1,0,-1,0]
# dj = [0,1,0,-1]
#
# dire = x = y = 0
# for i in range(1, C*R +1):
#     for j in range(1, C*R+1):
#         if K == i:
#             print(x+1, y+1)
#             break
#         else:




