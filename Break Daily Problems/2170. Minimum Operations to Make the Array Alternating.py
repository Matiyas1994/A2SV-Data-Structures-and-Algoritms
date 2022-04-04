class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n= len(nums)
        if n == 1:
            return  0
    
    
        edic=dict()
        odic= dict()
        
        for i in range(len(nums)):
            if i %2==0:
                if nums[i] in edic:
                    edic[nums[i]] +=1
                else:
                    edic[nums[i]] =1
            else:
                if nums[i] in odic:
                    odic[nums[i]] +=1
                else:
                    odic[nums[i]] = 1
                    
        etuple =[]      
        otuple =[]
        num_even = 0
        num_odd = 0
        
#         Build a max heap and count even and odd numbers
        for key, val in edic.items():
            num_even += val
            etuple.append((-val,key))
        for key, val in odic.items():
            num_odd += val
            otuple.append((-val,key))
    
        heapq.heapify(etuple)
        heapq.heapify(otuple)
        
        
        temp = []
        ke= (num_even + etuple[0][0])
        if otuple[0][1] == etuple[0][1]:
            temp.append(heapq.heappop(otuple))
        if otuple:
            ke +=(num_odd) + otuple[0][0]
        else:
            ke += -1*temp[0][0]
        
        
        while temp:
            heapq.heappush(otuple,temp.pop())
        
        
        ko =(num_odd + otuple[0][0])
        if etuple[0][1] == otuple[0][1]:
            t2 = heapq.heappop(etuple)
        
        if etuple:
            ko +=(num_even) + etuple[0][0]
        else:
            ko +=-t2[0]
        
        
        return min(ke,ko)        
        
