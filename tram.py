n=int(input())
x=[]
a=[]
b=[]
c=[]
m=0
for i in range(0,n):
    x.append(0)
    a.append(0)
    b.append(0)
    c.append(0)
for i in range(0,n):
    x[i]=[int(m) for m in input().split()]
    a[i]=x[i][0]
    b[i]=x[i][1]
c[0]=b[0]
for i in range(1,n):
    c[i]=c[i-1]-a[i]+b[i]
print(max(c))
