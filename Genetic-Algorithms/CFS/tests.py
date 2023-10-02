from cfs import *


#Teste das funções do arquivo Utils.py:

"""
#print(in_array_string('A', ['B','C','A'])) #ok
#print(distinct(['A','B','C','D','B','A'])) #ok
#print(frequence_double(["a", "b", "c"], ["a", "b", "c", "a", "b"])) #ok
#print(explode("Teste em python", " ")) #ok
#print(in_array_string("Teste", ['Hello', 'World', 'Teste'])) #ok
"""

#pearsonCoeff Coeficiente de correlação de Pearson:

"""
r = (n * sum_xy - sum_x * sum_y) / (math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)))

Onde:

n é o número de elementos nos dois vetores.
sum_xy é a soma dos produtos dos elementos de x e y correspondentes.
sum_x é a soma dos elementos de x.
sum_y é a soma dos elementos de y.
sum_x2 é a soma dos quadrados dos elementos de x.
sum_y2 é a soma dos quadrados dos elementos de y.

vectorA = [1, 2, 3, 4, 5]   #esperado -1 
vectorB = [-2, -4, -6, -8, -10]

vectorC = [1, 2, 3, 4, 5]
vectorD = [7, 3, 8, 2, 6]    #esperado ausencia de correlação linear

vectorE = [1, 2, 3, 4, 5]
vectorF = [2, 4, 6, 8, 10] #esperado 1  

print(pearsonCoeff(vectorA, vectorB))
print(pearsonCoeff(vectorC, vectorD))
print(pearsonCoeff(vectorE, vectorF))

#Função pearsonCoeff 100%

"""
#pearsonCoeff_cat_num Vetor categórico binário (que será transformado em binário)
"""
vetor_numerico = [1, 0, 1, 0, 1]

vetor_categorico = ["A", "B", "A", "B", "A"]


print(pearsonCoeff_cat_num(vetor_numerico, vetor_numerico))

"""

#pearsonCoeff_cat_cat Calcula a correlação entre dois atributos categoricos.

"""

vetor_categoricoA = ["A", "B", "A", "B", "A"] 
vetor_categoricoB = ["A", "B", "C", "D", "E"]
vetor_categoricoC = ["X", "X", "Y", "X", "X"]
vetor_categoricoD = ["Z", "Z", "Y", "Z", "Z"]


print(pearsonCoeff_cat_cat(vetor_categoricoA, vetor_categoricoB)) #ok
print(pearsonCoeff_cat_cat(vetor_categoricoA, vetor_categoricoC)) #ok
print(pearsonCoeff_cat_cat(vetor_categoricoC, vetor_categoricoD)) #ok

"""

vectorA = ['ABC', 'DEF', 'GHI']

vectorDistinct = possible_class_hierarchy(vectorA)

print(class_to_vector(vectorA, vectorDistinct))