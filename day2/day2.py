def string2Data(string):
    threeSplit = string.split(" ")
    highLowSplit = threeSplit[0].split("-")
    letter2Char = list(threeSplit[1])
    letter2Char = letter2Char[0]
    return int(highLowSplit[0]), int(highLowSplit[1]), letter2Char, threeSplit[2].replace("\n", "")

def validatePassword(low, high, letter, password):
    cSum = 0
    for char in password:
        if(char == letter):
            cSum = cSum + 1
    if(low <= cSum <= high):
        return True
    else:
        return False

def validatePassword2(low, high, letter, password):
    brokenUp = list(password)
    valid = False
    if(brokenUp[low-1] == letter):
        valid = True
    if (brokenUp[high-1] == letter):
        valid = not valid
    
    return valid


def main():
    f = open("day2/input.txt", "r")
    validpasswords = 0
    validpasswords2 = 0
    for x in f:
        low, high, char, password = string2Data(x)
        if(validatePassword(low, high, char, password)):
            validpasswords = validpasswords+1
        if(validatePassword2(low,high,char,password)):
            validpasswords2 = validpasswords2+1
    
    print(validpasswords)
    print(validpasswords2)


    
main()