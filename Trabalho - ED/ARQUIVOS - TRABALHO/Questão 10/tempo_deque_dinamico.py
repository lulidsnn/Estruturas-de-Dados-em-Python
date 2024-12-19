import random
import time
from Q10_Deque_Encadeado import DequeDinamico

def gerar_vetor_aleatorio(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

def medir_tempo_operacoes(tamanho):
    vetor = gerar_vetor_aleatorio(tamanho)
    deque = DequeDinamico()

    tempos = {}

    # Medir tempo de inserção no início
    inicio = time.time()
    for valor in vetor:
        deque.Insere_inicio_deque(valor)
    fim = time.time()
    tempos['inserir_inicio'] = fim - inicio

    # Medir tempo de remoção do início
    inicio = time.time()
    for _ in range(tamanho):
        deque.Remove_inicio_deque()
    fim = time.time()
    tempos['remover_inicio'] = fim - inicio

    # Preencher novamente o deque para operações no final
    for valor in vetor:
        deque.Insere_final_deque(valor)

    # Medir tempo de inserção no final
    inicio = time.time()
    for valor in vetor:
        deque.Insere_final_deque(valor)
    fim = time.time()
    tempos['inserir_final'] = fim - inicio

    # Medir tempo de remoção do final
    inicio = time.time()
    for _ in range(tamanho):
        deque.Remove_final_deque()
    fim = time.time()
    tempos['remover_final'] = fim - inicio

    return tempos

def main():
    tamanhos = [100, 1000, 10000, 1000000]
    resultados = {}

    for tamanho in tamanhos:
        print(f"Analisando tempo para vetor de tamanho {tamanho}...")
        tempos = medir_tempo_operacoes(tamanho)
        resultados[tamanho] = tempos

    # Exibir resultados
    for tamanho, tempos in resultados.items():
        print(f"\nResultados para tamanho {tamanho}:")
        for operacao, tempo in tempos.items():
            print(f"{operacao}: {tempo:.4f} segundos")

if __name__ == "__main__":
    main()
