def get_dim(wood):
    # getting the diemension
    print("Example input and output")
    length=float(input("Enter the length in feet:"))
    width=float(input("Enter the width in inches:"))
    height=float(input("Enter the height in inches:"))
    
    # converting diemensions to feet
    widthInFeet=width/12
    heightInFeet=height/12
    
    # finding the volume
    volume=length*widthInFeet*heightInFeet
    
    # calling weight calculating funtion
    calc_weight(wood, volume)
    return

def calc_weight(data, volume):
    # printing the required outputs
    print("\nSpecies \tMin Weight \tMaxWeight\n")
    for i in range(0, len(data)):
        
        # finding minimum weight
        minWeight = data[i]['min_density']*volume
        minWeightR = round(minWeight,3)
        
        # finding maximum weight
        maxWeight = data[i]['max_density']*volume
        maxWeightr = round(maxWeight,3)

        # printing the output
        print(data[i]['wood']+"\t\t"+str(minWeightR)+"\t\t"+str(maxWeightr))



def main():
    # setting the values 
    wood=[{'wood': 'Balsa','min_density':7,'max_density':9},
            {'wood': 'Hickory','min_density':37.5,'max_density':51},
            {'wood': 'Pine','min_density':22,'max_density':53},
            {'wood': 'Cedar','min_density':23,'max_density':36},
            {'wood': 'Spruce','min_density':25,'max_density':44},
            {'wood': 'Oak','min_density':37,'max_density':56}]
    # calling funtion to get diemensions
    get_dim(wood)


main()