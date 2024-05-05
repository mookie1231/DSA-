newArray = [6,1,6,2,6,3,6,4,5,5,6,10,6,10,6]

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
# a bug arises if there are two of the same numbers adjacent to each other 
# every problem causes other problems to arise - shoudl give it a shot but at your stage it is worth looking at optimal solutions faster 
# I don't think it is efficient trying to discover optimal solution myself 

def fullDelete(array, val):
    y = 0
    for x in range(len(array)):
        if(array[x] == val):
            print('hello')
            y = y + 1
            for z in range(len(array) - x - 1):
                array[x + z] = array[(x + z + 1)]
    


    for a in range(y):
        array.pop()
    
    print(array)

fullDelete(newArray,6)

              

    







