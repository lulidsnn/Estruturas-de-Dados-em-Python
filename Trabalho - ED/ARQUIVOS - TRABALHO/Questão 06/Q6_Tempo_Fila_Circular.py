import random
import time
from Q6_Fila_Circular import Fila_circular  # Importa a classe Fila_circular do módulo correspondente

# Função para medir o tempo de operações de enqueue e dequeue em uma fila circular
def medir_tempo_fila(capacidade):
    # Cria uma instância da fila circular com a capacidade especificada
    filaC = Fila_circular(capacidade)

    # Gera uma lista de números aleatórios para adicionar à fila
    elementos = [random.randint(1, 100) for _ in range(capacidade)]

    # Medindo o tempo de inserção (enqueue) na fila
    inicio_enqueue = time.time()  # Marca o tempo inicial
    for elem in elementos:
        filaC.enqueue(elem)  # Adiciona cada elemento na fila
    tempo_enqueue = time.time() - inicio_enqueue  # Calcula o tempo gasto

    # Medindo o tempo de remoção (dequeue) na fila
    inicio_dequeue = time.time()  # Marca o tempo inicial
    for _ in range(capacidade):
        filaC.dequeue()  # Remove elementos da fila
    tempo_dequeue = time.time() - inicio_dequeue  # Calcula o tempo gasto

    # Retorna os tempos de inserção e remoção
    return tempo_enqueue, tempo_dequeue

# Função principal para executar os testes
def main():
    tamanhos = [100, 1000, 10000, 1000000]  # Diferentes tamanhos de fila para teste
    resultados = {}  #O dicionário que irá armazenar os resultados dos tempos

    for tamanho in tamanhos:
        print(f"Medindo para tamanho: {tamanho}")  # Exibe o tamanho atual sendo medido
        # Mede os tempos de enqueue e dequeue para o tamanho atual
        tempo_enqueue, tempo_dequeue = medir_tempo_fila(tamanho)
        # Armazena os resultados em um dicionário
        resultados[tamanho] = {
            "enqueue": tempo_enqueue,
            "dequeue": tempo_dequeue
        }

    # Exibe os resultados após os testes
    print("\nResultados:")
    for tamanho, tempos in resultados.items():
        print(f"Tamanho: {tamanho}")
        print(f"  Tempo de Enqueue: {tempos['enqueue']:.4f} segundos")  # Tempo formatado com 4 casas decimais
        print(f"  Tempo de Dequeue: {tempos['dequeue']:.4f} segundos")

if __name__ == "__main__":
    main()  # Executa a função principal
