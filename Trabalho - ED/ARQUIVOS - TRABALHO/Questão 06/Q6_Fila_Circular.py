# Classe que representa um nó da fila
class Node:
    def __init__(self, elemento):
        # Cada nó contém um elemento e uma referência para o próximo nó
        self.elemento = elemento
        self.next = None

# Classe que implementa uma fila circular simplesmente encadeada - método FIFO (First In, First Out)
class Fila_circular: 
    def __init__(self, capacidade):
        # Inicializa a fila com referências para o início e fim
        # Define tamanho inicial como 0 e armazena a capacidade máxima da fila
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.capacidade = capacidade

    # Retorna o tamanho atual da fila
    def get_tamanho(self):
        return self.tamanho

    # Verifica se a fila está vazia
    def fila_vazia(self):
        return self.tamanho == 0
    
    # Verifica se a fila está cheia
    def fila_cheia(self):
        return self.tamanho == self.capacidade

    # Retorna o elemento no início da fila
    def topo(self):
        # Printa o elemento do início da fila
        print(self.inicio.elemento)
        return 

    # Adiciona um elemento na fila
    def enqueue(self, elemento):
        novo_no = Node(elemento)  # Cria um novo nó com o elemento fornecido

        if self.fila_vazia():
            # Caso a fila esteja vazia, o novo nó será tanto o início quanto o fim
            self.inicio = novo_no
            self.fim = novo_no
            self.fim.next = self.inicio  # Aponta para o início para manter o comportamento circular

        elif self.fila_cheia():
            # Caso a fila esteja cheia, exibe uma mensagem de erro
            print("FILA CIRCULAR CHEIA!")
            return

        else:
            # Adiciona o novo nó ao fim da fila e ajusta o ponteiro para o início
            self.fim.next = novo_no
            self.fim = novo_no
            self.fim.next = self.inicio

        self.tamanho += 1  # Incrementa o tamanho da fila

    # Remove um elemento do início da fila
    def dequeue(self):
        if self.fila_vazia():
            # Caso a fila esteja vazia, exibe uma mensagem de erro
            print("FILA VAZIA!")
        
        elif self.inicio == self.fim:
            # Se existe só um elemento, ele é removido e a fila é "zerada"
            self.inicio = None
            self.fim = None

        else:
            # Move o início para o próximo nó e ajusta o ponteiro do fim
            self.inicio = self.inicio.next
            self.fim.next = self.inicio

        self.tamanho -= 1  # Decrementa o tamanho da fila

    # Imprime os elementos da fila na ordem em que serão removidos
    def imprimir(self):
        if self.fila_vazia():
            print("FILA VAZIA")  # Caso a fila esteja vazia
        else:
            atual = self.inicio
            while True:
                # Percorre a fila circular e imprime os elementos
                print(atual.elemento, end=" <-- ")
                atual = atual.next
                if atual == self.inicio:  # Verifica se chegou novamente ao início
                    break
            print()

# Exemplo de uso da fila circular
if __name__ == "__main__":
    cq = Fila_circular(4)  # Cria uma fila circular com capacidade para 4 elementos
    cq.enqueue(1)  # Adiciona o elemento 1
    cq.enqueue(2)  # Adiciona o elemento 2
    cq.topo()  # Exibe o elemento no início da fila
    cq.enqueue(3)  # Adiciona o elemento 3
    cq.enqueue(6)  # Adiciona o elemento 6
    cq.enqueue(9)  # Tentativa de adicionar mais um elemento (fila cheia)
    cq.imprimir()  # Imprime os elementos da fila
    cq.dequeue()  # Remove o elemento do início da fila
    cq.imprimir()  # Imprime os elementos restantes
    print(cq.get_tamanho())  # Exibe o tamanho atual da fila
