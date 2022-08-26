# n=int(input("enter ur number"))
# i=1
# while i<n:
#     if n==4**i:
#         print("true")
#     else:
#         print("false")
#     i=i+1




# def power(a):
#     i=1
#     while i<a:
#         if a==4**i:
#             i=i+1
#         return True,False
# print(power(16))

def squ(num):
    if num==0:
        return False
    while num!=1:
        if num%4!=0:
            return False
        num=num//4
    return True
print(squ(16))
print(squ(5))
print(squ(1))