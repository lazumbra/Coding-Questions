


if __name__ == '__main__':
    array_len = input()
    array_1 = input()
    array_1 = list(map(int, array_1.split()))

    array_2 = input()
    array_2 = map(int, array_2.split())
    array_2 = list(array_2)

    array3 = []

    for i in range(int(array_len)):
        array3.append(array_1[i] + array_2[i])

    print(' '.join(map(str, array3)))

