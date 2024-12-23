import random
import time
from Q6_Fila_Estatica import Fila_estatica  # Importa a classe Fila_estatica

# Função para medir o tempo de operações de enqueue e dequeue em uma fila estática
def medir_tempo_fila(capacidade):
    # Cria uma instância da fila estática com a capacidade especificada
    fila = Fila_estatica(capacidade)

    # Gera uma lista de números aleatórios para adicionar à fila
    elementos = [random.randint(1, 100) for _ in range(capacidade)]

    # Medindo o tempo de inserção (enqueue) na fila
    inicio_enqueue = time.time()  # Marca o tempo inicial
    for elem in elementos:
        fila.enqueue(elem)  # Adiciona cada elemento na fila
    tempo_enqueue = time.time() - inicio_enqueue  # Calcula o tempo gasto

    # Medindo o tempo de remoção (dequeue) na fila
    inicio_dequeue = time.time()  # Marca o tempo inicial
    for _ in range(capacidade):
        fila.dequeue()  # Remove elementos da fila
    tempo_dequeue = time.time() - inicio_dequeue  # Calcula o tempo gasto

    # Retorna os tempos de inserção e remoção
    return tempo_enqueue, tempo_dequeue

# Função principal para executar os testes
def main():
    tamanhos = [100, 1000, 10000, 1000000]  # Lista de diferentes tamanhos de fila para teste
    resultados = {}  #O dicionário que irá armazenar os resultados dos tempos

    # Loop para medir os tempos para cada tamanho de fila
    for tamanho in tamanhos:
        print(f"Medindo para tamanho: {tamanho}")  # Exibe o tamanho atual sendo testado
        # Mede os tempos de enqueue e dequeue para o tamanho atual
        tempo_enqueue, tempo_dequeue = medir_tempo_fila(tamanho)
        # Armazena os resultados no dicionário
        resultados[tamanho] = {
            "enqueue": tempo_enqueue,
            "dequeue": tempo_dequeue
        }

    # Exibe os resultados de forma organizada
    print("\nResultados:")
    for tamanho, tempos in resultados.items():
        print(f"Tamanho: {tamanho}")
        print(f"  Tempo de Enqueue: {tempos['enqueue']:.4f} segundos")  # Tempo formatado com 4 casas decimais
        print(f"  Tempo de Dequeue: {tempos['dequeue']:.4f} segundos")

if __name__ == "__main__":
    main()  # Executa a função principal
