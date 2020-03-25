class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        numUpper = 0
        for letter in word:
            if letter.isupper():
                numUpper+=1
        
        if numUpper == 0:
            return True

        if numUpper == 1 and word[0].isupper() == True:
            return True
        
        if numUpper == len(word):
            return True
        return False
        
        

if __name__ == "__main__":
    print(Solution().detectCapitalUse("Leetcode"))