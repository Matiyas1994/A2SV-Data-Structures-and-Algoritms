class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        r = count["R"]
        d = count["D"]
        arr = list(senate)
        silencer=[0,0]
        
        while r!=0 and d!=0:
            for i in range(len(arr)):
                if arr[i] ==silencer[0] and silencer[1] > 0:
                    arr[i]=0
                    silencer[1] -=1
                
                else:
                    if arr[i] == "R":
                        silencer[0]="D"
                        silencer[1] +=1
                        d -=1
                    elif arr[i]=="D":
                        silencer[0]="R"
                        silencer[1] +=1
                        r -=1
                    
                if r == 0:
                    return "Dire"
                if d == 0:
                    return "Radiant"
                
        return "Dire" if r==0 else "Radiant"
        
