import sys
input = sys.stdin.readline
n, m = map(int, input().split())
number = list(map(int, input().split()))

prepix_sum=[0] #누적합 저장 리스트(맨앞에 0넣음)
tmp=0

for num in number:
    tmp=tmp+num #0+5
    prepix_sum.append(tmp)
    #prepix_sum=[0,5]
    
for _ in range(m):
    i,j=map(int, input().split())
    print(prepix_sum[j]-prepix_sum[i-1])
