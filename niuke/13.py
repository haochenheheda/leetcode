a,b,c = list(map(int,raw_input().strip().split()))
print(max(a+b+c,a*b*c,a+b*c,a*b+c,(a+b)*c,a*(b+c)))