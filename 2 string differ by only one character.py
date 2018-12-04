h,j=map(str,input().split())
count=0
for x in range(0,len(h)):
    a=h[x]
    b=j[x]
if(a==b):
        count=count
else:
    count=count+1
if(count==1):
            print("yes")
else:
    print("no")
