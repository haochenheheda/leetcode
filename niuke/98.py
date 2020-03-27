import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n = int(lines[0].strip())
lst = [int(i.strip()) for i in lines[1:-1]]
m = int(lines[-1].strip())

print(n,m,lst)