class Solution:
    def calPoints(self, ops: List[str]) -> int:
      '''
      time-O(n+m)
      n=# of elements of ops
      m=# of elements in rec
      '''
        rec=[]
        for i in range(len(ops)):
            if ops[i].lstrip("-").isdigit():
                rec.append(int(ops[i]))
            elif ops[i] == 'C':
                rec.pop()
            elif ops[i]=='D':
                rec.append(2*rec[-1])
            elif len(rec) >=2 and ops[i] == "+":
                rec.append(rec[-1]+rec[-2])
        return sum(rec)
        
