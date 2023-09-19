import math
import numpy
from utils import *

def sum_vc(vector):
    """Retorna o somatório de um vetor."""
    return sum(vector)

def mean(vector):
    """Retorna a média aritmética de um vetor."""
    return sum_vc(vector)/len(vector)

def sqsum(vector):
    """Retorna o somatório dos quadrados dos elementos de um vetor."""
    s = 0
    for i in range(len(vector)):
        s += pow(vector[i], 2)
    return s

def stdev(vector):
    """Retorna a raiz quadrada do somatório do vetor ao quadrado"""
    return math.sqrt(sqsum(vector))

def operatorMinus(vector, numSubtraction):
    """Retorna um vetor com os índice subtraídos pelo 'numSubtraction'"""
    vectorCopy = vector[:]
    for i in range(len(vector)):
        vectorCopy[i] = vector[i] - numSubtraction
    return vectorCopy

def operatorMultiplication(vector, numMultiplication):
    """Retorna um vetor com os índice multiplicados pelo 'numMultiplication'"""
    vectorCopy = vector[:]

    for i in range(0, len(vector)):
        vectorCopy[i] = vector[i] * numMultiplication[i]
    return vectorCopy

def pearsonCoeff(vectorA, vectorB): 
    """Calcula o coeficiente de correlação de Pearson entre dois vetores, varia de -1 (negativa) a 1 (positiva), com 0 indicando ausência de correlação linear."""
    
    mean_A, mean_B = mean(vectorA), mean(vectorB)
    dif_A, dif_B = operatorMinus(vectorA, mean_A), operatorMinus(vectorB, mean_B)
    multiplication = operatorMultiplication(dif_A, dif_B)
    try:
        pearson = abs((sum_vc(multiplication))/(stdev(dif_A)*stdev(dif_B)))
    except ZeroDivisionError:
            return 0.00000001 #divisão por zero

    return pearson

def binaryVector(k, vector): 
    """Percorre o "vector" e retorna um vetor binario para o k referenciado"""
    binary_vector = [0 for i in range(len(vector))]
    for i in range(len(vector)):
        if (vector[i] == k):
            binary_vector[i] = 1
    return binary_vector

def pearsonCoeff_cat_num(vectorA, vectorB):  #correlação de Pearson
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
    """Calcula e retorna a probabilidade de que dois vetores binários, tenham o mesmo valor no mesmo índice."""
    sum_A_B = 0
    for i in range(len(vectorA)):
        if vectorA[i] == 1 and vectorB[i] == 1:
            sum_A_B += 1
    return sum_A_B / len(vectorA)

def pearsonCoeff_cat_cat(vectorA, vectorB):
    """Calcula a correlação entre dois atributos categoricos. 
    
    - Muito bom 1--0 Muito ruim"""
    sum_cat_cat = 0 
    pearson = 0
    dist_A, dist_B = distinct(vectorA), distinct(vectorB)
    
    for i in range(len(dist_A)):
        binary_A = binaryVector(dist_A[i], vectorA)
        
        for j in range(len(dist_B)):
            binary_B = binaryVector(dist_B[j], vectorB)
            probability = prob_a_and_b(binary_A, binary_B)
            pearson = pearsonCoeff(binary_A, binary_B)
            sum_cat_cat += (probability*abs(pearson))
    return sum_cat_cat








