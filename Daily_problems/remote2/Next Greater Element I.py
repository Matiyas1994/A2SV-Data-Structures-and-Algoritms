class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      '''
      Time-O(n*m)
      m=number of elements in nums1
      n=number of elements after each element in nums1
      space-O(1)
      '''
        res=[]
        n=len(nums2)
        for i in nums1:
            for j in range(1 +nums2.index(i),n):
                if nums2[j] > i:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
                
        return res
        
