#Confeiteiro, Victoria
#CS110 A52
#A#2

#Question 1 Algorithm
#1. Input 1st string
#2. Input 2nd string
#3. Print 2nd string and 1st string in that order, seperated by a comma with a
#   dash (-) as the first and last characters

#Question 2 Algorithm
#1. Input a string that is at least 3 charcaters
#2. Get length of string input
#3. Print the length of the string
#4. Print the first character of the string
#5. Print the last character of the string
#6. Print string with the last three characters replaced with the letters 'ABC'

#Question 3 Algorithm
#1. Store the hectare to acres conversion rate
#2. Store the euros to dollars converison rate
#3. Input the hecatre amount
#4. Input the cost per hectare in euros
#5. Calculate the total cost in euros by multiplying the hectare amount
#   and the cost per hectare
#6. Print the hectare amount
#7. Print the cost per hectare in euros
#8. Print the total cost in euros
#9. Calculate the amount of acres by multiplying the hectare to acres converion rate
#   by hectare amount
#10. Calculate the cost in dollars by multiplying the euros to dollars converison
#    rate by hectare cost
#11. Calculate the total cost in dollars by multiplying the amount of acres by the
#    cost in dollars
#12. Print the hectare amount converted into acres
#13. Print the cost per hectare in dollars
#14. Print the total cost in dollars

#Question 4 Algorithm
#1. Store the kg to lbs conversion rate
#2. Store the m/s to ft/s conversion rate
#3. Input the mass in kg
#4. Input velcoity in m/s
#5. Calculate momentum in kg/ms by multiplying the mass in kg by the velocity in m/s
#6. Print the momentum in kg/ms
#7. Calculate the mass in lbs by multiplying the kg to lbs coverison rate by the mass in kg
#8. Calculate the velocity in ft/s by multiplying the m/s to ft/s conversion rate
#   by the velocity in m/s
#9. Calculate momentum in lbs*ft/s by multiplying mass in lbs by velcoity in ft/s
#10. Print the momentum in lbs*ft/s

#Question 5 Algorithm
#1. Store all 4 distances in miles
#2. Store all 4 drving times in hours
#3. Store the break time in hours
#4. Store the money earned per mile in dollars
#5. Calculate the total distance driven by adding up all 4 distances
#6. Print the total distance in miles
#7. Calculate total time needed by adding up all 4 driving times and break time
#8. Print total time needed in hours
#9. Caclulate the total driving time by adding all 4 times
#10. Print total driving time in hours
#11. Calculate total amount earned by multiplying total distance driven by money
#    earned per mile
#12. Print the total amount earned in dollars
#13. Caculate amount earned per hour by dividing the total distance driven by
#    the toal amount earned
#14. Print the amount earned per hour in dollars
#15. Calculate the amount earned from NY to LA by multiplying the distance between NY and LA
#    by the money earned per mile
#16. Print the amount earned from NY to LA in dollars
#17. Calculate the amount earned from LA to TX by multiplying the distance between LA and
#    TX and the money earned per mile
#18. Print the amount earned from LA to TX in dollars
#19. Calculate the amount earned from TX to NOLA by multiplying the distance between
#    TX and NOLA and the money earned per mile
#20. Print the amount earned from TX to NOLA in dollars
#21. Calculate the amount earned from NOLA to NY by multiplying the distance between
#    NOLA and NY by the money earned per mile
#22. Print the amount earned from NOLA to NY in dollars

#Narrative: Prints input reversed with comma in-between and a dash as first and last character
#Preconditions: none
#Post conditions:none 
def stringReverse():
    string_1 = input("Enter a string: ")
    string_2 = input("Enter a string: ")
    print("-" + string_2 + "," + string_1 + "-" "\n")

#Narrative: Prints length, first and last character, and replaces last 3 characters
#           with 'ABC' of string input
#Preconditions: none
#Post condtions: none
def stringInfo():
    only_string = input("Enter a string that is at least 3 characters: ")
    string_length = len(only_string)
    print("The lenght of your string is: ", string_length)
    print("The first character is: ", only_string[0])
    print("The last character is: ", only_string[-1])
    print(only_string.replace(only_string[-3:len(only_string)],"ABC\n"))

#Narrative: Converts hectare to acre and euros to dollars, calculates total cost
#           and displays user input and results
#Preconditions: none
#Post conditions: none 
def hectareConversion():
    ACRES_CONVERT_RATE = 2.47105
    DOLLAR_CONVERT_RATE = 1.29
    hectare_amount = int(input("Enter the hectare amount: "))
    hectare_cost = int(input("Enter the cost per hectare in Euros: "))
    total_cost_euros = hectare_amount * hectare_cost
    print("The hectare amount entered is: ", hectare_amount)
    print("The cost per hectare entered in Euros is: ", hectare_cost)
    print("The total cost in Euros is: ", format(total_cost_euros, '.2f'))
    acres_amount = ACRES_CONVERT_RATE * hectare_amount
    dollars_cost = DOLLAR_CONVERT_RATE * hectare_cost
    total_cost_dollars = acres_amount * dollars_cost
    print("The hectare amount entered converted into acres is: ", \
          format(acres_amount, '.2f'))
    print("The cost per hectare in dollars is: ", format(dollars_cost, '.2f'))
    print("The total cost in dollars is: ", format(total_cost_dollars, '.2f'))
    print("\n")

#Narrative: Caclauates momentum in kg*m/s and lbs*ft/s
#Preconditions:none
#Post conditions: none
def momentumFunction():
    KILOGRAM_CONVERT_RATE = 2.20462
    FTS_CONVERT_RATE = 3.28084
    mass_kilograms = int(input("Enter the mass in kilograms (kg): "))
    velocity_ms = int(input("Enter the velocity in meters per second (m/s): "))
    momentum_kg_ms = mass_kilograms * velocity_ms
    print("The momentum in kg*m/s is: ", format(momentum_kg_ms, '.2f')) 
    mass_pounds = KILOGRAM_CONVERT_RATE * mass_kilograms
    velocity_fts = FTS_CONVERT_RATE * velocity_ms
    momentum_ft_s = mass_pounds * velocity_fts
    print("The momentum in lbs*ft/s is: ", format(momentum_ft_s, '.2f'))
    print("\n") 

#Narrative: Calculate and display imformation regarding John's 4 drving trips
#Preconditions: none
#Post conditins: none
def drivingFunction():
    NY_LA_DISTANCE = 2775
    LA_TX_DISTANCE = 1546
    TX_NOLA_DISTANCE = 348
    NOLA_NY_DISTANCE = 1303
    NY_LA_TIME = 39
    LA_TX_TIME = 22
    TX_NOLA_TIME = 5
    NOLA_NY_TIME = 19
    BREAK_TIME = 72
    MONEY_PER_MILE = .65
    total_distance_driven = NY_LA_DISTANCE + LA_TX_DISTANCE + TX_NOLA_DISTANCE + NOLA_NY_DISTANCE
    print("The total distance driven in miles is: ", total_distance_driven)
    total_time = NY_LA_TIME + LA_TX_TIME + TX_NOLA_TIME + NOLA_NY_TIME + BREAK_TIME
    print("The total time needed in hours is: ", total_time)
    total_driving_time = NY_LA_TIME + LA_TX_TIME + TX_NOLA_TIME + NOLA_NY_TIME
    print("The total driving time in hours is: ", total_driving_time)  
    total_amount_earned = total_distance_driven * MONEY_PER_MILE
    print("The total amount earned in dollars is: ", format(total_amount_earned, '.2f'))
    amount_per_hour = total_driving_time / total_amount_earned
    print("The amount earned per hour in dollars is: ", format(amount_per_hour, '.2f'))
    amount_NYLA = NY_LA_DISTANCE * MONEY_PER_MILE
    print("The amount earned from driving from New York, NY to Los Angeles, CA in dollars is: ", \
          format(amount_NYLA, '.2f'))
    amount_LATX = LA_TX_DISTANCE * MONEY_PER_MILE
    print("The amount earned from driving from Los Angeles, CA to Huston, TX in dollars is: ", \
          format(amount_LATX, '.2f'))
    amount_TXNOLA = TX_NOLA_DISTANCE * MONEY_PER_MILE
    print("The amount earned from driving from Huston, TX to New Orleans, LA in dollars is: ", \
          format(amount_TXNOLA, '.2f'))
    amount_NOLANY = NOLA_NY_DISTANCE * MONEY_PER_MILE
    print("The amount earned from driving from New Orleans, LA to New York, NY in dollars is: ",\
          format(amount_NOLANY, '.2f'))
    

def main():
    stringReverse()
    stringInfo()
    hectareConversion()
    momentumFunction()
    drivingFunction()
    
main() 
