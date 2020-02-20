if __name__ == '__main__':
    value = int(input())

    

    for i in range(value):
        value_1 = input()
        lst1 = []
        for letra in value_1:
            lst1.append(int(letra))

        lst1.sort()
        simbolo = 'YES'
        for i in range(0,len(lst1)-1):
            
            if lst1[i+1] -lst1[i] > 1 or lst1[i+1] -lst1[i] < 1:
                simbolo = 'NO'
            
        print(simbolo)