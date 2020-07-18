n=int(input())
sum=0
flag=0
for i in range(n):
    sum=0
    a=int(input())
    x=[int(k) for k in input().split()]
    for c in range(a-1):
        flag=0
        for q in range(a-c):
                if x[c]>x[q]:
                        flag=1
                        break
        if flag==1:
            sum=sum+1
    print(sum)
        
        
