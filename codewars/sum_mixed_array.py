def sum_mix(arr):
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])

    return sum



print(sum_mix([9, 3, '7', '3']))