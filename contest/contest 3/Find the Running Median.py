def runningMedian(a):
    # Write your code here
    import heapq as h
    right = []
    left = []
    res = []
    for val in a:    
        if len(left) > len(right):
            t = h.heappushpop(left,-1*val)
            h.heappush(right,-1*t)

        else:
            t = h.heappushpop(right,val)
            h.heappush(left,-1*t)


        if len(left) > len(right):
            res.append(-1*left[0])
        else:
            res.append((-1*left[0]+right[0])/2)
        
    return res
    
    
