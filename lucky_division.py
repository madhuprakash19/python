lucky=input()
flag=1
a=len(lucky)
#print(a)
for i in range(a):
    if lucky[i]!='4':
        if lucky[i]!='7':
            flag=0
    if lucky[i]!='7':
        if lucky[i]!='4':
            flag=0
#print(flag)
if flag==0:
    if int(lucky)%4==0:
        flag=1
    if int(lucky)%7==0:
        flag=1
    if int(lucky)%47==0:
        flag=1
    if int(lucky)%74==0:
        flag=1
    if int(lucky)%477==0:
        flag=1
#print(flag)
if flag==1:
    print('YES')
else:
    print('NO')
