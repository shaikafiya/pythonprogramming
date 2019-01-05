x1,z1=map(int,input().split())
x2,z2=map(int,input().split())
x3,z3=map(int,input().split())
if((x1==x1==x3) or (z1==z2==z3)):
    print("yes")
elif(((z2-z1)/(x2-x1))==((z3-z1)/(x3-x1))): 
     print("yes")
else:
    print("no")
