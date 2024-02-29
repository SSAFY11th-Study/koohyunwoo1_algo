import sys
sys.stdin = open('input.txt')
'''
가장 큰 종이 조각의 넓이를 출력

'''
x, y = map(int, input().split())
N = int(input())

width = [0, y]  # 가로
height = [0, x]  # 세로

for tc in range(N):
    a, b = map(int, input().split())

    if a == 0:
        width.append(b)
    else:
        height.append(b)

width.sort()
height.sort()

result1 = []
for i in range(len(width)):
    if 0 <= i+1 < len(width):
        c = width[i+1] - width[i]
        result1.append(c)
e = max(result1)

result2 = []
for j in range(len(height)):
    if 0 <= j+1 < len(height):
        d = height[j+1] - height[j]
        result2.append(d)
f = max(result2)

print(e*f)


