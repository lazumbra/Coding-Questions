def convert_letters_to_hex(string):
    new_string = ''
    for letra in string:
        if letra == 'O':
            new_string += '0'
        elif letra == 'S':
            new_string += '5'
        else:
            new_string += letra
    return new_string

def check_word_decimal(word):
    for letra in word:
        if letra > 'F':
            return 0

    hx_aux = '0x'
    for letra in word:
        hx_aux += letra
    number_hex = int(hx_aux, 16)
    return number_hex    



def hex_word_sum(string):
    string = convert_letters_to_hex(string)

    sum_all_words = 0

    if string == '':
        return 0

    string = string.split(' ')
    if len(string) == 1:
            for letra in string[0]:
                if letra > 'F':
                    return 0
            return check_word_decimal(string)
    else:
        for i in range(len(string)):
            sum_all_words += check_word_decimal(string[i])

    return sum_all_words

print(hex_word_sum('DO YOU SEE THAT BEE DRINKING DECAF COFFEE'))
print(hex_word_sum('BUGS'))


