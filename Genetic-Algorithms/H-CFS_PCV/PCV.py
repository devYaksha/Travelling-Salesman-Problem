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
   5: (1,6),  #e
   6: (3, 1), #f
   7: (6, 3), #g
   8: (4, 5), #h
   9: (8, 6), #i
   10: (2, 3), #j
   11: (9, 9), #k
   12: (3, 7), #l
   13: (6, 1), #m
   14: (0, 5), #n
   15: (5, 5), #o
   16: (8, 2), #p
   17: (1, 2), #q
   18: (4, 6), #r
   19: (7, 4), #s
   20: (2, 1) #t
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
   
   #print(cromossomo)
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

    # PreenchE os genes restantes no filho1 e no filho2 usando PMX
    for i in range(len(parent1)):
        if point1 <= i <= point2:
            continue 
        else:
            # Encontre um mapeamento do pai2 para o gene atual filho1
            mapping = parent2[i]
            while mapping in offspring1[point1:point2 + 1]:
                index = parent1.index(mapping)
                mapping = parent2[index]
            offspring1[i] = mapping

            # Repete o processo pro filho 2
            mapping = parent1[i]
            while mapping in offspring2[point1:point2 + 1]:
                index = parent2.index(mapping)
                mapping = parent1[index]
            offspring2[i] = mapping

    return offspring1, offspring2

def crossover(populacao):
   novos_cromossomos = []
   for i in range(0, len(populacao)-1, 2):
        crossover_chance = random.randint(1,10) #repete o processo de pmx para todos os filhos-1
        if crossover_chance > 2:
            filho1, filho2 = pmx_crossover(populacao[i], populacao[i+1])
            novos_cromossomos.append(filho1)
            novos_cromossomos.append(filho2)
        else:
         filho1, filho2 = populacao[i], populacao[i+1]
         novos_cromossomos.append(filho1)
         novos_cromossomos.append(filho2)
   
   return novos_cromossomos
        
def melhor_individuo(vetor_fitness, populacao):
   melhor_fitness = vetor_fitness[0]
   pior_fitness = melhor_fitness
   pior_cromossomo = populacao[0]
   melhor_cromossomo = populacao[0]

   for i in range(len(vetor_fitness)):
      if vetor_fitness[i] < melhor_fitness:
          melhor_fitness = vetor_fitness[i]
          melhor_cromossomo = populacao[i]

      if vetor_fitness[i] > pior_fitness:
          pior_fitness = vetor_fitness[i]
          pior_cromossomo = populacao[i]

   return melhor_fitness, melhor_cromossomo, pior_fitness, pior_cromossomo     

def torneio(populacao, tamanho_da_luta):
    populacao_final = []
    lutadores = []
    
    k = 0.6
    for i in range(len(populacao)):
      for j in range(tamanho_da_luta):
          lutadores.append(random.choice(populacao))
      r = random.random()  # valor entre 0 e 1
      fitness = fitness_populacao(lutadores)
      
      melhor_fitness, melhor_cromossomo, pior_fitness, pior_cromossomo = melhor_individuo(fitness,lutadores)

      if r < k:
          populacao_final.append(melhor_cromossomo)
      else:
          populacao_final.append(pior_cromossomo)

    return populacao_final
 
def mutacao_cromossomo(cromossomo,taxa_mutacao):
    novo_cromossomo = cromossomo[:]  # Crie uma cópia do cromossomo original

    if random.random() < taxa_mutacao:  # Probabilidade de 5% de mutação
        indices = random.sample(range(len(cromossomo)), 2)
        index1, index2 = indices[0], indices[1]
        novo_cromossomo[index1], novo_cromossomo[index2] = novo_cromossomo[index2], novo_cromossomo[index1]

    return novo_cromossomo

def mutacao(populacao,taxa_mutacao):
    novo_mutante = [mutacao_cromossomo(cromossomo,taxa_mutacao) for cromossomo in populacao]
    return novo_mutante

def gerar_grafico(vetorFitness, num_geracoes, melhor_global):
   plt.plot(range(num_geracoes + 1), vetorFitness)
   plt.title(f"Fitness: {fitness_cromossomo(melhor_global):.2f}")
   plt.xlabel("Iterações")
   plt.ylabel("Fitness")
   plt.show()
   
def grafico_pontos(melhor_vetor_global):
    # Descompacte a lista de pontos em listas separadas para x e y
    cordenadas = []
    print(melhor_vetor_global)
    for i in range(len(melhor_vetor_global)):
      cordenada_gene = dictionary_Cities[melhor_vetor_global[i]]
      cordenadas.append(cordenada_gene)
    x_points, y_points = zip(*cordenadas)
    
    plt.scatter(x_points, y_points, label='Pontos', color='b', marker='o')
    
    # Traçar linhas entre os pontos consecutivos no vetor
    for i in range(len(cordenadas) - 1):
        x1, y1 = cordenadas[i]
        x2, y2 = cordenadas[i + 1]
        plt.plot([x1, x2], [y1, y2], color='r')
    
    # Adicione rótulos aos eixos x e y
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    
    # Adicione um título ao gráfico
    plt.title('Traçado de Linhas entre Pontos')
    
    # Exiba a legenda
    plt.legend()
    
    # Mostrar o gráfico
    plt.show()
def algoritmo_genetico(tamanho_populacao, numero_geracoes, tamanho_torneio, taxa_mutacao):

   populacao = criar_populacao(tamanho_populacao)
   fitness = fitness_populacao(populacao)
   melhor_fitness_global, melhor_individuo_global, pior_fitness, pior_cromossomo = melhor_individuo(fitness, populacao)

   melhor_vetor_global = []
   melhor_vetor_global.append(melhor_fitness_global)

   for i in range(numero_geracoes):
        populacao = torneio(populacao, tamanho_torneio)
        populacao = crossover(populacao)
        populacao = mutacao(populacao,taxa_mutacao)

        populacao[random.randint(0, len(populacao)-1)] = melhor_individuo_global
        fitness = fitness_populacao(populacao)
        melhor_fitness_global, melhor_individuo_global, pior_fitness, pior_cromossomo  = melhor_individuo(fitness, populacao)
        melhor_vetor_global.append(melhor_fitness_global)

   gerar_grafico(melhor_vetor_global, numero_geracoes, melhor_individuo_global)
   grafico_pontos(melhor_individuo_global)

# Exemplo de uso:
tamanho_populacao = 250
numero_geracoes = 50
taxa_mutacao = 0.8
tamanho_torneio = 5

algoritmo_genetico(tamanho_populacao, numero_geracoes,tamanho_torneio, taxa_mutacao)

#39.7
#39.14
#40.17
#40.46

#37.26