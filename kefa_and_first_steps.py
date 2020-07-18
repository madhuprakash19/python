n=int(input())
a=[int(i) for i in input().split()]
a.append(0)
#print(a)
c=[]
for i in range(0,n):
    temp=1
    c.append(temp)
#print(c)
m=1
for i in range(0,n):
    
    if a[i]<=a[i+1]:
        m=m+1
    else:
        c[i]=m
        m=1
print(max(c))
