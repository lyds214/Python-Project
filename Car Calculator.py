#This function calculates the cost of fuel per year for an electric car and a gas-driven car.
def cost_of_fuel():
    YEAR = 12

    #We used a while loop to check the input validation to see if their value is a positive number or not
    #(NOTE: 0 is neither a positive or a negative number. So if the user enters 0, then the program will
    #ask the user to input their value again until it's a positive number).
    car1_mi = float(input("Enter car 1's kW-h/mi:"))

    while car1_mi <= 0:
        car1_mi = float(input("Enter car 1's kW-h/mi:"))

    cost_per_kilowat = float(input("Enter cost per kW-h:"))

    while cost_per_kilowat <= 0:
        cost_per_kilowat = float(input("Enter cost per kW-h:"))

    car2_mpg = float(input("Enter car 2's MPG:"))

    while car2_mpg <= 0:
        car2_mpg = float(input("Enter car 2's MPG:"))

    cost_per_gal = float(input("Enter gas cost per gallon:"))

    while cost_per_gal <= 0:
        cost_per_gal = float(input("Enter gas cost per gallon:"))

    miles_per_month = float(input("How many miles do you drive per month?"))

    while miles_per_month < 0:
        miles_per_month = float(input("How many miles do you drive per month?"))
        

    #Once the program checks to see that all of their values are positive,
    #the formulas down below would calculate the electric car's and the gas car's
    #cost of fuel per year.
    kiloWattHour_per_year = (car1_mi * miles_per_month) * YEAR
    car1Price_per_year = kiloWattHour_per_year * cost_per_kilowat

    gallons_per_year = (miles_per_month / car2_mpg) * YEAR
    car2Price_per_year = gallons_per_year * cost_per_gal



    #This formula down below subtracts the electric car's and the gas car's cost of fuel per year
    #to see if they are within $5.
    #When we subtract variable "car2Price_per_year" from variable "car1Price_per_year:,
    #the variable "savings" can either be a positive or a negative number.
    #A graph down below can better explain our if-elif-else statements.

    # < ------- | --- |---- | ------- >
    #          -5     0     5

    #The "-" represents the possible values of variable "savings" and "|" represents an if, elif, or else statement.
    #A short logic explanation of this line of code:
        # electric - gasoline = +savings (if savings is a positive number, then gasoline is more efficient)
        # gasoline - electric = -savings (if savings is a negative number, then gasoline is more efficient)
    
    savings = car1Price_per_year - car2Price_per_year



    #If variable "savings" is greater than 5, then it'll print out that Car 2 is more efficient.
    #If variable "savings" is less than -5, then it'll print out that Car 1 is more efficient.
    #If variable "savings" is in a range of 0-5, then it'll print out that both Car 1 and Car 2 cost the same.
    if savings > 5:
        print(f"Car 2 will save",'${:.2f}'.format(savings), "in a year.")
        
    elif savings < -5:
        savings = -savings
        print(f"Car 1 will save",'${:.2f}'.format(savings), "in a year.")
        
    else:
        print("The two cars cost the same.")
    

#This function calculates the depreciation of a car value throughout the years.
def used_value():
    
    #This is a constant value of the depreciation rate.
    DEPRECIATION_RATE = 0.82

    #We used a while loop to check to see if the user's input is a positive number or not.
    original_car_price = float(input("Enter original car price:"))

    while original_car_price <= 0:
        original_car_price = float(input("Enter original car price:"))

    num_years = int(input("Enter number of years:"))

    while num_years <= 0:
        num_years = int(input("Enter number of years:"))

    #To calculate the depreciation of a car value, we used a for-loop because there's a limited
    #amount of times that the for-loop can iterate. The amount of times the for-loop iterates
    #depends on variable "num_years" (number of years). Every time the loop iterates, the
    #car value's would be printed.
    for x in range(num_years):
        original_car_price *= DEPRECIATION_RATE
        print("Year", x + 1, "value:", "${:.2f}".format(original_car_price))


#This function determines how far a car will travel before stopping when you apply the brakes at a certain speed.
def stopping_distance():
    MILE_TO_FEET = 5280
    ACCELERATION = 32.174
    FRICTION_COE = 0
    MIN = 60
    SEC = 60

    #We used a while loop to check the user's input to see if it's a positive number or not before it goes to the next line of code.
    #The initial speed's unit is miles.
    initial_speed = float(input("Enter initial speed:"))

    while initial_speed <= 0:
        initial_speed = float(input("Enter initial speed:"))

    tire_condition = float(input("Enter tire condition (1 = new, 2 = good, 3 = poor):"))

    #Additionally, we applied the DeMorgan's Law to check the user's input when they're asked to enter their tire condition.
    #Reason for this is that if they don't input a value that's from 1-3, then the program will ask the user to enter their value again
    #until they enter a number that's from 1-3.
    while tire_condition != 1 and tire_condition != 2 and tire_condition != 3:
        tire_condition = float(input("Enter tire condition (1 = new, 2 = good, 3 = poor):"))

   #This block of if-elif statements assigns the friction coefficients and the condition of tires depending on variable "tire_condition".
    if tire_condition == 1:
        FRICTION_COE = 0.8
        tire_name = "new tires"

    elif tire_condition == 2:
        FRICTION_COE = 0.6
        tire_name = "good tires"
        
    elif tire_condition == 3:
        FRICTION_COE = 0.5
        tire_name = "poor tires"


    #This line of code converts the variable "initial_speed" into ft/s.
    convert_speed = ((initial_speed * MILE_TO_FEET) / MIN) / SEC

    #This line of code calculates the distance of how far a car will travel before stopping when you apply the brakes at a certain speed.
    distance = (convert_speed * convert_speed) / (2 * FRICTION_COE * ACCELERATION)

    print(f"At {initial_speed} miles per hour, with {tire_name}, the car will stop in", "{:.2f}".format(distance), "feet.")



#This is the main menu of the code. 

if __name__ == "__main__":
    sentinel = 4 #variable "sentinel" is used to indicate that the program will stop running when the user presses 4. 

    while sentinel == 4:
        print("Main menu:")
        print("1. Cost of Fuel")
        print("2. Used Value")
        print("3. Stopping Distance")
        print("4. Quit")

        #The user can input any numbers as long as it's from 1-4 to go to a certain function.
        #If the user enters a number that is outside of the range of 1-4, then the program will continually ask the user to input
        #a number until they enter a number from 1-4.
        user_input = float(input("Choose a function:"))

        while (user_input < 0) or (user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4):
            user_input = float(input("Choose a function:"))


        #When the user enters a number from 1-4, different functions would get called depending on what number the user inputs.
        #Once the function finshes running, the program will print out the main menu again.
        if user_input == 1:
            cost_of_fuel()

        elif user_input == 2:
            used_value()

        elif user_input == 3:
            stopping_distance()

        #When the user enters 4, the program will stop running.
        elif user_input == 4:
            quit() 
