#!/usr/bin/python3

class Solution:
    
    def isPrime(self, number):
        if number % 2  == 0:
            return False
        for i in range(3, number, 2):
            if number % i == 0:
                return False
        
        return True

    def countPrimes(self, n):
        if n == 1 or n == 2:
            return 0
        
        quantity = 0
        i = 2
        for i in range(2,i*i < n,1):
            print('who is it:', i)
            if Solution().isPrime(i):
                quantity+=1
        
        if n >= 2:
            quantity+=1
        return quantity
            
print('oi')
print(Solution().isPrime(1))
print(Solution().countPrimes(10))
        