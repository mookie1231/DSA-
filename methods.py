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
        newArray[index + x] = newArray[(index + x + 1)]
    array.pop()
    print(array)
    


def deleteNum(array, val):
    for x in range(len(array)):
        if (array[x] == val):
           delete(array, x)
           print(array)

# splitting it into multiple functions is what made this so much harder.

def fullDelete(array, val):
    y = 0
    for x in range(len(array)):
        if(array[x] == val):
            y = y + 1
            for z in range(len(array) - x - 1):
                array[x + z] = array[(x + z + 1)]
    
    


              

    







