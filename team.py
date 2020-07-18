n=int(input())
check=0
count=0
for i in range(0,n):
    a=[int(m) for m in input().split()]
    check=a[0]+a[1]+a[2]
    if check>1:
        count=count+1
    a=[0,0,0]
print(count)
