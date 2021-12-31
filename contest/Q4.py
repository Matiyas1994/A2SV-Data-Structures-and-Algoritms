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
'''
b,
'''
      n=4

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
    for i in range(1,n):
        for j in range(1,i+1):
            print(" ",end=" ")
        for k in range(1,n-i+1):
            print(k,end=" ")
        for m in range(n-i-1,0,-1):
            print(m,end=' ')
        print(' ')

'''
c,
'''
  n=5
    for i in range(n):
       if i%2==0:
           for j in range(n):
                print('##  ', end=' ')
       else:
           for j in range(n-1):
                print('  ##',end=' ')
       print()

  
