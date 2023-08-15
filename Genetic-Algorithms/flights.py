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

print(flights)