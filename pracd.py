# a=5
# g=8
# print(pow(a,g))


# a=[1,2,3]
# print(*a)

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    small=a[0]
    large=a[0]
    i=0
    while i<len(a):
        if a[i]>a[0]:
            large=a[i]
        if a[i]<a[0]:
            small=a[i]
        i+=1
    print(small,large)