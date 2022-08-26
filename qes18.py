def midd(a):
    if len(a)%2==0:
        return ""
    else:
        i=int(len(a)//2)
        return repr(a[i:i+1])
print(midd("abc"))
print(midd("aaaa"))
