x=[int(i) for i in input().split()]
n=x[0]
k=x[1]
c=[int(I) for I in input().split()]
count=0
for i in range(0,k):
    if c[i]>=c[k-1] and c[i]>0:
        count=count+1
    if i==k-1:
        for m in range(k,n):
                if c[m]==c[k]:
                    if c[m]>=c[k-1] and c[i]>0:
                        count=count+1
print(count)
        
