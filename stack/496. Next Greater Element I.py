class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
     
        '''
        res=[]
        mostack=[]
        dicti=defaultdict(int)
        
        for i in range(len(nums2)):
            if not mostack:
                mostack.append(nums2[i])
            else:
                while mostack and nums2[i] > mostack[-1]:
                    n=mostack.pop()
                    dicti[n]=nums2[i]
                mostack.append(nums2[i])
        while mostack:
            dicti[mostack[-1]]=-1
            mostack.pop()
        for j in nums1:
            res.append(dicti[j])
        return res
        
