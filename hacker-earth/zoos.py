palavra = input()

len_z = 0
len_o = 0

for letra in palavra:
    if letra == 'z':
        len_z += 1
    else:
        len_o += 1 

if 2 * len_z == len_o:
    print('Yes')
else:
    print('No')