def uppr(a):
    i=0
    s=[]
    while i<len(a):
        if a[i]==a[i].upper():
            s.append(i)
        i=i+1
    return s
print(uppr("HeLlO"))
