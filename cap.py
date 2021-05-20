def modify_animal_names(list):
    
    list_length=len(list)

    for i in range(0, list_length):

        list[i] = list[i].capitalize()
    
    return list

def find_replace_name(list, name):

    list_length = len(list)

    for i in range (0, list_length):

        if(list[i] == "Spinosaurus\n"):
            list[i] = name + '\n'

    return list

try:

    newFile = open('info.txt', 'w+')
    nwLine=['ankylosaurus\n','carnotaurus\n','spinosaurus\n','mosasurus']
    newFile.writelines(nwLine)
    newFile.close()

    file1 = open('info.txt', 'r')
    Lines = file1.readlines()
    print("Initially the names in the list are:")
    for line in Lines:
        print(line, end="")

    Lines = modify_animal_names(Lines)

    print("\nThe names in the list after modify_animal_names function is called:")

    for line in Lines:

        print(line, end="")

    yourName=input("\nEnter your name:")
    
    Lines = find_replace_name(Lines, yourName)

    print("\nThe names in the list after find_replace_name function is called:")

    for line in Lines:

        print(line, end="")
    

except:
    print("File not found")
