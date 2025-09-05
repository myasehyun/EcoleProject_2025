n = int(input())
arr = []
stack = []
cnt = 1
res = []
flag = True

for _ in range(n):
    arr.append(int(input()))

for x in arr:
    while cnt <= x:
        stack.append(cnt)
        cnt += 1
        res.append("+")

    if stack[-1] == x:
        stack.pop()
        res.append("-")
    else:
        flag = False
        break

if flag:
    for i in res:
        print(i)
else:
    print("NO")