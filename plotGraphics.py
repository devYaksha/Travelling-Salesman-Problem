import matplotlib.pyplot as plt
from cities import *

def grafico_pontos(melhor_vetor_global, dictionary_Cities):
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
        
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    
    # Adicione um título ao gráfico
    plt.title('Traçado de Linhas entre Pontos')
    plt.legend()
    plt.show()

def gerar_grafico(vetorFitness, num_geracoes, melhor_global):
   plt.plot(range(num_geracoes + 1), vetorFitness)
   plt.title(f"Fitness: {melhor_global:.2f}")
   plt.xlabel("Iterações")
   plt.ylabel("Fitness")
   plt.show()
   