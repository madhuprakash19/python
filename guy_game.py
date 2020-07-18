n=int(input())
a=[int(i) for i in input().split()]
a.pop(0)
b=[int(j) for j in input().split()]
b.pop(0)
c=a+b
#print(c)
flag=0
for i in range(1,n+1):
    flag=0
    for m in range(0,len(c)):
        if c[m]==i:
            flag=1
    if flag==0:
        break
if flag==1:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
    
