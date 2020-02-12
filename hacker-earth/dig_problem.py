valueA, valueB = input().split(' ')
valueB = int(valueB)

new_str = ''

for numero in str(valueA):
    if valueB > 0:
        if numero == '9':
            new_str += numero
        else:
            numero = '9'
            new_str += numero
            valueB -= 1
    else:
        new_str += numero



print(new_str)

