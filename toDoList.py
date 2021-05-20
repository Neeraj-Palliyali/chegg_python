
# getting the file name and returning the elements as a list
def getList(filename):
    # opeing the file
    openFile = open(filename, "r+")
    # reading the file
    data = openFile.read().split('\n')
    # since the data gets intialized with an non empty list that is an empty file with /n
    # we pop the first /n character. To make the list empty
    data.pop()
    # closing the file
    openFile.close()
    return data


# showing the list recieving the list
def showList(data):
    # print an list as empty if there is nothing
    if(len(data)==0):
        print("Your To Do List is empty.")
    # printing the to do list as it is
    else:
        print("To Do List:")
        for i in range(1, len(data)+1):
            print(" "+str(i)+") "+data[i-1])
    return

# adding things to the list
def addToList(filename, data):
    # asking the input to do list
    toAdd=input("Add:")
    print("Item added to list.")
    # appending the element to the "to do" list
    data.append(toAdd)
    # opening the file
    openFile = open(filename, "r+")
    # writing the elements to the file
    openFile.writelines(toAdd)
    openFile.close()
    # returning the data with added "to do"
    return data

# deleting the element from the list
def deleteFromList(filename, data):
    # getting the input elemnet
    element = int(input("Item number to delete:"))
    # deleting the element from the list
    del data[element-1]
    print("Item deleted from list.")
    # opening the file as empty
    openFile = open(filename, "w+")
    # writing the elements to the file
    openFile.writelines(data)
    openFile.close()
    return data

# ------main part of program ----------
FILENAME = 'list.txt'
lineList = getList(FILENAME)

# endless loop until the user presses 'x' for exit
while True:

    showList(lineList)

    print('\nType "a" to add an item.')

    if len(lineList) > 0:
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    # prompt for a command
    command = input('> ')

    # 'a' for append
    if(command =='a'):
        lineList = addToList(FILENAME, lineList)

    # 'd' for delete
    elif (command == 'd' and len(lineList)>0):
        lineList = deleteFromList(FILENAME, lineList)

    # 'x' for exit
    elif command == 'x':
        print('Goodbye!')
        break

    # else invalid command
    else:
        print('Invalid command \n') 