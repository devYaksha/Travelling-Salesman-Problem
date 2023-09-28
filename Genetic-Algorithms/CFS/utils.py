def in_array(value, vector):
    """Verifica se o 'value' esta no 'vector'"""
    for i in range(len(vector)):
        if value == vector[i]:
            return i
    return -1


def distinct(categorical):
    """Recebe uma lista de valores categóricos e retorna uma lista de valores distintos"""
    vector_distinct = [categorical[0]]
    for i in range(1, len(categorical)):
        if in_array(categorical[i], vector_distinct) == -1:
            vector_distinct.append(categorical[i])

    return vector_distinct

def frequence_double(dist_class, vector_categorical):
    """Calcula a frequência de ocorrência de elementos do vetor categórico em relação a uma distribuição de classes."""
    frequence = [0 for i in range(len(dist_class))]
    for k in range(len(vector_categorical)):
        position = in_array(vector_categorical[k], dist_class)
        frequence[position] += 1
    
    return frequence

def explode(input_str, delimiter):
    """Recebe uma input_string e a 'quebra' e retorna em um vetor de pequenas sub-strings baseado no caractere delimitador"""
    out = []
    start = 0
    found = input_str.find(delimiter)

    while found != -1:
        sub_str = input_str[start:found]
        out.append(sub_str)
        start = found + 1
        found = input_str.find(delimiter, start)

    # Adiciona a ultima sub-string
    out.append(input_str[start:])

    return out

def in_array_string(v_class, vectorA):
    """Verifica se v_class está contida no vectorA, retornando sua posição."""
    for i in range(len(vectorA)):
        if v_class == vectorA[i]:
            return i
    
    return -1

def get_column(matrix, k):
    vector = []
    for j in range(len(matrix)):
        vector.append(matrix[j][k])
    return vector


