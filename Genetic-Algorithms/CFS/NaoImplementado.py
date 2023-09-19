from cfs import *
import matplotlib.pyplot as plt

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