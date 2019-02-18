m=int(input())
if(m>0 and (m & (m-1))==0):
    print("0")
else:
    if(m%2!=0):
        print("1")
    else:
        print("2")

