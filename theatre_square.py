d=[int(i) for i in input().split()]
l=d[0]
b=d[1]
a=d[2]
if (l%a)==0:
    x=int(l/a)
else:
   x=int(l/a)+1
if (b%a)==0:
    y=int(b/a)
else:
    y=int(b/a)+1
ans=x*y
print(ans)    
    
