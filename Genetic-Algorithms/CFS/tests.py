from cfs import *


#Utils:

#print(in_array_string('A', ['B','C','A'])) #ok?
#print(distinct(['A','B','C','D','B','A'])) #ok
#print(frequence_double(["a", "b", "c"], ["a", "b", "c", "a", "b"])) #ok
#print(explode("Teste em python", " ")) #ok
#print(in_array_string("Teste", ['Hello', 'World', 'Teste'])) #ok

"""
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