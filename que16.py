# l = ["Shogun","Tapioca Express","Burger King","KFC"]
# m = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# i=0
# b=[]
# while i<len(l):
#     if l[i] in m:
#         b.append(l[i])
#     i+=1
# print(b)

l = ["Shogun","Tapioca Express","Burger King","KFC"]
m =["KFC","Shogun","Burger King"]
i=0
b=[]
while i<=len(l):
    if l[i] in m and l[i]<l[i+1]:
        b.append(l[i])
    i+=1
print(b)

