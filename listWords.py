# defining the function
def listLetters(text1):
    # initiazing the counts dictionary
    counts={}
    
    # looping through all the elements
    for i in text1:
        
        # adding the count if the characters exists
        if(i in counts.keys()):
            counts[i]+=1
        
        # skipping blank spaces
        elif(i==' '):
            continue
        
        # creating the element key if it doesn't exist
        else:
            counts[i]=1
    
    # returning the dictionary
    return counts


# word list finding function
def listWord(text1):
    # each word will have a space so we split
    k = text1.split()

    wordCount={}

    for i in k:
        # if the word exists in dictionary adding the occurence
        if(i in wordCount.keys()):
            wordCount[i]+=1
        
        # creating a key value pair if the word is encountered for the first time
        else:
            wordCount[i]=1

    # returning the value
    return(wordCount)

# getting the input
text1=input("Enter input String:")

# calling and printing the values
print(listLetters(text1))

# calling the listWord function
print(listWord(text1))