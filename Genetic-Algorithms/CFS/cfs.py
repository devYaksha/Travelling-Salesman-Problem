import math
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
    """Retorna um vetor com os elementos multiplicados por 'numMultiplication'."""
    vectorCopy = vector[:]
    for i in range(len(vector)):
        vectorCopy[i] = vector[i] * numMultiplication[i]
    return vectorCopy

def pearsonCoeff(vectorA, vectorB):
    """Calcula o coeficiente de correlação de Pearson entre dois vetores, varia de -1 (negativa) a 1 (positiva), com 0 indicando ausência de correlação linear."""
    
    mean_A, mean_B = mean(vectorA), mean(vectorB)
    dif_A, dif_B = operatorMinus(vectorA, mean_A), operatorMinus(vectorB, mean_B)
    product_AB = sum_vc(operatorMultiplication(dif_A, dif_B))
    stdev_A, stdev_B = stdev(dif_A), stdev(dif_B)
    
    try:
        pearson = product_AB / (stdev_A * stdev_B)
    except ZeroDivisionError:
        return 0.00000001  # Divisão por zero
    
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


def possible_class_hierarchy(a_class, dist_class):
    """
    A função itera sobre as classes distintas e constrói um vetor de classes possíveis
    na hierarquia. O resultado é ordenado.

    Args:
    - a_class: Não é usado na função.
    - dist_class: Um vetor de strings que contém classes distintas.

    Return:
    - List
"""
    possible_class = []
    concate = []
    for i in range(len(dist_class)):
        aux_str = explode(dist_class[i], '.')
        level = len(aux_str)

        for j in range(level):
            if j == 0:
                concate.append(aux_str[j])
            else:
                concate.append("." + aux_str[j])
            possible_c = concate[:]
            if in_array_string(possible_c, possible_class) == -1:
                possible_class.append(possible_c) #se for classe nova, adicona no vector possible_class

        
    possible_class.sort()
    return possible_class


def class_to_vector(a_class, possible_class):
    """
    Esta função recebe uma lista de instâncias de classe e uma lista de hierarquias de classe
    possíveis. Ela gera um vetor binário para cada instância de classe, onde cada elemento
    no vetor corresponde à presença (1) ou ausência (0) de uma hierarquia de classe específica em 'possible_class'.

    Args:
    - a_class: Uma lista de instâncias de classe.
    - possible_class: Uma lista de hierarquias de classe possíveis, gerada por `possible_class_hierarchy()`

    Return:
    - lista de listas, (Matriz): Uma lista de vetores binários representando a ocorrência de classes."""
    occurrence = []
    for i in range(len(a_class)):
        instance_vec = [0]*len(possible_class)
        aux_str = explode(a_class[i], '.')
        for j in range(len(aux_str)):
            current_c = '.'.join(aux_str[:j + 1])
            position = in_array_string(current_c, possible_class)
            if position != -1:
                instance_vec[position] = 1
        occurrence.append(instance_vec)
    return occurrence


def correlation_fl_multilabel(class_vector, data, f_type):
    """
    Cria o vetor de correlacao entre todas as features da base e o atributo classe, considerando cada classe da heirarquia como classe binaria
    """
    correlation = []
    tam_class_vector = len(class_vector[0])
    tam_features = len(data[0])

    for k in range(tam_features):
        feature = get_column(data,k)
        sum_correlation = 0

        if f_type[k] == 1:
            for i in range(tam_class_vector):
                label = get_column(class_vector, i)
                pearson = pearsonCoeff(feature, label)
                sum_correlation += abs(pearson)

        else:
            for i in range(tam_class_vector):
                label = get_column(class_vector, i)
                pearson = pearsonCoeff_cat_num(feature, label)
                sum_correlation += abs(pearson)

        pearson_normal = sum_correlation/tam_class_vector
        correlation.append(pearson_normal)
        
    return correlation

def class_level(possible_class):
    """percorre o vetor de classes possiveis e retorna um vetor de mesmo tamanho com o nivel da classe"""
    level_vector = []
    for i in range(len(possible_class)):
        aux_str = explode(possible_class[i], '.')
        level_vector.append(len(aux_str))
    return level_vector

def classes_per_level(max_level, possible_class_level):
    """percorre o vetor de classes possiveis e retorna um vetor com o total de classes por nivel da hierarquia"""
    total_classes_per_level = [0 for i in range(max_level)]
    for i in range(len(possible_class_level)):
        total_classes_per_level[possible_class_level[i]-1] += 1
    
    return total_classes_per_level




def correlation_fl_hierarchical(class_vec, data, f_type, class_level, w_0, classes_per_level):
    tam_class_vec = len(class_vec[0])
    tam_features = len(data[0])
    sum_weight = 0
    correlation = []

    for k in range(len(classes_per_level)):
        sum_weight += (pow(w_0, k+1)*classes_per_level[k])

    for k in range(tam_features):
        feature = get_column(data,k)
        sum_correlation = 0

        if f_type[k] == 1:
            for i in range(tam_class_vec):
                label = get_column(class_vec, i)
                pearson = pearsonCoeff(feature, label)
                sum_correlation += abs(pearson)*(pow(w_0, class_level[i]))
        else: 
            for i in range(tam_class_vec):
                label = get_column(class_vec, i)
                pearson = pearsonCoeff_cat_num(feature, label)
                sum_correlation += abs(pearson)*(pow(w_0, class_level[i]))

        pearson_normal = sum_correlation/sum_weight
        correlation.append(pearson_normal)

    return correlation

def correlation_f_to_f_vec(data, f_type):
    correlation_matrix = []
    
    tam_features = len(data[0])
    
    for k in range(tam_features - 1):
        correlation = [] #reseta a cada iteração
        for j in range(k + 1, tam_features):
            if f_type[k] == 1 and f_type[j] == 1:  # numerico e numerico
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff(f1, f2)
                correlation.append(pearson)
            elif f_type[k] == 1 and f_type[j] == 2:  # numerico e categorico
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff_cat_num(f2, f1)
                correlation.append(pearson)
            elif f_type[k] == 2 and f_type[j] == 1:  # categorico e numerico
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff_cat_num(f1, f2)
                correlation.append(pearson)
            else:  # categorico e categorico
                f1 = get_column(data, k)
                f2 = get_column(data, j)
                pearson = pearsonCoeff_cat_cat(f1, f2)
                correlation.append(pearson)
        
        correlation_matrix.append(correlation)
    
    return correlation_matrix



def merit_cfs(s, correlation_ff_mat, correlation_fl_vec):
    merit = []
    sum_correlation_ff = 0
    sum_correlation_fl = 0
    att_vec = s
    tam_features = len(att_vec)

    att_vec.sort()  # Atributos ordenados de maneira crescente

    for k in range(tam_features - 1):
        for j in range(k + 1, tam_features):
            sum_correlation_ff += correlation_ff_mat[att_vec[k]][att_vec[j] - att_vec[k] - 1]

    for k in range(tam_features):
        sum_correlation_fl += correlation_fl_vec[att_vec[k]]

    merit_denominator = pow((tam_features + (tam_features *(tam_features - 1) * sum_correlation_ff)), 0.5)

    if math.isnan(merit_denominator):
        merit_denominator = 0.00000001

    merit_value = (tam_features * sum_correlation_fl)/(merit_denominator)
    merit.append(merit_value)

    return merit


