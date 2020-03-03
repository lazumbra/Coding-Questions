class Solution:
    def sortArrayByParity(self, A):
        arrPar = []
        arrImp = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                arrPar.append(A[i])
            else:
                arrImp.append(A[i])

        for i in range(len(arrImp)):
            arrPar.append(arrImp[i])
        return arrPar


Solution().sortArrayByParity([3,1,2,4])