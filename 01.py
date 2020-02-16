import string
def solution(x):
    newstring = ""
    decoder = {}
    y = reversed(string.ascii_lowercase)
    z = string.ascii_lowercase
    for index, c in enumerate(y):
        char = z[index]
        decoder[c] = char
    
    for char in x:    
        if char in decoder:
            newstring += decoder[char]
        else:
            newstring += char
            
    return(newstring)

print(solution("meeddd"))