a=[int(i) for i in input().split()]
intialcost=a[0]
money=a[1]
banana=a[2]
n=int(banana)+1
total=0
final=0
for i in range(n):
    total=total+i*int(intialcost)
if total<=money:
    final=0
else:
    final=total-int(money)
print(final)
