#https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    for i in range(len(string)):
        for j in range(i+1, len(string), 1):
            if string[i].lower() == string[j].lower():
                return False
    
    return True


    #your code here

#is_isogram("Dermatoglyphics")
print(is_isogram(""))