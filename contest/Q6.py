'''
input=[0, 1, 0, 3, 12]
output=[1,3,12,0,0]
sort and put the zeros at the end.
time-O(nlogn)//for the sorting.
'''


  k = [0, 1, 0, 3, 12]
  zeros = []
  for i in k:
      if i == 0:
          zeros.append(i)
          k.remove(i)

  k_sorted = sorted(k)
  print(k_sorted + zeros)
