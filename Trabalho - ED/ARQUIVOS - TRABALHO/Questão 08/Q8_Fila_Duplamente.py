class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None
    
class Fila_duplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def fila_vazia(self):
        return self.inicio is None
    
    def fila_cheia(self):
        return False
    
    def insere_fila(self, valor):
        novo_no = No(valor)
        if self.fila_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no
        return True
    
    def remove_fila(self):
        if self.fila_vazia():
            return None
        else:
            valor = self.inicio.dado
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            else:
                self.inicio.anterior = None
            return valor
    
    def imprimir_fila(self):
        atual = self.inicio
        print("Fila:", end=" ")
        
        while atual:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()

if __name__ == "__main__":
    f = Fila_duplamente()
    print(f.insere_fila(6))
    print(f.insere_fila(9))
    print(f.insere_fila(3))
    print(f.insere_fila(19))
    print(f.imprimir_fila())
    print(f.remove_fila())
    print(f.remove_fila())
    print(f.imprimir_fila())
