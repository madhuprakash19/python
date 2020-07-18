n=int(input())
p=[int(i) for i in input().split()]
#print(p)
sum=0
for i in range(n):
    sum+=p[i]
ans=float(sum/n)
print(ans)
