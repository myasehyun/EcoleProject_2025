import sys
input = sys.stdin.readline

n = int(input())
m = sorted(list(map(int, input().split())))
result = []
result.append(m[0])

for i in range(1, n):
    result.append(m[i] + result[i-1])

print(sum(result))