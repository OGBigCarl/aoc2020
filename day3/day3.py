def checkTravel(hori, vert, data):
    vertBound = len(data)
    horiBound = len(data[0]) -1
    trees = 0

    vertTravel = 0
    horiTravel = 0

    while(vertTravel < vertBound):
        if(data[vertTravel][horiTravel] == "#"):
            trees += 1
        vertTravel += vert
        horiTravel = (horiTravel + hori) % horiBound
    
    return trees

def main():
    data =[]
    f = open("day3/input.txt", "r")
    for x in f:
        data.append(list(x))

    print(checkTravel(3,1, data))

    inputs = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    treeSum = 1

    for item in inputs:
        treeSum *= checkTravel(item[0], item[1], data)
    
    print(treeSum)

main()