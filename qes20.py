def larg(a):
    i=0
    m=0
    s=a[0]
    while i<len(a):
        if a[i]>m:
            m=a[i]
        elif a[i]<s:
            s=a[i]
        i=i+1
    return m-s
    
print(larg([1,2,3]))
print(larg([-100,2,100]))
