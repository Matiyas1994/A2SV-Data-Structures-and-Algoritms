from collections import Counter
n = int(input())
for i in range(n):
    n2=int(input())
    nums=list(map(int,input().split()))
    c=Counter(nums)
    n2=list(c.keys())
    res=0
    for j in n2:
        if c[j]==1 or j==0 :
            res+=1
        else:
            res+=2
    print(res)

