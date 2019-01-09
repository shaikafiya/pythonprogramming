p,q=input().split(' ')
for i in range (len(p)):
    if(i<len(p)-1):
        if(p[i]+p[i+1] in q):
            print("yes")
            break
else:
    print("no")
    
