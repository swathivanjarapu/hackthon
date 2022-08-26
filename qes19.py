# def add_d(a):
#     b=""
#     i=0
#     while i<len(a):
#         b+=a[i]+"."
#         i=i+1
#     return b

# print(add_d("test"))

def add_r(a):
    c=" "
    j=0
    while j<len(a):
        if a[j]!=".":
            c+=a[j]
        j=j+1
    print(c)

add_r("t.e.s.t")
