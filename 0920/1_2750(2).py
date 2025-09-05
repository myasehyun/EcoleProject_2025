import sys
input=sys.stdin.readline

n=int(input())
number=[]

for _ in range(n):
    num=int(input())
    number.append(num)

number.sort

for num in number:
    print(num)