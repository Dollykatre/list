# y=("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\tUp above the world so high, \n\tLike a diamond in the sky. \nTwinkle, twinkle, little stare, \n\tHow I wonder what you are!")
# print(y)

# average question
# m=[
#     [78,76,94,86,88],
#     [91,71,98,65,76],
#     [95,45,78,52,49]
# ]
# for i in range(len(m)):
#     t=0
#     for j in range(len(m[i])):
#         t=t+m[i][j]
#         a=t/5
# print(int(a))


# n=[10,11,12,13,14,15,16,17,18,19]
# number=30
# def find (n,len,number):
#     print("pair whose sum is",number)
#     for i in range(len):
#         for j in range(i,len):
#             if(n[i]+n[j]==number):
#                 print(n[i],n[j])

# n=[10,11,12,13,14,15,16,17,18,19]
# number=30
# print("rt=",n)
# find(n,len(n),number)

# magic square

# n=3
# def m(mat):
#     s=0
#     for i in range(0,n):
#         s=s+mat[i][i]
#     for i in range(0,n):
#         rs=0
#         for j in range(0,n):
#             rs+=mat[i][j]
#         if rs!=s:
#             return False
#     for i in range(0,n):
#         cs=0
#         for j in range(0,n):
#             cs+=mat[j][i]
#         if s!=cs:
#             return False
#     return True
# mat=[
#     [8,3,4,0],
#     [1,5,9],
#     [6,7,2]
# ]
# if m(mat):
#     print("m sq")
# else:
#     print("not m sq")

    
# stud=["dolly","tamanna","neha","ariya"]
# lenght=len(stud)
# dig=[20,30,40,50]
# i=0
# while i<lenght:
#     print(stud[i]+str(dig[i]))
#     i+=1

# a=[23,14,56,12,19,9,15,25,31,42,43]
# e,o=0,0
# for num in a:
#     if num%2==0:
#         e+=1
#     else:
#         o+=1
# print(e)
# print(o)

# a=[23,14,56,12,19,9,15,25,31,42,43]
# b=str(a) 
# es=0
# os=0
# for i in b:
#     for j in str(i):
#         if int(j)%2==0:
#             es+=int(j)
#         else:
#             os+=int(j)
# print(es)
# print(os)


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# # printing original list
# print("The original list is : " + str(elements))

# odd_sum = 0
# even_sum = 0

# for sub in elements:
#     for item in str(sub):
#         if int(item) % 2 == 0:
#             even_sum += int(item)
#         else:
#             odd_sum += int(item)
# print("Odd digit sum : " + str(odd_sum))
# print("Even digit sum : " + str(even_sum))


#  occurence

# cl=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# r=[]
# for i in cl:
#     s=[]   
#     s.append(i) 
#     s.append(cl.count(i))
#     if s not in r:
#         r.append(s)
# print(r)

# 3 step before copy
#     if i not in r:
#         r.append(i)



# l=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# nw=[]
# for a in l:
#     n=l.count(a)
#     if n>1:
#         nw.append(a)
#         # if nw.count(a)==0:
#             # nw.append(a)
# print(nw)
# print(r)


# NEXT QUESTION
# day=int(input("enter the day[1-31]"))
# month=int(input("enter the month[1-12]"))
# year=int(input("enter the year"))
# if year%4==0:
#     print("leap year")
# if year%4!=0:
#     print("note leap year")
#     if month==2:
#         print(day+1,month,year)
# if month in (1,3,5,7,8,10,12):
#     if day<31:
#         print(day+1,month,year)
#     elif day==31 and month<12:
#         print("1",month+1,year)
#     else:
#         print("1","1",year+1)
# elif month==2:
#     if day<28:
#         print(day+1,month,+year)
#     elif day==28:
#         print("1",month+1,year)
#     elif day==29:
#         print("1",month+1,year)
#     else:
#         print("error")
# elif month in (2,4,6,9):
#     if day<30:
#         print(day+1,month,year)
#     elif day==30:
#         print("1",month+1,year)
#     else:
#         print("error")
# else:
#     print("nothing")


# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + int(marks[counter])
#     counter = counter + 1
# print(total_marks)


# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + marks[counter]
#     counter = counter + 1



# a=list("a#b#c#d".split("#"))
# print(a)

# n1=["Amir","Bala","Charlie"]

# for i in n1:
#     n2=n1.lower()
#     print(n2[2][0])


# names1 = ['Amir', 'Bala', 'Charlie']
# names2 = [names1.lower()]
# for name in names1:
#     print(names2[2][0])

a=["python","java","C","C++","c"]
print(max(a))
print(min(a))

# a=list("www.csiplearninghub.com")
# print(a[20:-1])

# l=["tom","mary","simor"]
# l.insert(5,8)
# print(l)

# a=list("welcome")
# print(a)

# l=[1,2,3,4,5]
# for i in l:
#     print(i,end=" ")
#     i+=1























