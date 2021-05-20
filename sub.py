def count_squares(s):
    # intial count
    count = 0

    for i in range(0, len(s)):
        # to get all the elements form star
        subWord=s[i]
        for j in range(i+1, len(s)):
            # to find the length and psotion for the subword
            k=j+len(subWord)
            # if the subword and the string is equal 
            if(subWord == s[j:k] and k<=len(s)):
                # increasing count
                count+=1
                break
            # else increasing the subword or adding the next element
            else:
                subWord+=s[j]

    print(count)

# input for entering string
s = input("Enter string:")
count_squares(s)


