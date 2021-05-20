def checkNum(userPassword, score):
    # flag for only adding score once
    flag=0
    # check if there are numbers in password
    for i in range(0,10):
        m=str(i)
        if(m in userPassword):
            if(flag==0):
                score += 1  
                flag = 1    
    return score

def checkCapitalChar(userPassword, score):
    # flag for only adding score once
    flag=0
    # check if there are character (A-Z) Capital letters in password
    for i in range(65, 91):
        # 65-91 is the ascii equalent of A-Z
        if(chr(i) in userPassword):
            if(flag==0):
                score += 1
                flag = 1
    return score

def checkSmallChar(userPassword, score):
    # flag for only adding score once
    flag=0
    # check if there are character (a-z) Lowercase letters in password
    for i in range(97, 123):
        # 97-122 is the ascii equalent of a-z
        if(chr(i) in userPassword):
            if(flag==0):        
                score += 1
                flag = 1
    return score

def lengthOfPassword(userPassword, score):    
    # check if the length of the length of the password is long enough
    if(len(userPassword)>8):
        score+=1
    return score

def specialChar(userPassword, score, alphaNumeric):
    # check if any special characters ie characters other than alphanumeric elements are present
    for i in userPassword:
        if(i not in alphaNumeric):
            score+=1
            break
    return score

def main():

    score = 0
    # getting password
    userPassword = input("Enter the password:")

    # Empty list for all alphanumeric elements 
    alphaNumeric=[]
    
    # check if there are character (A-Z) Uppercase letters in password
    for i in range(65, 91):
        # 65-91 is the ascii equalent of A-Z
        alphaNumeric.append(chr(i))
    
    for i in range(0,10):
        m=str(i)
        alphaNumeric.append(m)
    
    # check if there are character (a-z) Lowercase letters in password
    for i in range(97, 123):
        # 97-122 is the ascii equalent of a-z
        alphaNumeric.append(chr(i))
    
    # calling function to check if number exists
    score = checkNum(userPassword, score)

    # calling function to check if capital characters are there
    score = checkCapitalChar(userPassword, score)

    # calling function to check if small characters are there
    score = checkSmallChar(userPassword, score)
     
    # length of password
    score = lengthOfPassword(userPassword, score)
    
    # calling function to check if special characters are there
    score = specialChar(userPassword, score, alphaNumeric)
    
    if(score<4):
       print("Password is invalid. Please add a capital letter, a small letter")
       print("a symbol, a digit and let the minimum length be greater than or equal to 8")
        
    
    elif(score>=4):
        print("Password is strong")
    


    

if __name__ == "__main__":
    main()