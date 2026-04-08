import heapq

def dijkstra(grafo, origem):
    # Inicializa as distâncias com infinito e a origem com 0
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    
    # Dicionário para rastrear os predecessores e reconstruir os caminhos
    predecessores = {no: None for no in grafo}
    
    # Fila de prioridade: armazena tuplas (distancia_acumulada, no)
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)
        
        # Se a distância retirada da fila for maior que a registrada, ignora (nó já fechado com custo menor)
        if distancia_atual > distancias[no_atual]:
            continue
            
        # Avalia os vizinhos do nó atual
        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso
            
            # Relaxamento da aresta: se encontrou um caminho mais curto, atualiza
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))
                
    return distancias, predecessores

def obter_caminho_completo(predecessores, origem, destino):
    """Função auxiliar para reconstruir a string do caminho do início ao fim."""
    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = predecessores[atual]
        
    if caminho and caminho[0] == origem:
        return " -> ".join(caminho)
    return "Caminho inacessível"

# 1. Definição do Grafo (baseado na imagem fornecida)
grafo = {
    'S': {'A': 3, 'C': 2, 'F': 6},
    'A': {'B': 6, 'D': 1},
    'B': {'E': 1},
    'C': {'A': 2, 'D': 3},
    'D': {'E': 4},
    'E': {}, # Nó E não tem arestas de saída
    'F': {'E': 2}
}

# 2. Execução do Algoritmo
origem = 'S'
distancias, predecessores = dijkstra(grafo, origem)

# 3. Impressão dos Resultados formatados
print(f"{'Nó Destino':<12} | {'Menor Custo':<12} | {'Predecessor':<12} | {'Caminho Completo'}")
print("-" * 75)

# Ordenando a exibição pelo custo, similar à ordem de fechamento do algoritmo
nos_ordenados_por_custo = sorted(distancias.items(), key=lambda x: x[1])

for destino, custo in nos_ordenados_por_custo:
    pred = predecessores[destino] if predecessores[destino] else "-"
    caminho_str = obter_caminho_completo(predecessores, origem, destino)
    print(f"{destino:<12} | {custo:<12} | {pred:<12} | {caminho_str}")