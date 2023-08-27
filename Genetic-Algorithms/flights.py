import time
import random
import math
import sys
import os

people = [('Lisbon', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Brussels', 'BRU'),
           ('London', 'LHR')]

Finaldestiny = 'FCO' #Rome

#flights = {('BRU', 'FCO'): ['15:44', '18:55', 382]}
#print(flights['BRU', 'FCO'])[0]                                TESTES
#print (f"Directory: {os.getcwd()}")                            


flights = {}
for linha in open('./Genetic-Algorithms/flights.txt', 'r'):
    origin, destiny, departureTime, arrivalTime, value = linha.split(',')
    flights.setdefault((origin, destiny), [])
    flights[(origin, destiny)].append((departureTime, arrivalTime, value))

def printCalendar(calendar):
    fly_id = -1
    totalPrice = 0
    for i in range(len(calendar)//2):
        name = people[i][0]
        origin = people[i][1]
        fly_id += 1
        fly_departure = flights[(origin, Finaldestiny)][calendar[fly_id]]
        print(name)
        print(fly_departure)
        totalPrice += int(fly_departure[2])
        fly_id += 1
        fly_back = flights[(destiny, origin)][calendar[fly_id]]
        totalPrice += int(fly_back[2])
        print('%10s%10s %5s-%5s U$%3s %5s-%5s U$%3s' % (name, origin, fly_departure[0], fly_back[1], fly_departure[2], 
                                                    fly_back[0], fly_back[1], fly_back[2]))
    print('Preço total: ', totalPrice)


#printCalendar([1,4, 3,2, 7,3, 6,3, 2,4, 5,3])



def get_minutes(hora):
    t = time.strptime(hora, '%H:%M')
    minutes = t[3]*60 + t[4]
    return minutes


print(get_minutes('10:32'))