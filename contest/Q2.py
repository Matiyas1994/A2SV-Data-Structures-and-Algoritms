  '''
  printing a pattern. time-O(n), space-O(1)
  '''
  n=4
   for i in range(n + 1):
     print('*' * i + ' ' * (2 * n - 2 * i) + '*' * i)
