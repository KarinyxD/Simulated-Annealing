import math
import random

# ==============================================================================
# SEÇÃO PARA ADAPTAR AO SEU PROBLEMA
# Você só precisa modificar as 3 funções abaixo para o problema da sua aula.
# ==============================================================================

def gerar_solucao_inicial():
    """
    Cria e retorna uma solução inicial aleatória para o seu problema.
    A 'solução' pode ser qualquer coisa: uma lista, um número, um objeto, etc.
    
    Exemplo (para um problema de encontrar o mínimo de uma função f(x)):
    # return random.uniform(-100, 100) # Um número aleatório entre -100 e 100
    """
    # IMPLEMENTE AQUI: Como gerar a primeira solução.
    # Exemplo genérico:
    return [random.randint(0, 10) for _ in range(5)] # Uma lista de 5 números aleatórios

def custo(solucao):
    """
    Calcula e retorna o "custo" da solução.
    O objetivo do algoritmo é MINIMIZAR este valor.
    Se o seu problema for de MAXIMIZAÇÃO, basta retornar o valor negativo (ou 1/valor).
    
    Exemplo (minimizar a soma dos quadrados dos números na lista):
    # return sum(x**2 for x in solucao)
    """
    # IMPLEMENTE AQUI: A função objetivo do seu problema.
    # Exemplo genérico:
    return sum(solucao) # Queremos minimizar a soma dos valores da lista

def vizinho(solucao):
    """
    Gera uma solução "vizinha", ou seja, uma pequena modificação da solução atual.
    A qualidade da busca depende muito de como você define um "vizinho".
    
    Exemplo (para uma lista de números):
    # nova_solucao = solucao[:] # Cria uma cópia
    # indice = random.randint(0, len(nova_solucao) - 1)
    # nova_solucao[indice] += random.uniform(-0.5, 0.5) # Modifica um elemento
    # return nova_solucao
    """
    # IMPLEMENTE AQUI: Como gerar uma pequena variação da solução atual.
    # Exemplo genérico:
    nova_solucao = solucao[:] # É CRUCIAL criar uma cópia!
    indice_para_mudar = random.randint(0, len(nova_solucao) - 1)
    nova_solucao[indice_para_mudar] += random.randint(-1, 1) # Adiciona ou subtrai 1
    return nova_solucao

# ==============================================================================
# ALGORITMO DO SIMULATED ANNEALING (Não precisa modificar daqui para baixo)
# ==============================================================================

def simulated_annealing(temperatura_inicial, taxa_resfriamento, temperatura_minima, num_iteracoes_por_temp):
    """
    Executa o algoritmo do Recozimento Simulado.
    
    Parâmetros:
    - temperatura_inicial: A temperatura inicial do sistema. Controla a probabilidade de aceitar piores soluções no início.
    - taxa_resfriamento: Fator pelo qual a temperatura é multiplicada a cada passo (ex: 0.95).
    - temperatura_minima: O algoritmo para quando a temperatura atinge este valor.
    - num_iteracoes_por_temp: Quantas vezes o algoritmo tenta encontrar um vizinho melhor antes de diminuir a temperatura.
    
    Retorna:
    - A melhor solução encontrada e o seu custo.
    """
    print("Iniciando o Simulated Annealing...")
    
    # 1. Gera uma solução inicial aleatória
    solucao_atual = gerar_solucao_inicial()
    custo_atual = custo(solucao_atual)
    
    # Guarda a melhor solução encontrada até agora
    melhor_solucao = solucao_atual
    melhor_custo = custo_atual
    
    temperatura = temperatura_inicial
    
    # 2. Loop principal: continua enquanto o sistema estiver "quente"
    while temperatura > temperatura_minima:
        for _ in range(num_iteracoes_por_temp):
            # 3. Gera uma solução vizinha
            solucao_vizinha = vizinho(solucao_atual)
            custo_vizinho = custo(solucao_vizinha)
            
            # 4. Decide se deve mover para a solução vizinha
            delta_custo = custo_vizinho - custo_atual
            
            # Se a nova solução for melhor, sempre aceita
            if delta_custo < 0:
                solucao_atual = solucao_vizinha
                custo_atual = custo_vizinho
                
                # Atualiza a melhor solução global se necessário
                if custo_atual < melhor_custo:
                    melhor_solucao = solucao_atual
                    melhor_custo = custo_atual
            # Se a nova solução for pior, aceita com uma certa probabilidade
            else:
                probabilidade_aceitacao = math.exp(-delta_custo / temperatura)
                if random.random() < probabilidade_aceitacao:
                    solucao_atual = solucao_vizinha
                    custo_atual = custo_vizinho
        
        # 5. Diminui a temperatura (resfriamento)
        temperatura *= taxa_resfriamento
        
    print("Algoritmo finalizado.")
    return melhor_solucao, melhor_custo

# --- Exemplo de como executar o algoritmo ---
if __name__ == "__main__":
    # Parâmetros do algoritmo (você pode precisar ajustá-los)
    TEMP_INICIAL = 1000
    TAXA_RESFRIAMENTO = 0.99  # Um valor entre 0.8 e 0.99 é comum
    TEMP_MINIMA = 1
    ITERACOES_POR_TEMP = 100
    
    melhor_solucao_encontrada, menor_custo_encontrado = simulated_annealing(
        temperatura_inicial=TEMP_INICIAL,
        taxa_resfriamento=TAXA_RESFRIAMENTO,
        temperatura_minima=TEMP_MINIMA,
        num_iteracoes_por_temp=ITERACOES_POR_TEMP
    )
    
    print("\n" + "="*30)
    print(f"Melhor solução encontrada: {melhor_solucao_encontrada}")
    print(f"Menor custo obtido: {menor_custo_encontrado}")
    print("="*30)