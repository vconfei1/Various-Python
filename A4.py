#Confeiteiro, Victoria
#CS 110 A52
#A#4

        
def getDimensions():
    length = int(input("What is the length of the pool?: "))
    width = int(input("What is the width of the pool?: "))
    depth = int(input("What is the depth of the pool?: "))
    metersCalculations(length, width, depth)
    conversion(length, width, depth)
    
        
def metersCalculations(length, width, depth):
    volume = length * width * depth
    surfaceArea = (2 * length * width) + (2 * width * depth) 
    perimeter = (length * 2) + (width * 2)
    print("The amount of water needed to fill the pool is: ", volume)
    print("The swimming surface area is: ", surfaceArea)
    print("The surface perimeter of the pool is: ", perimeter)
    

def conversion(length, width, depth):
    feetConvert = 3.28084
    lengthFeet = length * feetConvert
    widthFeet = width * feetConvert
    depthFeet = depth * feetConvert

    volumeFeet = lengthFeet * widthFeet * depthFeet
    surfaceAreaFeet = lengthFeet * widthFeet
    perimeterFeet = (lengthFeet * 2) + (widthFeet * 2)

    print("The amount of water needed to fill the pool in feet is: ", volumeFeet)
    print("The swimming surface area in feet is: ", surfaceAreaFeet)
    print("The surface perimeter of the pool in feet is: ", perimeterFeet)
    print('\n') 

def getIntegers():
    keepGoing = 1
    while keepGoing == 1:
            int1 = int(input("Please enter an integer between 1 and 10: "))
            if int1 >= 1 and int1 <= 10:
                keepGoing = 0
            else:
                keepGoing = 1
    keepGoing1 = 1
    while keepGoing1 == 1:
            int2 = int(input("Please enter a different integer greater than the first integer: "))
            if int2 >= 1 and int2 <= 10 and int1 < int2:
                keepGoing1 = 0
            else:
                keepGoing1 = 1
    calculationFunction(int1, int2) 

def calculationFunction(int1, int2):
    product = 1
    for i in range(int1, int2+1):
        product*=i
    addAnswer = 0
    for i in range(int1, int2+1):
        addAnswer+=i
    printResults(product, addAnswer) 
    

def printResults(product, addAnswer):
    print("The product of all the numbers in range: ", product)
    print("The sum of all the numbers in range: ", addAnswer)
    print('\n')

def chooseUnits():
    keepGoing = 1
    while keepGoing == 1:
        userUnit = input("Enter 'm' if you wants to use metric units, enter 'u' if you want to use US customary units: ")
        if userUnit == 'm':
            distanceDrivenKM = int(input("Enter the distance driven in kilometers: "))
            fuelConsumedL = int(input("Enter the fuel consumed in liters: "))
            keepGoing1 = input("Do you want to repeat enter 'y' for yes, if not enter 'n': ")
            if keepGoing1 == 'y':
                keepGoing = 1
            else:
                keepGoing = 0
        else:
            distanceDrivenM = int(input("Enter the distance driven in miles: "))
            fuelConsumedG = int(input("Enter the fuel consumed in miles: "))
            keepGoing2 = input("Do you want to repeat enter 'y' for yes, if not enter 'n': ")
            if keepGoing2 == 'y':
                keepGoing = 1
            else:
                keepGoing = 0
    metersCalculation(distanceDrivenKM, fuelConsumedL)
    usCalculation(distanceDrivenM, fuelConsumedG)

def metersCaclulation(distanceDrivenKM, fuelConsumedL):
    mpg = distanceDrivenKM / fuelConsumedL
    print("Your distance driven in kilometers is: ", distanceDrivenKM)
    print("Your fuel consumed is: ", fuelConsumedL)
    print(format("Your fuel consumed per mile is: ", mpg, '.2f'))

def usCalculation(distanceDrivenM, fuelConsumedG):
    mpg = distanceDrivenM / fuelConsumedG
    print("Your distance driven in miles is: ", distanceDrivenM)
    print("Your fuel consumed is: ", fuelConsumedG)
    print(format("Your fuel consumed per mile is: ", mpg, '.2f'))
    
    
            
def main():
    getDimensions()
    getIntegers()
    chooseUnits() 
 
 
  

main()
    
    
