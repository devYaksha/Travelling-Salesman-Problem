import time
import random
import math
import sys

pessoas = [('Lisbon', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Brussels', 'BRU'),
           ('London', 'LHR')]

dominio = [(0, 9)] * (len(pessoas) * 2)
destino = 'FCO' # Roma
voos = {}
for linha in open('flights.txt'):
  origem, destino, partida, chegada, preco = linha.split(',')
  voos.setdefault((origem, destino), [])
  voos[(origem, destino)].append((partida, chegada, int(preco)))

  def imprime_calendario(calendario):
    voo_id = -1
    preco_total = 0
    for i in range(len(calendario) // 2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        voo_id += 1
        voo_ida = voos[(origem, destino)][calendario[voo_id]]
        preco_total += voo_ida[2]
        voo_id += 1
        voo_volta = voos[(destino, origem)][calendario[voo_id]]
        preco_total += voo_volta[2]
        print('%10s%10s %5s-%5s U$%3s %5s-%5s U$%3s' % (nome, origem, voo_ida[0], voo_ida[1], voo_ida[2], 
                                                        voo_volta[0], voo_volta[1], voo_volta[2]))
    print('Preço total: ', preco_total)

def get_minutos(hora):
  t = time.strptime(hora, '%H:%M')
  minutos = t[3] * 60 + t[4]
  return minutos

def funcao_avaliacao(calendario):
  preco_total = 0
  ultima_chegada = 0
  primeira_partida = 1439

  voo_id = -1
  for i in range(len(calendario) // 2):
    origem = pessoas[i][1]
    voo_id += 1
    voo_ida = voos[(origem, destino)][calendario[voo_id]]
    voo_id += 1
    voo_volta = voos[(destino, origem)][calendario[voo_id]]

    preco_total += voo_ida[2]
    preco_total += voo_volta[2]

    if ultima_chegada < get_minutos(voo_ida[1]):
      ultima_chegada = get_minutos(voo_ida[1])
    if primeira_partida > get_minutos(voo_volta[0]):
      primeira_partida = get_minutos(voo_volta[0])


  espera_total = 0
  voo_id = -1
  for i in range(len(calendario) // 2):
    origem = pessoas[i][1]
    voo_id += 1
    voo_ida = voos[(origem, destino)][calendario[voo_id]]
    voo_id += 1
    voo_volta = voos[(destino, origem)][calendario[voo_id]]

    espera_total += ultima_chegada - get_minutos(voo_ida[1])
    espera_total += get_minutos(voo_volta[0]) - primeira_partida

  return espera_total + preco_total


def mutacao(dominio, passo, calendario, probabilidade):
  gene = random.randint(0, len(dominio) - 1)
  mutante = calendario
  if random.random() < probabilidade: 
    if calendario[gene] != dominio[gene][0]:
      mutante = calendario[0:gene] + [calendario[gene] - passo] + calendario[gene + 1:]
    else:
      if calendario[gene] != dominio[gene][1]:
        mutante = calendario[0:gene] + [calendario[gene] + passo] + calendario[gene + 1:]
  return mutante

def crossover(dominio, individuo1, individuo2):
  gene = random.randint(1, len(dominio) - 2)
  return individuo1[0:gene] + individuo2[gene:]

def algoritmo_genetico(dominio, funcao_avaliacao, tamanho_populacao = 100, passo = 1,
                       elitismo = 0.2, numero_geracoes = 500, probabilidade_mutacao = 0.05):
  populacao = []
  for i in range(tamanho_populacao):
    individuo = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
    populacao.append(individuo)
  numero_elitismo = int(elitismo * tamanho_populacao)


  for i in range(numero_geracoes):
    custos = [(funcao_avaliacao(individuo), individuo) for individuo in populacao]
    custos.sort()
    individuos_ordenados = [individuo for (custo, individuo) in custos]
    populacao = individuos_ordenados[0:numero_elitismo] 
    while len(populacao) < tamanho_populacao:
      i1 = random.randint(0, numero_elitismo)
      i2 = random.randint(0, numero_elitismo)
      novo_individuo = crossover(dominio, individuos_ordenados[i1], individuos_ordenados[i2])
      mutacao_novo_individuo = mutacao(dominio, passo, novo_individuo, probabilidade_mutacao)
      populacao.append(mutacao_novo_individuo)

  return custos[0][1]



solucao = algoritmo_genetico(dominio, funcao_avaliacao, numero_geracoes = 500, tamanho_populacao=100, 
                             elitismo = 0.2, probabilidade_mutacao = 0.05)



print(solucao)
imprime_calendario(solucao)