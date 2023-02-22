# # remove duplicate items

# l=[1,2,3,1,2,2]
# a=[]
# i=0
# while i<len(l):
#     if l[i] not in a:
#         a.append(l[i])
#     i+=1
# print(a)
#  o/p is [1,2,3]

# product of remove duplicate and not remove duplicate item

# l=[1,2,3,4,5,5]
# a=[]
# prod=1
# i=0
# while i<len(l):
#     prod*=l[i]
#     i+=1
# print(prod)
#   ouyput is 600

# l=[1,2,3,4,5,5]
# a=[]
# prod=1
# i=0
# while i<len(l):
#     if l[i] not in a:
#         a.append(l[i])
#         prod*=a[i]
#     i+=1
# print(prod)
# #  output is 120


a=[10,20,2.3]
a.reverse()
print(a)