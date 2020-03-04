class Solution:
    def isHappy(self, n):
        dicValores = []
        val = n
        while val not in dicValores:
            dicValores.append(val)
            val = sum([int(c) ** 2 for c in str(val)])
            if val == 1:
                return True
        return False

           
        

if __name__ == "__main__":
    n="100"
    p = [int(c) ** 2 for c in str(n)]
    print(p)
    print(Solution().isHappy(19))
    pass
        
