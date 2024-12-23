# Classe que implementa uma fila estática usando um vetor (lista) - 
class Fila_estatica:
    def __init__(self, capacidade):
        # Inicializa os atributos principais da fila
        self.inicio = 0  # Índice do primeiro elemento
        self.fim = -1  # Índice do último elemento
        self.tamanho_maximo = capacidade  # Capacidade máxima da fila
        self.fila = [None] * capacidade  # Lista que armazena os elementos da fila
        self.tamanho_atual = 0  # Número atual de elementos na fila

    # Exibe o primeiro elemento da fila, se existir
    def primeiro_elem(self):
        if self.fim == -1:
            print("Queue is Empty")  # Mensagem caso a fila esteja vazia
            return
        print(self.fila[self.inicio])  # Mostra o elemento no índice inicial

    # Verifica se a fila está vazia
    def fila_vazia(self):
        return self.tamanho_atual == 0

    # Verifica se a fila está cheia
    def fila_cheia(self):
        return self.tamanho_atual == self.tamanho_maximo

    # Retorna o tamanho atual da fila
    def tamanho(self):
        return self.tamanho_atual

    # Adiciona um elemento ao final da fila
    def enqueue(self, elemento):
        if self.fila_cheia():
            # Exibe uma mensagem caso a fila esteja cheia
            print("FILA CHEIA")
            return 
        self.fim += 1  # Atualiza o índice do fim
        self.fila[self.fim] = elemento  # Adiciona o elemento no índice fim
        self.tamanho_atual += 1  # Incrementa o contador de tamanho

    # Remove o primeiro elemento da fila
    def dequeue(self):
        if self.fila_vazia():
            # Exibe uma mensagem caso a fila esteja vazia
            print("FILA VAZIA")
            return
        # Move os elementos subsequentes para preencher o espaço vazio
        for i in range(self.fim):
            self.fila[i] = self.fila[i + 1]
        self.fim -= 1  # Atualiza o índice do fim
        self.tamanho_atual -= 1  # Decrementa o contador de tamanho

    # Imprime os elementos da fila na ordem em que seriam removidos
    def imprimir(self):
        if self.inicio > self.fim:
            # Exibe uma mensagem caso a fila esteja vazia
            print("Queue is Empty")
            return
        # Percorre e imprime os elementos da fila
        for i in range(self.inicio, self.fim + 1):
            print(self.fila[i], end=" <-- ")
        print()

# Testa a classe Fila_estatica
if __name__ == "__main__":
    # Cria uma fila de capacidade 20
    q = Fila_estatica(20)
    print(q.fila_vazia())  # Verifica se a fila está inicialmente vazia

    # Adiciona elementos de 1 a 20 na fila
    for i in range(1,16):
        q.enqueue(i)
    
    q.imprimir()  # Imprime os elementos da fila
    q.dequeue()  # Remove o primeiro elemento
    q.dequeue()  # Remove o próximo elemento
    q.dequeue()  # Remove mais um elemento
    q.imprimir()  # Imprime os elementos restantes na fila
    print(q.tamanho())  # Exibe o tamanho atual da fila
