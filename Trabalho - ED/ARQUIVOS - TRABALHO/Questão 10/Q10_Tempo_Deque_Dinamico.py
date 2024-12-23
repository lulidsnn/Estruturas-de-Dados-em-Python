import random  # Biblioteca para gerar números aleatórios
import time    # Biblioteca para medir o tempo de execução
from Q10_Deque_Encadeado import DequeDinamico  # Importa a classe DequeDinamico do arquivo Q10_Deque_Encadeado

def gerar_vetor_aleatorio(tamanho):
    """
    Função que gera um vetor de números aleatórios entre 1 e 100.
    """
    return [random.randint(1, 100) for _ in range(tamanho)]  # Gera um vetor com números aleatórios

def medir_tempo_operacoes(tamanho):
    """
    Função que mede o tempo de várias operações (inserção e remoção) em um deque encadeado.
    """
    vetor = gerar_vetor_aleatorio(tamanho)  # Gera o vetor de tamanho 'tamanho' com números aleatórios
    deque = DequeDinamico()  # Cria uma instância de deque encadeado

    tempos = {}  # Dicionário para armazenar os tempos das operações

    # Medir tempo de inserção no início do deque
    inicio = time.time()  # Marca o tempo de início
    for valor in vetor:  # Para cada valor no vetor
        deque.Insere_inicio_deque(valor)  # Insere o valor no início do deque
    fim = time.time()  # Marca o tempo de fim
    tempos['inserir_inicio'] = fim - inicio  # Calcula o tempo de inserção no início

    # Medir tempo de remoção do início do deque
    inicio = time.time()  # Marca o tempo de início
    for _ in range(tamanho):  # Para o tamanho do vetor
        deque.Remove_inicio_deque()  # Remove o valor do início do deque
    fim = time.time()  # Marca o tempo de fim
    tempos['remover_inicio'] = fim - inicio  # Calcula o tempo de remoção do início

    # Preencher novamente o deque para as operações no final
    for valor in vetor:  # Insere todos os valores novamente no deque
        deque.Insere_final_deque(valor)

    # Medir tempo de inserção no final do deque
    inicio = time.time()  # Marca o tempo de início
    for valor in vetor:  # Para cada valor no vetor
        deque.Insere_final_deque(valor)  # Insere o valor no final do deque
    fim = time.time()  # Marca o tempo de fim
    tempos['inserir_final'] = fim - inicio  # Calcula o tempo de inserção no final

    # Medir tempo de remoção do final do deque
    inicio = time.time()  # Marca o tempo de início
    for _ in range(tamanho):  # Para o tamanho do vetor
        deque.Remove_final_deque()  # Remove o valor do final do deque
    fim = time.time()  # Marca o tempo de fim
    tempos['remover_final'] = fim - inicio  # Calcula o tempo de remoção do final

    return tempos  # Retorna os tempos das operações

def main():
    """
    Função principal que executa a medição de tempo para diferentes tamanhos de vetores.
    """
    tamanhos = [100, 1000, 10000, 1000000]  # Tamanhos de vetor a serem testados
    resultados = {}  # Dicionário para armazenar os resultados

    # Para cada tamanho especificado, mede os tempos das operações
    for tamanho in tamanhos:
        print(f"Analisando tempo para vetor de tamanho {tamanho}...")  # Exibe qual tamanho está sendo analisado
        tempos = medir_tempo_operacoes(tamanho)  # Mede os tempos das operações para o tamanho
        resultados[tamanho] = tempos  # Armazena os resultados no dicionário

    # Exibir os resultados
    for tamanho, tempos in resultados.items():
        print(f"\nResultados para tamanho {tamanho}:")
        for operacao, tempo in tempos.items():
            print(f"{operacao}: {tempo:.4f} segundos")  # Exibe o tempo de cada operação

if __name__ == "__main__":
    main()
