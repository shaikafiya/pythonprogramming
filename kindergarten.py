n=int(input())
if(n==3):
    print(3)
elif (n<=1000000000000000000000):
    b=1
    for i in range(1,n):
        b=b*i
    print(b)
else:
    print("invalid")
