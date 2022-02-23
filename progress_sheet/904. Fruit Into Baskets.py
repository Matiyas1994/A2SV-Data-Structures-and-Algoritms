class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ''''
        maxi = float(-inf)
        p1 = 0
        p2 = 0
        n = len(fruits)-1
        fset = set ()
        while p2 <= n: 
            while len(fset) <= 2 and p2 <= n:
                if fruits[p2] not in fset:
                    fset.add(fruits[p2])
                p2 +=1
            maxi = max(maxi,p2-p1)
            p1 +=1
            p2 = p1
            fset.clear()
        return maxi
        '''
        first_fruit = float(-inf)
        last_fruit =float(-inf)
        Number_of_lastFruit = 0
        curMax = 0
        maxi = float(-inf)
        
        for f in fruits:
            if f == first_fruit or f == last_fruit:
                curMax += 1
            else:
                curMax = Number_of_lastFruit + 1
            if f == last_fruit:
                Number_of_lastFruit += 1
            else:
                Number_of_lastFruit = 1
            if f != last_fruit:
                first_fruit = last_fruit
                last_fruit = f
            maxi = max(curMax,maxi)
        
        
        return maxi
