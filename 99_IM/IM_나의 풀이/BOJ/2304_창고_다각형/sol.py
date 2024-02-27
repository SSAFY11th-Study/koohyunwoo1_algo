import sys
sys.stdin = open('input.txt')
'''

'''
lst = []
N = int(input())
for tc in range(N):
    L, H = map(int, input().split())
    lst.append([H, L])


lst.sort()
print(lst)