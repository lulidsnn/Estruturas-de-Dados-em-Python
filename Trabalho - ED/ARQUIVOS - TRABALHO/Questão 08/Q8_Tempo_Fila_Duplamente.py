import random  
import time    
from Q8_Fila_Duplamente import Fila_duplamente  # Importa a classe Fila_duplamente do arquivo Q8_Fila_Duplamente

def medir_tempo_fila(capacidade):
    """
    Função que mede o tempo de operação de inserção (enqueue) e remoção (dequeue) 
    em uma fila duplamente encadeada.
    """
    filaD = Fila_duplamente()  # Cria uma instância da fila duplamente encadeada

    # Gera uma lista de elementos aleatórios (inteiros entre 1 e 100)
    elementos = [random.randint(1, 100) for _ in range(capacidade)]

    # Medindo o tempo para inserir os elementos na fila (enqueue)
    inicio_enqueue = time.time()  # Marca o tempo de início
    for elem in elementos:
        filaD.insere_fila(elem)  # Insere cada elemento na fila
    tempo_enqueue = time.time() - inicio_enqueue  # Calcula o tempo gasto para a operação

    # Medindo o tempo para remover os elementos da fila (dequeue)
    inicio_dequeue = time.time()  # Marca o tempo de início
    for _ in range(capacidade):
        filaD.remove_fila()  # Remove cada elemento da fila
    tempo_dequeue = time.time() - inicio_dequeue  # Calcula o tempo gasto para a operação

    return tempo_enqueue, tempo_dequeue  # Retorna os tempos de enqueue e dequeue

def main():
    """
    Função principal que executa a medição de tempo para diferentes tamanhos de filas.
    """
    tamanhos = [100, 1000, 10000, 1000000]  # Diferentes capacidades para testar a fila
    resultados = {}  #O dicionário que irá armazenar os resultados dos tempos

    # Para cada tamanho especificado, mede os tempos de enqueue e dequeue
    for tamanho in tamanhos:
        print(f"Medindo para tamanho: {tamanho}")  # Exibe qual tamanho está sendo medido
        tempo_enqueue, tempo_dequeue = medir_tempo_fila(tamanho)  # Mede os tempos
        resultados[tamanho] = {  # Armazena os resultados para cada tamanho
            "enqueue": tempo_enqueue,
            "dequeue": tempo_dequeue
        }

    # Exibe os resultados de todas as medições
    print("\nResultados:")
    for tamanho, tempos in resultados.items():
        print(f"Tamanho: {tamanho}")
        print(f"  Tempo de Enqueue: {tempos['enqueue']:.4f} segundos")
        print(f"  Tempo de Dequeue: {tempos['dequeue']:.4f} segundos")

if __name__ == "__main__":
    main()
