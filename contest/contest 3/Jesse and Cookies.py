
def cookies(k, A):
    # Write your code here
    import heapq as h
    h.heapify(A)
    Minop = 0
    
    while A[0] < k:
        if len(A) < 2:
            return -1
        
        ls = h.heappop(A)
        sls =h.heappop(A)
        Sum = ls + 2*sls 
        h.heappush(A,Sum)
        Minop +=1
        
    return Minop
    
