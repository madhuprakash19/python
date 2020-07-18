a=[int(i) for i in input().split()]
i=0
while a[1]>a[0] or a[1]==a[0]:
    a[0]=a[0]*3
    a[1]=a[1]*2
    i=i+1
print(i)
