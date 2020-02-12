#https://www.hackerearth.com/pt-br/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/description/

binary_number = input()
print(len(binary_number))

total = 0
resultado = 0

for i in range(len(binary_number) - 1):
    if binary_number[i+1] == binary_number[i]:
        total += 1
        print('yes', i, binary_number[i+1], binary_number[i])
        print('total', total)
        if total >= 6:
            print('entrei aqui')
            resultado = 6
    else:
        total = 0
    print(binary_number[i+1], i)

print(resultado)