'''
CS 101
Klein.Dustin-Program3
Assignment 3
Dustin Klein
dbktgb@mail.umkc.edu
Problem: Create an algorithm that mutates random strings into a target string
Algorithm:
•	Create string to be matched
•	Generate 500 random strings
o	Store them in a list
•	Find the fitness score for each string and remember the best fitness
•	Find the average fitness and get rid of the strings that are less than average
•	Get the population back up to 500 with mutated strings
o	For mutation, each character has a 1% chance to mutate
•	Repeat this process until the best fitness is 0
'''
import random
#Create string to be matched
origin = "This is the String"

population = []
breeding_population = []

temp_string = ""
child_string = ""

best_fitness = 99999
best_string = ""

temp_fitness = 0
total_fitness = 0

#Generate 500 random strings
for i in range(500):
    for j in range(18):
        temp_string += chr(random.randint(32, 126))
        j+=1
    population.append(temp_string)
    temp_string=""
print("Starting population generated")

while best_fitness != 0:
    #Find the fitness score for each string and remember the best fitness
    for i in range(500):
        for j in range(18):
            temp_fitness += abs(ord(population[i][j]) - ord(origin[j]))
        total_fitness += temp_fitness
        if temp_fitness < best_fitness:
            best_fitness = temp_fitness
            best_string = population[i]
        temp_fitness = 0
    print("Best fit so far:", best_string, "Score:", best_fitness)

    #Find the average fitness
    average = total_fitness/500

    #Get rid of the strings that are less than average
    for i in range(500):
        for j in range(18):
            temp_fitness += abs(ord(population[i][j]) - ord(origin[j]))
        if temp_fitness < average:
            breeding_population.append(population[i])
        temp_fitness = 0


    #Get the population back up to 500 with mutated strings
    for i in range(500 - len(breeding_population)):
        parent1 = random.choice(breeding_population)
        parent2 = random.choice(breeding_population)

        for j in range(18):
            if random.random() < 0.50:
                child_string += parent1[j]
            else:
                child_string += parent2[j]

        breeding_population.append(child_string)
        child_string = ""

    population = breeding_population

    mutated_population = []

    for i in range(500):
        for j in range(18):
            if random.random() < 0.01:
                if random.random() < 0.50:
                    temp_string += chr(ord(population[i][j]) - 1)
                else:
                    temp_string += chr(ord(population[i][j]) + 1)
            else:
                temp_string += population[i][j]

        mutated_population.append(temp_string)
        temp_string = ""

    population = mutated_population

    total_fitness = 0