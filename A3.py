#Confeiteiro, Victoria
#CS110 A52
#A#3

#Function 1 Algorithm
#1. Input first name, only alphabetic letters, if conditions is not met
#   then repeat until condition is met
#2. Input last name, only alphabetic letters, if conditions is not me
#   then repeat until condition is met
#3. Input a number greater than 1000, if conditions is not met then
#   repeat until conditions is met
#4. Take first letter of the first name input, and that is the first letter
#   of the username
#5. Take first 6 letters of last name input, and those are after the
#   first letter of the username
#6. Take the number from the number input and assign it to the end
#   of the username
#7. Display username
#8. Ask the user if they want to repeat the loop, if the answer is
#   yes then repeat, if not the loop will terminate

#Function 2 Algorithm
#1. Set variable to control loop
#2. Input seconds
#3. If the user enters less than 60 seconds, then display the value
#   in seconds
#4. If the user enters less than 3,600 seconds then divide the value
#   by 60 (time in minutes), and the remainder is the time in seconds
#5. Display the time in minutes and seconds
#6. If the user enters less than 86,400 seconds then divide the
#   value by 3,600 (time in hours), then the remainder by 60 (time
#   in minutes), and that remainder is the time in seconds
#7. Display the time in hours, minutes, and seconds
#8. If none of the above conditions are true, divide input by 86,400
#   (time in days), then the remainder by 3,600 (time in hours), then
#   the remainder by 60 (time in minutes), and that remainder is the time in seconds
#9. Display the time in days, hours, minutes and seconds
#10.Ask user if the loop needs to be repeated, if yes repeat, if no terminate 

#Narrative: Creates a username
#Preconditions:none
#Post conditions: none
def usernameFunction():
    keepGoing1 = '1'
    while keepGoing1 == '1':
        firstName = input("Please enter your first name: ")
        if firstName.isalpha():
            keepGoing1 = '0'
        else:
            keepGoing1 = '1'
    keepGoing2 = '1'
    while keepGoing2 == '1':
        lastName = input("Please enter your last name: ")
        if lastName.isalpha():
            keepGoing2 = '0'
        else:
            keepGoing2 = '1'
    keepGoing3 = '1'
    while keepGoing3 == '1':
        enterNumber = input("Please enter a number greater than 1,000: ")
        if enterNumber >= '1000':
            keepGoing3 = '0'
        else:
            keepGoing3 = '1'
    firstName = firstName[0]
    lastName = lastName[0:6]
    username = firstName + lastName + enterNumber
    print("Your username is: ", username) 

#Narrative: Calculates time from an input in seconds
#Preconditions:none
#Post conditions: none
def secondsConverter():
    keepGoing = 'y'
    while keepGoing == 'y':
        userEnter = int(input("Enter a time in seconds (s): "))
        days = userEnter // 86400
        leftover1 = userEnter % 86400
        hours = leftover1 // 3600
        leftover2 = leftover1 % 3600
        minutes = leftover2 // 60
        leftover3 = leftover2 % 60
        sec = leftover3

        print("Days: ", days)
        print("Hours: ", hours)
        print("Minutes: ", minutes)
        print("Seconds: ", sec) 
 

        keepGoing = input("Do you want to calculate another (enter y for yes): ") 


def main():
    usernameFunction()
    secondsConverter() 
main() 
