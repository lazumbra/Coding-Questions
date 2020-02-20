def find_min(list, number):
    for i in range(len(list)):
        if list[i] < number:
            return False
        
    return True



if __name__ == '__main__':
    test_cases = input()
    for i in range(int(test_cases)):
        vector_1 = input()
        vector_1 = list(map(int, vector_1.split()))

        vector_2 = input()
        vector_2 = map(int, vector_2.split())
        vector_2 = list(vector_2)

        menor_elemento = min(vector_2)

 
        if vector_1[1] - menor_elemento < 0:
            print(0)
        else:
            print(vector_1[1] - menor_elemento)  