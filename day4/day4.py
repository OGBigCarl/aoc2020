import re

#Parsing input data 
def createDictionaryFromList(data):
    dic = {}
    for ll in data:
        splitArr = ll.split(" ")
        for ss in splitArr:
            splitKV = ss.split(":")
            dic[splitKV[0]] = splitKV[1]
    return dic

def createPassportList(data):
    finalData = []
    temp = []
    for item in data:
        if(item == "\n"):
            dic = createDictionaryFromList(temp)
            finalData.append(dic)
            temp=[]
        else:
            temp.append(item.replace("\n", ""))

    if(temp != []):
        finalData.append(createDictionaryFromList(temp))

    return finalData

#Day 1 functions
def dictionaryContainsEveryKey(dictionary, keys):
    for key in keys:
        if(key not in dictionary):
            return False
    return True

def numberOfValidPassports(data, ignoreList=[]):
    keysToCheck = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    for item in ignoreList:
        keysToCheck.remove(item)
    validSum =0

    for item in data:
        if(dictionaryContainsEveryKey(item, keysToCheck)):
            validSum +=1
    
    return validSum

#Day 2 Functions
def validate_byr(value):
    if(1920 <= int(value) <= 2002):
        return True
    else:
        return False

def validate_iyr(value):
    if(2002 <= int(value) <= 2020):
        return True
    else:
        return False

def validate_eyr(value):
    if(2020 <= int(value) <= 2030):
        return True
    else:
        return False

def validate_hgt(value):
    if("cm" in value):
        if(150 <= int(value.replace("cm", ""))<= 193):
            return True
    elif ("in" in value):
        if(59 <= int(value.replace("in", ""))<= 76):
            return True
    return False

def validate_hcl(value):
    pattern = re.compile("^[a-z0-9]{6}$")
    if(value[0] == '#'):
        if(pattern.match(value.replace("#", ""))):
            return True
    return False

def validate_ecl(value):
    validColors= ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if(value in validColors):
        return True
    else:
        return False

def validate_pid(value):
    pattern = re.compile("^[0-9]{9}$")
    if(pattern.match(value)):
        return True
    else:
        return False

def validate_cid(value):
    return True

def validateKeyValue(key, value):
    if(key == "byr"):
        return validate_byr(value)
    elif (key == "iyr"):
        return validate_iyr(value)
    elif (key == "eyr"):
        return validate_eyr(value)
    elif (key == "hgt"):
        return validate_hgt(value)
    elif (key == "hcl"):
        return validate_hcl(value)
    elif (key == "ecl"):
        return validate_ecl(value)
    elif (key == "pid"):
        return validate_pid(value)
    elif (key == "cid"):
        return validate_cid(value)
    return False

def validateValuesInPassport(data, keysToCheck):
    for key in keysToCheck:
        if(not validateKeyValue(key, data[key])):
            return False
    return True
    

def numberOfValidPassports2(data, ignoreList=[]):
    keysToCheck = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    for item in ignoreList:
        keysToCheck.remove(item)
    validSum =0

    for item in data:
        if(dictionaryContainsEveryKey(item, keysToCheck)):
            if(validateValuesInPassport(item, keysToCheck)):
                validSum += 1
    
    return validSum

def main():
    data =[]
    
    f = open("day4/input.txt", "r")
    for x in f:
        data.append(x)

    passportDict = createPassportList(data)

    iggList=["cid"]
            
    print(numberOfValidPassports(passportDict, iggList))

    print(numberOfValidPassports2(passportDict, iggList))

main()