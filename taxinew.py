n=int(input())
m=[str(i) for i in input().split()]
a=0
b=0
c=0
d=0
total=0
z=0
x=0
rem=0
for i in range(0,n):
    if '1' in m[i]:
        a=a+1
    if '2' in m[i]:
        b=b+1
    if '3' in m[i]:
        c=c+1
    if '4' in m[i]:
        d=d+1
total+=d
total=total+b//2
b=b%2
if a<=c:
    total+=a
    total=total+b
    total=c-a
else:
    total+=c
    a=a-c
    total=total+a//4
    a=a%4
    rem=a+(2*b)
    if rem>0:
        total+=1 if rem <=4 else 2
print(total)
    
    
    
    
