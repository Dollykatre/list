# 1 while loop
# gl=['flour','cheese','carrots']
# i=0
# while i<len(gl):
#     print(i,":",gl[i])
#     i+=1

# 1 for loop
# gl=['flour','cheese','carrots']
# # for i in gl:
# #     print(i)
# for i in range(len(gl)):
#     print(i,":",gl[i])

# 2 while loop
# a=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j],end="")
#         j+=1
#     i+=1



# 2for loop
# a=[['g','f','g'],['i','s'],['b','e','s','t']]
# for i in a:
#     for j in i:
#         print(j,end="")

# a=[['g','f','g'],['i','s'],['b','e','s','t']]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end="")


#  ARCHANA DII

# a="sky is blue"
# b=a.split()
# c=b[::-1]
# i=0
# while i<len(c):
#     f="".join(c[i])
#     i+=1
#     print(f,end=" ")


# a="sky is blue"
# b=a.split()
# i=0
# while i<len(b):
#     b.reverse()
#     f="".join(b[i])
#     i+=1
#     print(f,end=" ")

# a="sky is blue"
# i=0
# while i<len(b):
#     b.reverse()
#     print(b)
#     i+=1
# print(b)

# # print(b[::-1])

# for i in b:
#     b.reverse()
#     print(b)
# print(b)

# for i in range(len(b)):
#     b.reverse()
#     print(b)
# print(b)

#  4 for loop
# a=[6,1,3,5,6,3,1]
# b=[]
# prod=1
# for i in (a):
#     if i not in b:
#         b.append(i)
#         prod*=i
# print(prod)


# 4 while loop
# a=[6,1,3,5,6,3,1]
# i=0
# b=[]
# p=1
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         p*=b[i]
#     i+=1
# print(p)

#  5 for loop
# a=[1,2,2,5,8,4,4,8]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         f=len(b)
# print(b)
# print(f)


#  5 while loop
# a=[1,2,2,5,8,4,4,8]
# b=[]
# count=0
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         if a[i]  in b:
#             count+=1
#     i+=1
# print(b)
# print(count)

# 9 maximum num 




# 11
# a=int(input("enter"))
# while a>0:
#     b=a%10
#     c=b**2
#     print(c,end="")
#     a//=10


# 12
# a=int(input("enter num"))
# b=[]
# i=len(str(a))-1
# for k in str(a):
#     if k!="0":
#         b.append(k+"0"*i)
#     i-=1
#     x=" + ".join(b)
# print("'",x,"'")


# try 13
# a=[1,1,2,3,4,4,5,1]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if len(a[i])>1:
#             print(len(a[i]),a[0])
#         else:
#             print(a[0])
#         j+=1
#     i+=1
#     print("7")


# a=[10,20,30]
# b=[40,50,60]
# print(a+b)
# print(a*3)

# try 13
# a=[1,1,22,3,4,4,5,1]


# def encode(message):
#     encoded_message = ""
#     i = 0
 
#     while (i <= len(message)-1):
#         count = 1
#         ch = message[i]
#         j = i
#         while (j < len(message)-1):
#             if (message[j] == message[j+1]):
#                 count = count+1
#                 j = j+1
#             else:
#                 break
#         encoded_message=encoded_message+str(count)+ch
#         i = j+1
#     return encoded_message
 
# #Provide different values for message and test your program
# encoded_message=encode("ABBBBCCCCCCCCAB")
# print(encoded_message)


# 13
# b="aabcddddadnss"
# c=""
# v=[]
# i=0
# while i<=len(b)-1:
#     count=1
#     ch=b[i]
#     u=[]
#     j=i
#     while j<len(b)-1:
#         if b[j]==b[j+1]:
#             count+=1 
#             j+=1
#         else:
#             break
#     c=c+str(count)+ch    
#     i=j+1
# print(c)   


# try 13
# a=[1,1,2,3,4,4,5,1]
# b="aabcddddadnss"
# i=0
# while i<len(a)-1:
#     count=1
#     ch=a[i]
#     j=i


# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# max1=0
# min1=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
        

    
# def longest(lst):
#    longestList = []
#    maxLength = max(len(x) for x in listA)
#    for i in listA:
#       if len(i) == maxLength :
#          longestList = i
#    return longestList, maxLength
# # Driver Code
# listA = [[1,2], [2,45,6,7], [11,6,2]]
# print("Longest List and its length:\n",longest(listA))



# a=[[1,2],[2,45,6,7],[11,6,2]]
# b=[]

# for x in a:
#     maxa=max(len(x))
#     for i in a:
#         if len(i)==maxa:
#             ll=i
#     print(ll)

#  max nested list


# Alist = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]
# # Given list
# print("The given list:\n ",Alist)
# # Use Max
# res = [max(elem) for elem in Alist]
# # Printing max
# print("Maximum values from each element in the list:\n ",res)


# a=[[10,13,454,66,44],[10,8,7,23]]
# b=[]
# for i in a:
#     m=max(i)
#     b.append(m)
# print(b)


# a=[[10,13,454,66,44],[10,8,7,23]]
# r=[max(i) for i in a]
# print(r)

a=[[10,13,454,66,44],[10,8,7,23]]
i=0
b=[]
while i<len(a):
    j=0
    max1=0
    while j<len(a[i]):
        if max1>j:
            max1=a[j]
            b.append(max1)
print(b)








#  firsdt item in list

# Alist = [['Mon', 1], ['Tue', 'Wed', "Fri"], [12,3,7]]
# print("Given List:\n",Alist)
# print("First Items from sublists:\n")
# for item in Alist:
#    print((item[0]))

# a=[['mon',1],['tue',2],['wed',3]]
# for i in a:
#     print(a[0][0])
#  no wrong