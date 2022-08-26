def arug(a,b):
    i=0
    while i<len(a):
        if a[i] in b:
           return True
        i=i+1
    return False
        
print(arug("typhoon", "opython"))
print(arug("Alice", "Bob"))
print(arug("Swathi", "iaS"))