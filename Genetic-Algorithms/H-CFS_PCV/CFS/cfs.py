import math
import numpy
from utils import *

def sum_vc(vector):
    return sum(vector)

def mean(vector):
    return sum_vc(vector)/len(vector)

def sqsum(vector):
    s = 0
    for i in range(len(vector)):
        s += pow(vector[i], 2)
    return s

def stdev(vector):
    """Retorna a raiz quadrada do somatório do vetor ao quadrado"""
    return math.sqrt(sqsum(vector)) 

def operatorMinus(vector, numSubtraction):
    vectorCopy = vector[:]
    for i in range(len(vector)):
        vectorCopy[i] = vector[i] - numSubtraction
    return vectorCopy

def operatorMultiplication(vector, numMultiplication):
    vectorCopy = vector[:]
    for i in range(len(vector)):
        vectorCopy[i] = vector[i] * numMultiplication[i]
    return vectorCopy

def pearsonCoeff(vectorA, vectorB):
    mean_A, mean_B = mean(vectorA), mean(vectorB)
    dif_A, dif_B = operatorMinus(vectorA, mean_A), operatorMinus(vectorB, mean_B)
    multiplication = operatorMultiplication(dif_A, dif_B)
    pearson = abs((sum_vc(multiplication))/(stdev(dif_A)*stdev(dif_B)))

    if numpy.isnan(pearson):
        return 0.00000001 #divisão por zero

    return pearson

def binaryVector(k, vector): 
    """Percorre o "vector" e retorna um vetor binario para o k referenciado"""
    binary_vector = [0 for i in range(len(vector))]
    for i in range(len(vector)):
        if (vector[i] == k):
            binary_vector[i] = 1
    return binary_vector

def pearsonCoeff_cat_num(vectorA, vectorB):  
    """Calcula a correlação entre dois atributos, sendo vectorA categorico, e vectorB numerico"""
    size_vectorA = len(vectorA)
    vector_distinct = distinct(vectorA)
    frequence = frequence_double(vector_distinct, vectorA)

    pearson_sum = 0
    for i in range(len(vector_distinct)):
        binary = binaryVector(vector_distinct[i], vectorA)
        pearson = pearsonCoeff(binary, vectorB)
        pearson_sum += ((frequence[i]/size_vectorA)*abs(pearson))

    return pearson_sum 

def prob_a_and_b(vectorA, vectorB):
    sum_A_B = 0
    for i in range(len(vectorA)):
        if vectorA[i] == 1 and vectorB[i] == 1:
            sum_A_B += 1
    return sum_A_B/(len(vectorA))


teste = [1,2,3]
teste2 = [0,0,1]

print(pearsonCoeff_cat_num(teste, teste2))
