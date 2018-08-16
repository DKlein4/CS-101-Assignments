'''
CS 101
Klein.Dustin-Program4
Assignment 4
Dustin Klein
dbktgb@mail.umkc.edu
Problem: Find all of the meteorite hits within a radius
Algorithm:
•	Get user input – for all verify they are valid
o	Name of the input file
o	Name of the output file
o	Latitude and longitude
o	Radius
•	Open input, output file
•	Get all of the meteorites that are within the radius
    𝑑𝑒𝑙𝑡𝑎𝐿𝑜𝑛𝑔 = 𝑙𝑜𝑛𝑔2 − 𝑙𝑜𝑛𝑔1 𝑑𝑒𝑙𝑡𝑎𝐿𝑎𝑡 = 𝑙𝑎𝑡2 − 𝑙𝑎𝑡1 𝑎 = (𝑠𝑖𝑛(𝑑𝑒𝑙𝑡𝑎𝐿𝑎𝑡/2)) 2 + 𝑐𝑜𝑠(𝑙𝑎𝑡1) ∗ 𝑐𝑜𝑠(𝑙𝑎𝑡2) ∗ (𝑠𝑖𝑛(𝑑𝑒𝑙𝑡𝑎𝐿𝑜𝑛𝑔/2)) 2 𝑐 = 2 ∗ 𝑎𝑡𝑎𝑛2(√𝑎, √1 − 𝑎) 𝑑 = 3961 ∗ 𝑐 # 3961 𝑖𝑠 𝑡ℎ𝑒 𝑟𝑎𝑑𝑖𝑢𝑠 𝑜𝑓 𝑡ℎ𝑒 𝑒𝑎𝑟𝑡ℎ 𝑖𝑛 𝑚𝑖𝑙𝑒
•	Write them to the output file
•	Close input, output file
•	Ask if the user would like to go again

'''

import math

def getInputFile():
    # Gets the input file and open it

    input_file_is_open = False
    while not input_file_is_open:
        input_file_name = input("Enter the name of the Meteorite file to read. ")

        try:
            input_file = open(input_file_name, "r", encoding="utf-8")
            input_file_is_open = True
            print()
            return input_file
        except:
            print("Could not open the file specified. Please choose again.\n")

def getOutputFile():
    # Gets the output file and open it

    output_file_is_open = False
    while not output_file_is_open:
        output_file_name = input("Enter the name of the file to output to. ")
        try:
            output_file = open(output_file_name, "w", encoding="utf-8")
            output_file_is_open = True
            print()
            return output_file
        except:
            print("Could not open the file specified. Please choose again.\n")

def closeFiles():
    #Closes the files

    input_file.close()
    output_file.close()

def getCoords():
    # Gets the latitude and longitude from the user and returns them as lat, long

    input_is_valid = False
    while not input_is_valid:
        coord = input("Enter the lat and long of the source point separated by a comma eg 20, 30. ")
        coord = coord.split(",")

        #Verifys that the input us seperated by a comma
        if len(coord) == 2:
            try:
                #Verifys both inputs are nunmbers
                for i in range(len(coord)):
                    coord[i] = float(coord[i].strip())

                #Verifys the numbers are within the valid range
                if coord[0] < -90 or coord[0] > 90:
                    print("The latitude must be between -90 and 90\n")
                elif coord[1] < -180 or coord[1] > 180:
                    print("The longitude must be between -180 and 180\n")
                else:
                    input_is_valid = True
            except ValueError:
                print("Both values must be floating point.\n")

        else:
            print("You must enter the latitude and longitude seperated by a comma. \n")

    lat = coord[0]
    long = coord[1]

    return lat, long

def getRadius():
    # Gets the radius from the user

    input_is_valid = False
    while not input_is_valid:
        radius = input("\nEnter the number of miles from the source to find meteors for. ")
        try:
            radius = float(radius)

            if radius <= 0:
                print("You must enter a number greater than 0.\n")
            else:
                input_is_valid = True
        except ValueError:
            print("You must enter a number.\n")


    return radius

def getDistance(lat1, lon1, lat2, lon2):
    #Converts degrees to radians
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)

    #Math
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 3961 * c

    return d

def findMeteorites(input_file, output_file, user_lat, user_long, radius):
    # find all of the meteorites within the radius and writes them to a file

    header = input_file.readline()
    print(header, file=output_file)

    #For each line after the header
    for line in input_file:
        #Pick out the latitude and longitude
        lat = line[135:150].strip()
        long = line[150:165].strip()

        #If lat or long don't have a value, skip otherwise check their values
        if lat == "" or long == "":
            pass
        else:
            lat = float(lat)
            long = float(long)

            distance = getDistance(user_lat, user_long, lat, long)
            if distance < radius:
                print(line, file=output_file)

def continuePlaying():
    input_is_valid = False
    while not input_is_valid:
        cont = input("\nDo you want to run the meteorite program again? Y/YES/N/NO. ")
        cont = cont.lower()
        valid_inputs = ["yes", "y", "no", "n"]

        if cont not in valid_inputs:
            print("You must enter Y, YES, N, or NO.\n")
        else:
            input_is_valid = True

    if cont == "y" or cont == "yes":
        return True
    else:
        return False

continue_playing = True
while continue_playing:

    input_file = getInputFile()
    output_file = getOutputFile()

    user_lat, user_long = getCoords()

    radius = getRadius()

    findMeteorites(input_file, output_file, user_lat, user_long, radius)

    closeFiles()

    continue_playing = continuePlaying()
