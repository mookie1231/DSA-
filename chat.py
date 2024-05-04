def fullDelete(array, val):
    y = 0
    x = 0
    while x < len(array):
        if array[x] == val:
            print('hello')
            y += 1
            for z in range(x, len(array) - 1):
                array[z] = array[z + 1]
        else:
            x += 1
    
    for a in range(y):
        array.pop()
    
    print(array)

newArray = [1, 2, 3, 6, 4, 5, 5, 6, 6, 6, 10]
fullDelete(newArray, 5)
