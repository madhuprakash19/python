a=[int(i) for i in input().split()]
#print(a)
n=a[0]
k=a[1]
b=[]
for i in range(1,n+1):
    if i%2!=0:
        b.append(i)
for i in range(1,n+1):
    if i%2==0:
        b.append(i)
print(b[k-1])
        
