  '''
  a,
  '''
    n=3

    for i in range(1,n+1):
        for j in range(n-i):
            print(' ' ,end=' ')
        for k in range(1,i+1):
           print(k,end=' ')
        for m in range(i-1,0,-1):
            if i==1:
                continue
            print(m,end=' ')
        print(" ")
