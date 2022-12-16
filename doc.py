# 1

# grocery_list=["flour","cheese","carrots"]
# for i in grocery_list:
#     print(i)

# for i in range(len(grocery_list)):
#     print(i,grocery_list[i])


# 2

# a=[["g","f","g"],["i","s"],["b","e","s","t"]]
# for i in a:
#     for j in i:
#         print(j,end="")
# r="".join(j for i in a for j in i)
# print(r)



# 3
# difference betbeen tuple and list

# 4 product

# list=[6,1,3,5,6,3,1]
# b=[]
# p=1
# for i in list:
#     if i not in b:
#         b.append(i)
#         p*=i
# print(p)

# 5

# ip=[1,2,2,5,8,4,4,8]
# b=[]
# for i in ip:
#     if i not in b:
#         b.append(i)
#         a=len(b)
# print(b)

# 6
# hackerrank

# 7
# hackerrank

# 8
# hackerrank

# 9
# a=[23,12,14,78,98]
# a.sort(reverse=True)
# j=0
# while j<len(a):
#     if j==3:
#         break
#     print(a[j])
#     j=j+1

# a=[23,12,14,78,98]
# max1=0
# max2=0
# max3=0
# for i in a:




# list1 = [10, 20, 4, 45, 99]
 
# mx = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])
# n = len(list1)
# for i in range(2,n):
#     if list1[i] > mx:
#         secondmax = mx
#         mx = list1[i]
#     elif list1[i] > secondmax and \
#         mx != list1[i]:
#         secondmax = list1[i]
#     elif mx == secondmax and \
#         secondmax != list1[i]:
#           secondmax = list1[i]
 
# print("Second highest number is : ",\
#       str(secondmax))


# def findLargest(arr):
#     secondLargest = 0
#     largest = min(arr)
 
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             secondLargest = largest
#             largest = arr[i]
#         else:
#             secondLargest = max(secondLargest, arr[i])
 
#     # Returning second largest element
#     return secondLargest
 
 
# # Calling above method over this array set
# print(findLargest([10, 20, 4, 45, 99]))

# a=[1,2,3,4]
# s=[]
# sum=0
# i=0
# while i<len(a):
#     sum=sum+a[i]
#     # s.append(sum)
#     i+=1
# print(sum)

# a=[1,2,3,4]
# b=sum(a)
# print(b)

# a=[[1,2,3],[1,2,3]]
# s=[]
# sum=0
# i=0
# while i<len(a):
#     whil
#     sum+=i
#     i+=1
# print(sum)



# a=[1,2,3,4]
# a.append([2,3])
# print(a)


a=-4
i=0
while a<5:
    print(i,end=" ")
    a+=1
    i+=1


























































# 10
# hackerrank

# def sq(num):
#     words=list(str(num))
#     for word in words:
#         print(int(word)**2,end="")
# num=9119
# sq(num)


# a=list("9119")
# for i in a:
#     print(int(i)**2,end="")







# def sq(num):
#     a=" ".join(str(int(i)**2) for i in str(num))
#     return int(a)



# n=str(input("enter num"))
# def pc(n):
#     d=list(n)
#     for j in d:
#         print(int(j)**2,end="")
# pc(n)




# a=["9119"]
# for i in a:
#     print(int(a)**2,end="")






































