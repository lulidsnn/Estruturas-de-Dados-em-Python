class Node:
    def __init__(self, elemento):
        self.elemento = elemento
        self.next = None

class Fila_circular:
    def __init__(self, capacidade):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.capacidade = capacidade
     
    def get_tamanho(self):
        return self.tamanho

    def fila_vazia(self):
        return self.tamanho == 0
    
    def fila_cheia(self):
        return self.tamanho == self.capacidade
    
    def topo(self):
        print(self.inicio.elemento)
        return 

    def enqueue(self, elemento):
        novo_no = Node(elemento)

        if self.fila_vazia():
            self.inicio = novo_no
            self.fim = novo_no
            self.fim.next = self.inicio
            
        elif self.fila_cheia():
            print("FILA CIRCULAR CHEIA!")
            return

        else:
            self.fim.next = novo_no
            self.fim = novo_no
            self.fim.next = self.inicio

        self.tamanho += 1

    def dequeue(self):
        if self.fila_vazia():
            print("FILA VAZIA!")

        elif self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        
        else:
            self.inicio = self.inicio.next
            self.fim.next = self.inicio

        self.tamanho -= 1

    def imprimir(self):
        if self.fila_vazia():
            print("FILA VAZIA")
        else:
            atual = self.inicio
            while True:
                print(atual.elemento, end=" <-- ")
                atual = atual.next
                if atual == self.inicio:
                    break
            print()

if __name__ == "__main__":
    cq = Fila_circular(4)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.topo()
    cq.enqueue(3)
    cq.enqueue(6)
    cq.enqueue(9) #a fila tem capacidade 4, ao tentar colocar o quinto elemento retorna q a fila esta cheia
    cq.imprimir() 
    cq.dequeue()
    cq.imprimir() 
    print(cq.get_tamanho())