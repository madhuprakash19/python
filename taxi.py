n=int(input())
m=[str(i) for i in input().split()]
a=0
b=0
c=0
d=0
total=0
z=0
x=0
for i in range(0,n):
    if '1' in m[i]:
        a=a+1
    if '2' in m[i]:
        b=b+1
    if '3' in m[i]:
        c=c+1
    if '4' in m[i]:
        d=d+1
#print(a)
#print(b)
#print(c)
#print(d)
#total=total+d
if c>=a:
    a=0
if c<a:
    a=a-c
#total=total+c
if a%2!=0:
    z=1
    a=a-1
    a=a/2
if a%2==0:
    a=a/2
x=a+b
if x%2!=0:
    x=x-1
    x=x/2
    z=1
if x%2==0:
    x=x/2
total=x+z+c+d
print(int(total))
    
