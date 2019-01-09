n=(input())
arr=[]
s=0
for y in n:
    if not y in arr:
        s+=1
        arr.append(y)
    else:
        break
print(s)   
