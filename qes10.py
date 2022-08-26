def num(a,b):
    c=0
    while a<=b:
        if a%10==2 or a%10==3 or a%10==9:
            c+=1
        a+=1
    return c
c=num(1,10)
d=num(11,33)
print(c)
print(d)

