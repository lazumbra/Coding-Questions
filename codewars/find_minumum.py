#https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python

def sum_of_minimums(numbers):
    list_minumums = []
    for i in range(len(numbers)):
        minum = 999999999   
        for j in range(len(numbers[0])):
            print(numbers[i][j])
            if numbers[i][j] < minum:
                minum = numbers[i][j]
        list_minumums.append(minum)

    return sum(list_minumums)

    

sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ])