import math
a=[int(i) for i in input().split()]
#print(a)
n=a[0]
k=a[1]
if k<=math.ceil(n/2):
    print((k*2)-1)
else:
    if n%2==0:
        print(n-((n-k)*2))
    else:
        print((n-((n-k)*2))-1)
    
    
