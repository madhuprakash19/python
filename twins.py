n=int(input())
a=[int(i) for i in input().split()]
#print(a)
a.sort(reverse=True)
total=sum(a)
#print(total)
taken=0
i=0
while taken<total or taken==total:
    taken=taken+int(a[i])
    total=total-int(a[i])
    i=i+1
#print(taken)
print(i)
