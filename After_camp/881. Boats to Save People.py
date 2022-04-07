class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, p1, p2 =  0 ,0, len(people)-1
        
        while p1 <= p2:
            if people[p2] + people[p1] <= limit:
                p1 += 1
            p2 -= 1 
            ans +=1
            
        return ans
