class Book:
    Information=None
    def __init__(self, ID, Name):       #constructor for ID and Name
        self.ID=ID
        self.Name=Name

    def addBookDescription(self, Information):  #method for addin information
        self.Information=Information

    def Description(self):                  #Method to print all information about the
        print('The ID is ',self.ID)                      #book
        print('The Name of the book is :',self.Name)
        if(self.Information != None):
            print('The information are:')
            for i in self.Information:
                print(i)


b1=Book('32','The Book')                    #creating an object for the class
b1.addBookDescription(['Great book on cultural Facts','Best release']) #adding information
b1.Description()                    #calling method to print all the information 
