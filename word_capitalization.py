word=input()
if (word[0].isupper())== True:
    print(word)
else:
    new=str((word[0].upper())+word[1:])
    print(new)
