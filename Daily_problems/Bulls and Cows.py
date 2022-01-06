class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret =list(map(str,secret))
        guss=list(map(str,guess))
        cow=0
        bull=0
        zipped=list(zip(secret,guss))
        
        for i in zipped:
            if i[0]==i[1]:
                bull+=1
                secret.remove(i[0])
                guss.remove(i[0])
                
        for j in guss:
            if j in secret:
                cow+=1
                secret.remove(j)
                
        return (str(bull)+"A"+str(cow)+"B")
        
        
        
