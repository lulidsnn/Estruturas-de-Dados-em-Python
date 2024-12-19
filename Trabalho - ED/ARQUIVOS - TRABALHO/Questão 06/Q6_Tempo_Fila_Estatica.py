import random
import time
from Q6_Fila_Estatica import Fila_estatica

def medir_tempo_fila(capacidade):

    fila = Fila_estatica(capacidade)

    elementos = [random.randint(1, 100) for _ in range(capacidade)]

    inicio_enqueue = time.time()
    for elem in elementos:
        fila.enqueue(elem)
    tempo_enqueue = time.time() - inicio_enqueue

    inicio_dequeue = time.time()
    for _ in range(capacidade):
        fila.dequeue()
    tempo_dequeue = time.time() - inicio_dequeue

    return tempo_enqueue, tempo_dequeue

def main():
    tamanhos = [100, 1000, 10000, 1000000]
    resultados = {}

    for tamanho in tamanhos:
        print(f"Medindo para tamanho: {tamanho}")
        tempo_enqueue, tempo_dequeue = medir_tempo_fila(tamanho)
        resultados[tamanho] = {
            "enqueue": tempo_enqueue,
            "dequeue": tempo_dequeue
        }

    print("\nResultados:")
    for tamanho, tempos in resultados.items():
        print(f"Tamanho: {tamanho}")
        print(f"  Tempo de Enqueue: {tempos['enqueue']:.4f} segundos")
        print(f"  Tempo de Dequeue: {tempos['dequeue']:.4f} segundos")

if __name__ == "__main__":
    main()
