a=str(input())
n=len(a)
b=[]
s=''
for i in range(0,n,2):
    new=a[i]
    b.append(new)
b.sort()
x=len(b)
for i in range(0,x):
    s=s+b[i]
    
    if i<x-1:
        s=s+'+'
print(s)
        
        
    
