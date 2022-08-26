# You are provided an array A of size N  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10
a=[80,20,60,20,80]
i=0
b=0
while i<len(a):
    b= b*10+a[i]%10
    i=i+1
print(b)
if b%10==0:
    print("yes")
else:
    print("no")


    
