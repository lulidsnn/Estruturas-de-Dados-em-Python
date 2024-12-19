class Fila_estatica:
    def __init__(self, capacidade):
        self.inicio = 0
        self.fim = -1
        self.tamanho_maximo = capacidade
        self.fila = [None] * capacidade #Vetor que irá receber os elementos da fila
        self.tamanho_atual = 0

    def primeiro_elem(self):
        if self.fim == -1:
            print("Queue is Empty")
            return
        print(self.fila[self.inicio])

    def fila_vazia(self):
        return self.tamanho_atual == 0
    
    def fila_cheia(self):
        return self.tamanho_atual == self.tamanho_maximo
    
    def tamanho(self):
        return self.tamanho_atual
    
    def enqueue(self, elemento):
        if self.fila_cheia(): #Checa se 
            print("FILA CHEIA")
            return 
        self.fim += 1
        self.fila[self.fim] = elemento
        self.tamanho_atual += 1

    def dequeue(self):
        if self.fila_vazia(): #Checa se a fila está vazia
            print("FILA VAZIA")
            return
        #elem = self.primeiro_elem()
        for i in range(self.fim):
            self.fila[i] = self.fila[i + 1]
        self.fim -= 1
        self.tamanho_atual -= 1
        return 

    def imprimir(self):
        if self.inicio > self.fim:
            print("Queue is Empty")
            return
        for i in range(self.inicio, self.fim + 1): # "Invertendo" para mostrar a dinâmica de fila
            print(self.fila[i], end=" <-- ")
        print()

if __name__ == "__main__":
    # Create a queue of capacity 4
    q = Fila_estatica(20)
    print(q.fila_vazia())
    for i in range(1, 21):
        q.enqueue(i)
    
    q.imprimir()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.imprimir()
    print(q.tamanho())


            