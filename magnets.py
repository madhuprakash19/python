n=int(input())
prev=int(input())
temp=0
group=1
for i in range(0,n-1):
    temp=int(input())
    if(temp!=prev):
        group=group+1
        prev=temp

print(group)
