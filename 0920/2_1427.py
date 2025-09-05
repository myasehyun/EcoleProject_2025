import sys
number=sys.stdin.readline().strip()

number_list=sorted(number,reverse=True)
result="".join(number_list)
print(result)
