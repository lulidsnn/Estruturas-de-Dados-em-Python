from typing import Any

class Node:
    """
    Representa um nó do deque dinâmico.

    Atributos:
        valor (Any): O valor armazenado no nó.
        próximo (Node): Ponteiro para o próximo nó no deque.
        anterior (Node): Ponteiro para o nó anterior no deque.
    """
    def __init__(self, valor: Any):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class DequeDinamico:
    """
    Implementa um deque (fila duplamente terminada) usando uma lista encadeada.
    """
    def __init__(self): #Inicializa um deque vazio
        self.inicio = None #Ponteiro para o início do deque
        self.fim = None #Ponteiro para o fim do deque
        self.tamanho = 0 #Número de elementos no deque

    def Deque_e_vazia(self) -> bool:
        '''
        Verifica se o deque está vazio
        Returns:
            bool: True se o deque estiver vazio, False caso o deque contrário
        '''
        return self.tamanho == 0
    
    def Insere_inicio_deque(self, valor: Any):
        '''
        Insere um valor no início do deque.
        Args:
            valor (Any): O valor a ser inserido.
        '''
        novo_no = Node(valor) #Cria um novo nó com o valor fornecido
        if self.Deque_e_vazia():
            #Se o deque estiver vazio, o nó se torna o inicio e o fim
            self.inicio = novo_no
            self.fim = novo_no
        else:
            #Liga o novo nó ao início atual
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no # Atualiza o ponteiro anterior do nó que era o início
            self.inicio = novo_no #O novo nó se torna o novo início
        self.tamanho += 1 #Incrementa o tamanho do deque

    def Insere_final_deque(self, valor: Any):
        """
        Insere um valor no final do deque.

        Args:
            valor (Any): O valor a ser inserido.
        """
        novo_no = Node(valor)
        if self.Deque_e_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            # Liga o novo nó ao final atual
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no # o novo nó se torna o novo fim
        self.tamanho += 1

    def Remove_inicio_deque(self) -> Any:
        """
        Remove e retorna o valor do início do deque.

        Raises:
            IndexError: Se o deque estiver vazio.

        Returns:
            Any: O valor removido do início do deque.
        """
        if self.Deque_e_vazia():
            raise IndexError('Deque vazio!')
        valor = self.inicio.valor #Armazena o valor a ser retornado
        if self.tamanho == 1:
            #Se houver apenas um elemento, o deque fica vazio
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo #Remove o primeiro elemento
            self.fim.anterior = None #O anterior do início é nulo

        self.tamanho -=1
        return valor
    
    def Remove_final_deque(self) -> Any:
        """
        Remove e retorna o valor do final do deque.

        Raises:
            IndexError: Se o deque estiver vazio.

        Returns:
            Any: O valor removido do final do deque.
        """
        if self.Deque_e_vazia():
            raise IndexError('Deque vazio!')
        valor = self.fim.valor
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else: 
            self.fim = self.fim.anterior #O elemento anterior ao fim vira o novo fim
            self.fim.proximo = None #O próximo do novo fim é nulo
        self.tamanho -= 1
        return valor
    
    def imprimir(self):
        """
        Imprime os elementos do deque.
        """
        if self.Deque_e_vazia():
            print('Deque vazio!')
            return
        atual = self.inicio
        while atual: #Enquanto atual não for nulo
            print(atual.valor, end=" ") #Printa o valor de atual
            atual = atual.proximo #Atual recebe o próximo nó
        print()

if __name__ == "__main__":
    d = DequeDinamico()
    d.Insere_final_deque(9)
    d.Insere_inicio_deque(1)
    d.Insere_inicio_deque(6)
    d.Insere_inicio_deque(4)
    d.Remove_inicio_deque()
    d.Insere_final_deque(8)
    d.Remove_final_deque()
    d.imprimir()