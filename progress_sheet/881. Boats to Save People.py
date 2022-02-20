class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1 = 0
        p2 = len(people)-1
        ans=0
        while p1 <= p2:
            if people[p2] < limit:
                if people[p2] + people[p1] <= limit:
                    ans +=1
                    p1 += 1
                    p2 -=1
                else:
                    ans +=1
                    p2 -= 1 
            else:
                ans +=1
                p2 -=1
            
        return ans
