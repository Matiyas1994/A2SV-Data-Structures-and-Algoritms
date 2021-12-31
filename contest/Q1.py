    '''
    printing a pattern ....time-O(n+n+1)=O(2n+1)=O(n). space-O(1)
    '''
    n = 4
    for i in range(n):
        print(" " * (n - i) + "*" * (2 * i + 1))
    for i in range(n + 1):
        print("*" * i)
