newArray = [1,2,3,6,4,5,5,6,6,6,10]

def Mukesh(array):
    array.append(20)
    newArrayPartTwo = array
    x = newArrayPartTwo.count(6)
    print(x)
    print(array)
    array.clear()
    print(array)
    print(newArrayPartTwo)




def delete(array, index):
    for x in range(len(array) - index - 1):
        newArray[index + x - 1] = newArray[(index + x)]
        array.pop()
    print(array)
    


def deleteNum(array, val):
    for x in range(len(array)):
        if (array[x] == val):
           print(x)
           delete(array, x)
           print(array)
        


delete(newArray, 6)
delete(newArray, 7)

    







