n=int(input())
x=0
y=0
z=0
a=[]
m=0
for i in range(0,n):
    a.append(0)
for i in range(0,n):
    a[i]=[int(m) for m in input().split()]
for i in range(0,n):
    x=x+a[i][0]
    y=y+a[i][1]
    z=z+a[i][2]
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
