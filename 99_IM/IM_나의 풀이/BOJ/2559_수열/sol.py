import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
lst = list(map(int, input().split()))

result = []
result.append(sum(lst[:K]))

for i in range(N-K):
    result.append(result[i] - lst[i] + lst[K+i])

print(max(result))

