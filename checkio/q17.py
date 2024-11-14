"""

https://py.checkio.org/en/mission/end-zeros/

------------------------------------------------


"""




def end_zeros(numero: int) -> int:

    str_num = str(numero)
    contador = 0

    for numerozinho in reversed(str_num):
        if numerozinho == "0":
            contador += 1
        else:
            break

    return contador

# Exemplo de uso
print("Example:")
print(end_zeros(10))

# Testes para verificação
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("All tests passed!")
