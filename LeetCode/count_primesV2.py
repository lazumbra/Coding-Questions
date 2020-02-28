#!/usr/bin/python3
import math

class Solution:
    
    def isPrime(self, number):
        if number % 2  == 0:
            return False
        for i in range(3, number, 2):
            if number % i == 0:
                return False
        
        return True

    def countPrimes(self, n):
        listOfZeros = [0] * (n-1)
        squareNumber = int(math.sqrt(n))

        for i in range(2, squareNumber+1):
            for j in range(i+i, n, i):
                listOfZeros[j-1] = 1
        
        num_primes = listOfZeros.count(0) - 1
        print(listOfZeros)
        if num_primes > 0:
            return num_primes
        else:
            return 0 



            
print('oi')
print(Solution().isPrime(1))
print(Solution().countPrimes(1378))
        