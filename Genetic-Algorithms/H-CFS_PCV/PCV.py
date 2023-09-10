#Cidade A: (0, 0) -> 1
#Cidade B: (2, 4) -> 2
#Cidade C: (5, 2) -> 3
#Cidade D: (7, 7) -> 4
#Cidade E: (1, 6) -> 5

import random
import math 
import matplotlib.pyplot as plt


dictionary_Cities = {
    1: (0,0), #a
    2: (2,4), #b
    3: (5,2), #c
    4: (7,7), #d
    5: (1,6)  #e
}

def criar_cromossomo():
    cromossomo = []
    genesPossiveis = [i+1 for i in range(len(dictionary_Cities))]
    for i in range(len(dictionary_Cities)):
      gene = random.choice(genesPossiveis)
      if gene not in cromossomo:
         cromossomo.append(gene)
         index = genesPossiveis.index(gene) 
         genesPossiveis.pop(index)
    return cromossomo

def criar_populacao(tamanho_populacao):
   populacao = [criar_cromossomo() for i in range(tamanho_populacao)]
   return populacao


def fitness_cromossomo(cromossomo): #Calcula a distancia entre dois pontos utilizando a função: #dAB = sqrt((xB – xA)² + (yB – yA)²) 
   
   cordenadas = []
   for i in range(len(cromossomo)):
      cordenada_gene = dictionary_Cities[cromossomo[i]]
      cordenadas.append(cordenada_gene) #armazena em um vetor de coordenadas


   fitness = 0

   for j in range(len(cordenadas)-1):
      xb_xa = pow(cordenadas[j+1][0] - cordenadas[j][0], 2) 
      yb_ya = pow(cordenadas[j+1][1] - cordenadas[j][1], 2)
      fitness += math.sqrt(xb_xa + yb_ya)
    
   return fitness
   
def fitness_populacao(populacao):
   fitness = [fitness_cromossomo(populacao[i]) for i in range(len(populacao))] #repete o processo para n populacao
   return fitness
   

def pmx_crossover(parent1, parent2):

    point1, point2 = sorted(random.sample(range(len(parent1)), 2))

    # filhos em branco
    offspring1 = [None] * len(parent1)
    offspring2 = [None] * len(parent2)

    #copia os genes entre o corte de dois pontos
    offspring1[point1:point2 + 1] = parent1[point1:point2 + 1]
    offspring2[point1:point2 + 1] = parent2[point1:point2 + 1]

    # Fill in the remaining genes in offspring1 and offspring2 using PMX
    for i in range(len(parent1)):
        if point1 <= i <= point2:
            continue 
        else:
            # Find a mapping from parent2 for the current gene in offspring1
            mapping = parent2[i]
            while mapping in offspring1[point1:point2 + 1]:
                index = parent1.index(mapping)
                mapping = parent2[index]
            offspring1[i] = mapping

            # Repeat the process for offspring2
            mapping = parent1[i]
            while mapping in offspring2[point1:point2 + 1]:
                index = parent2.index(mapping)
                mapping = parent1[index]
            offspring2[i] = mapping

    return offspring1, offspring2


def crossover(populacao):
   novos_cromossomos = []
   for i in range(len(populacao)-1):
        crossover_chance = random.randint(1,10)
        if crossover_chance > 2:
            filho1, filho2 = pmx_crossover(populacao[i], populacao[i+1])
            novos_cromossomos.append(filho1)
            novos_cromossomos.append(filho2)
   
   return novos_cromossomos
        

def definir_sobreviventes(populacao, populacao_filha): #por torneio https://www.youtube.com/watch?v=NFVng_313b4&ab_channel=Ren%C3%A9GarganoFerrari

   populacao_final = []
   if len(populacao_filha) == 0:
      populacao_final = populacao
      return populacao_final

   
   k = 0.1
   for i in range(len(populacao)):

      primeiroR = random.choice(populacao)
      segundoR = random.choice(populacao_filha)
      fitness_primeiroR = fitness_cromossomo(primeiroR)
      fitness_segundoR = fitness_cromossomo(segundoR)

      if fitness_primeiroR <= fitness_segundoR:
         melhor_cromossomo = primeiroR
         pior_cromossomo = segundoR
      else:
         melhor_cromossomo = segundoR
         pior_cromossomo = primeiroR
         

      r = random.randint(0,1)
      if r > k:
         populacao_final.append(melhor_cromossomo)
      else:
         populacao_final.append(pior_cromossomo)

   return populacao_final

def fitness(populacao):
   melhorIndividuo = fitness_populacao(populacao)
   fitnessX = melhorIndividuo[0]
   for i in range(len(melhorIndividuo)):
      if melhorIndividuo[i] < fitnessX:
         fitnessX = melhorIndividuo[i]
   
   return fitnessX


def gerar_grafico(vetorFitness, num_geracoes):
   plt.plot(range(num_geracoes), vetorFitness)
   plt.title("Gráfico")
   plt.xlabel("Iterações")
   plt.ylabel("Fitness")
   plt.show()
  
def algoritmo_genetico(tamanho_populacao, numero_geracoes):
   populacao = criar_populacao(tamanho_populacao)
   fitness_melhor = []

   for i in range(numero_geracoes):
        populacao_filha = crossover(populacao)
        populacao = definir_sobreviventes(populacao, populacao_filha)
        melhor_fitness = fitness(populacao)
        fitness_melhor.append(melhor_fitness)

   
   gerar_grafico(fitness_melhor, numero_geracoes)

# Exemplo de uso:
tamanho_populacao = 10
numero_geracoes = 100
algoritmo_genetico(tamanho_populacao, numero_geracoes)