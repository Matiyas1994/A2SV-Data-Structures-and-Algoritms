 '''
 roman number to integer. 
 time - O(n)// n=len of roman number
'''  
  val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

  s = "LVIII"

  s = s.replace("IV", "IIII").replace("IX", "VIIII")
  s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
  s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

  result = 0
  for i in s:
      if i in val.keys():
          result += val[i]

  print(result)
