s=input()
n=[]
for i in s:
    if(i not in n):
        n.append(i)
if(len(n)==26 or len(n)==27):
    print("yes")
else:
    print("no")
    
