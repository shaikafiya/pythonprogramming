s=str(input())
for y in range(1,len(s)):
    if s[y:]>s:
        print(s[y:])
        break
        
