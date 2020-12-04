import os

def my2sum(data, target):
    for i, item in enumerate(data, start=0):
        for nxt in data[i+1:]:
            if(item+nxt == target):
                return [item, nxt, item*nxt]
    return []

def my3sum(data, target):
    for item in data:
        check = my2sum(data, target-item)
        if(check != []):
            return [item, check[0], check[1], item*check[0]*check[1]]
    return []

def main():
    data = []
    f = open("day1/input.txt", "r")
    for x in f:
        data.append(int(x)) 
    
    print(my2sum(data, 2020))
    print(my3sum(data, 2020))
    
main()