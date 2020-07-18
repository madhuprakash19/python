m=[int(i) for i in input().split()]
x=m[0]
y=m[1]
z=m[2]
t1=m[3]
t2=m[4]
t3=m[5]
stair=abs((x-y)*t1)
elevator=(abs((x-z)*t2)+abs((x-y)*t2)+3*t3)
#print(stair)
#print(elevator)
if elevator<=stair:
    print("YES")
else:
    print("NO")
