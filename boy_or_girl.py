name=input()
new=''.join(set(name))
gender=len(new)
if gender%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
