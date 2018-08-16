'''
CS 101
Klein.Dustin-Program2
Assignment 2
Dustin Klein
dbktgb@mail.umkc.edu
Problem: Make a 10 day simulation of a shave ice stand.
Algorithm:
•	Print: Day day you have $ money in the bank
o	Where day is the day of the simulation from one to ten
o	money is the amount of money they have. Defaulted to five
•	Print: It is precipitation and the temperature is temp degrees.
o	Precipitation is clear or rainy. 10% chance for rain
o	Temp is the temperature. A number randomly generated from 70-110
•	Ask how many cones the user would like to make
o	Verify it is a valid input
	Greater than 0
	They have enough money for that number of cones
•	Ask the price the user would like to charge
o	Verify it is a valid input
	Greater than 0
o	Take away from total money
•	Print how many cones the user made and how much it will cost them
•	Print: You sold num_sold taking in $ gross_income for a daily profit/loss of net_income
o	max_customers is a randomly generated number depending on the weather and temp
	Cannot sell more cones than were made
o	Gross_income is num_sold * price of the cones
o	Net_income is gross_income – cost of the cones
•	Add net_income to total money
•	If total money < 50 cents shut down the simulation
•	Repeat this process from day 1 – day 10
•	Ask the user if they would like to go again
o	Verify valid input of Y, YES, N, NO
•	If yes, start the simulation over with $5.00 total money
'''

import random

day = 0
money = 5
cones_made = -1
cost_cones = 9999999
price_cones = -1
max_customers = 0
max_sold = 0
continue_playing = True

while continue_playing:
    print("Welcome to the Shave Ice Stand. Good luck in your new business.\n")

    #Repeat this process from day 1 – day 10
    while day<10:
        day+=1
        # Print: Day day you have $ money in the bank
        print("Day", day, "you have $", money, "in the bank")


        #Precipitation is clear or rainy. 10% chance for rain
        precip_chance = random.randint(0,100)
        if precip_chance<10:
            weather="rainy"
        else:
            weather="clear"
        #emp is the temperature. A number randomly generated from 70-110
        temp = random.randint(70,110)
        #Print: It is precipitation and the temperature is temp degrees.
        print("It is", weather, "and the temperature is", temp, "degrees")


        #Verify it is a valid input-
        #Greater than 0
        #They have enough money for that number of cones
        while cones_made<=0 and cost_cones>money:
            #Ask how many cones the user would like to make
            cones_made = int(input("How many cones of Shave Ice will you make?"))
            if cones_made <= 0:
                print("You must enter a number greater than 0")
            else:
                cost_cones = 0.5 * cones_made
                if cost_cones>money:
                    print("You don't have enough money")
                    cost_cones = 9999999
                    cones_made = -1

        #Verify it is a valid input
        while price_cones<0:
            #Ask the price the user would like to charge
            price_cones = float(input("What price do you charge per cone?"))
            if price_cones<0:
                print("You must enter a number greater than 0")

        #Print how many cones the user made and how much it will cost them
        print("You made", cones_made, "cones of Shave Ice costing", cost_cones)

        #max_customers is a randomly generated number depending on the weather and temp
        max_customers = int((temp - 70) * 0.5/price_cones)
        #Cannot sell more than they have made
        if max_customers < cones_made:
            max_sold = max_customers
        else:
            max_sold = cones_made
        cones_sold = random.randint(0, max_sold)


        #Gross_income is num_sold * price of the cones
        gross_income = cones_sold * price_cones
        #Net_income is gross_income – cost of the cones
        net_income =  gross_income - cost_cones
        print("You sold", cones_sold, "cones taking in $", gross_income, "for a daily profit/loss of", net_income, "\n")
        #Add net_income to total money
        money += net_income

        #If total money < 50 cents shut down the simulation
        if money < 0.5:
            print("You have $", money, "You do not have enough to make any more shave ice.\n")
            break

        #reset variables for the next loop
        cost_cones = 999999
        cones_made = -1
        price_cones = -1


    #Ask the user if they would like to go again
    choice = input("Would you like to play another 10 day simulation?")
    print()
    continue_playing = choice.upper()=="Y" or choice.upper()=="YES"

    #If yes, start the simulation over with $5.00 total money
    day = 0
    money = 5
    max_customers = 0
    max_sold = 0
    cost_cones = 999999
    cones_made = -1
    price_cones = -1

    if not(continue_playing):
        print("Thank you for playing.")