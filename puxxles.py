a=[int(i) for i in input().split()]
n=a[0]
m=a[1]
b=[int(x) for x in input().split()]
b.sort()
print(b[0])
print(b[n-1])
ans=b[n-1]-b[0]
print(ans)
