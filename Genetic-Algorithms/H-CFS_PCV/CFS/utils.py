def in_array(value, vector):
    """Verifica se o 'value' esta no 'vector'.
    
    Returns:
        vectorType: Retorna um valor do tipo do vetor caso esteja na lista, ou -1 caso não esteja na lista
    
    """
    for i in range(len(vector)):
        if value == vector[i]:
            return i
    return -1 #nao esta no vector


def distinct(categorical):
    """Recebe uma lista de valores categóricos e retorna uma lista de valores distintos"""
    vector_distinct = [categorical[0]]
    for i in range(1, len(categorical)):
        if in_array(categorical[i], vector_distinct) == -1:
            vector_distinct.append(categorical[i])

    return vector_distinct

def frequence_double(dist_class, vector_categorical):
    """
    Calcula a frequência de ocorrência de elementos do vetor categórico em relação a uma distribuição de classes.

    Args:
        dist_class (list): Uma lista que representa a distribuição de classes, contendo os valores possíveis.
        vector_categorical (list): Uma lista de elementos categóricos para os quais a frequência será calculada.

    Returns:
        list: Uma lista contendo a frequência de ocorrência de cada elemento de 'vector_categorical' em relação a 'dist_class'.
        
    """
    frequence = [0 for i in range(len(dist_class))]
    for k in range(len(vector_categorical)):
        position = in_array(vector_categorical[k], dist_class)
        frequence[position] += 1
    
    return frequence
