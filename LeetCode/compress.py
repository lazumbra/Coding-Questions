from typing import List

def compress(chars):
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    print(chars)
    return write

'''def compress(chars):
    total = 0

    dicionario_final = {}

    for i in range(len(chars)):
        if chars[i] in dicionario_final:
            dicionario_final[chars[i]] += 1
        else:
            dicionario_final[chars[i]] = 1
    
    for key in dicionario_final:

        if len(str(dicionario_final[key])) > 1:
            total += len(str(dicionario_final[key]))
            total += 1
        elif dicionario_final[key] == 1:
            total += 1
        else:
            total += 2
    
    
    return total'''
    

if __name__ == '__main__':

    print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
 


'''
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

'''