"""

https://py.checkio.org/en/mission/armstrong-number-checking/

"""


def is_armstrong(num: int) -> bool:

    num_str = str(num)

    qty_digits = len(num_str)

    soma_potencias = sum(int(digito) ** qty_digits for digito in num_str)

    return soma_potencias == num


# Exemplo de uso
print("Example:")
print(is_armstrong(11))  # Saída esperada: False

# Testes de verificação
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
