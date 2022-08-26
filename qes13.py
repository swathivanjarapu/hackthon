#  a=[0,1,0,3,12]
a=[0]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]==0:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
c.extend(b)
print(c)
    
    
