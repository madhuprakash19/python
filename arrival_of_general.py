n=int(input())
a=[int(i) for i in input().split()]
res = a[::-1]
m=res.index(min(res))
mi=n-m-1
ma=a.index(max(a))
#print(mi)
#print(ma)
ans=0
if ma-mi>0:
    ans=(n-mi+ma-2)
else:
    ans=(n-mi+ma-1)
print(ans)
    
