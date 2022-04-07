class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        odd= True if len(palindrome)%2 !=0 else False
            
        for i in range(len(palindrome)):
            if i == len(palindrome)-1 and palindrome[i]=="a":
                return palindrome[:-1] + "b"
            
            if  palindrome [i] != "a":
                if odd and i == len(palindrome)//2 and palindrome [i-1] == "a":
                    pass
                else:
                    return palindrome[:i] + "a" + palindrome[i+1:]
