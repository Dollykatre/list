# def mul(i):
#     t=1
#     for x in i:
#         t*=x
#     return t
# print(mul([1,2,-8]))

a=[1,2,-8]
t=1
b=[]
# # for x in a:
#     t*=x
# print(t)
i=0
while i<len(a):
    t*=a[i]
    i+=1
print(t)
# i=0
# while i<len(a):
#     t*=a[i]
#     i+=1
# b.append(t)
# print(b)

# i=0
# while i<len(a):
#     z=a[i]*i
#     i+=1
# print(z)


# largest number list in python

# def m(li):
#     ma=li[0]
#     for a in li:
#         if a>ma:
#             ma=a
#     return ma
# print(m([1,2,-8,0]))

# a=[1,2,-8,0]
# ma=a[0]
# b=[]
# for i in a:
#     if i>ma:
#         ma=i
# b.append(ma)
# print(b)
# i=0
# while i<len(a):
#     if ma<a[i]:
#         ma=a[i]
#     i=i+1
# print(ma)

# i=0
# max=0
# b=[]
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i=i+1
# b.append(max)
# print(b)
