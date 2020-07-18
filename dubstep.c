a=str(input())
for i in range(len(a)):
    if a[i]=='W' and a[i+1]=='U' and a[i+2]=='B':
        i=i+2
        print(" ")
    else:
        print(a[i])
