class No:
    """
    Classe que representa um nó de uma lista duplamente encadeada.
    Cada nó contém um dado (dado) e referências para o próximo (proximo) e anterior (anterior) nó.
    """
    def __init__(self, dado):
        self.dado = dado  # Armazena o dado do nó
        self.proximo = None  # Referência para o próximo nó (inicialmente None)
        self.anterior = None  # Referência para o nó anterior (inicialmente None)
    
class Fila_duplamente:
    """
    Classe que implementa uma fila utilizando uma lista duplamente encadeada.
    A fila permite inserção e remoção de elementos de forma eficiente em ambas as extremidades.
    """
    
    def __init__(self):
        """
        Inicializa a fila como vazia, com inicio e fim como None.
        """
        self.inicio = None  # Referência para o início da fila
        self.fim = None  # Referência para o fim da fila
    
    def fila_vazia(self):
        """
        Verifica se a fila está vazia.
        Retorna True se a fila estiver vazia e False caso contrário.
        """
        return self.inicio is None
    
    def fila_cheia(self):
        """
        Verifica se a fila está cheia.
        Para uma fila encadeada, a fila nunca está cheia, a não ser que haja falta de memória.
        Retorna sempre False.
        """
        return False
    
    def insere_fila(self, valor):
        """
        Insere um elemento no final da fila.
        Cria um novo nó e o adiciona ao fim da fila.
        """
        novo_no = No(valor)  # Cria um novo nó com o valor fornecido
        if self.fila_vazia():
            # Se a fila estiver vazia, o novo nó será tanto o início quanto o fim
            self.inicio = novo_no
            self.fim = novo_no
        else:
            # Se a fila não estiver vazia, o novo nó é inserido após o nó no fim da fila
            novo_no.anterior = self.fim  # O anterior do novo nó aponta para o fim atual
            self.fim.proximo = novo_no  # O próximo do nó fim aponta para o novo nó
            self.fim = novo_no  # O fim da fila é atualizado para o novo nó
        return True
    
    def remove_fila(self):
        """
        Remove o elemento do início da fila.
        Retorna o valor do nó removido ou None se a fila estiver vazia.
        """
        if self.fila_vazia():
            return None  # Se a fila estiver vazia, retorna None
        else:
            valor = self.inicio.dado  # Armazena o valor do nó removido
            self.inicio = self.inicio.proximo  # Atualiza o início da fila para o próximo nó
            if self.inicio is None:
                self.fim = None  # Se a fila ficar vazia, o fim também será None
            else:
                self.inicio.anterior = None  # Remove a referência para o nó anterior
            return valor
    
    def imprimir_fila(self):
        """
        Imprime os elementos da fila do início ao fim.
        """
        atual = self.inicio  # Começa pela referência para o início da fila
        print("Fila:", end=" ")
        
        while atual:
            print(atual.dado, end=" ")  # Imprime o dado do nó atual
            atual = atual.proximo  # Move para o próximo nó
        print()

if __name__ == "__main__":
    # Testando as funcionalidades da Fila_duplamente
    f = Fila_duplamente()
    
    # Inserindo elementos na fila
    print(f.insere_fila(6))  # Insere 6 na fila
    print(f.insere_fila(9))  # Insere 9 na fila
    print(f.insere_fila(3))  # Insere 3 na fila
    print(f.insere_fila(19))  # Insere 19 na fila
    
    # Imprime o estado atual da fila
    print(f.imprimir_fila())  # Fila: 6 9 3 19
    
    # Removendo elementos da fila
    print(f.remove_fila())  # Remove o primeiro elemento (6)
    print(f.remove_fila())  # Remove o próximo elemento (9)
    
    # Imprime o estado da fila após remoções
    print(f.imprimir_fila())  # Fila: 3 19
