class Node:
    """
    Classe que representa um nó na pilha encadeada.
    Cada nó armazena um valor (data) e uma referência para o próximo nó (next).
    """
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó


class Stack:
    """
    Classe que implementa uma pilha (stack) encadeada.
    A pilha utiliza nós (Node) para armazenar os valores de forma dinâmica.
    """

    def __init__(self):
        """
        Inicializa uma pilha vazia.
        """
        self.top = None  # O topo da pilha começa vazio

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        Retorna True se a pilha estiver vazia; caso contrário, False.
        """
        return self.top is None

    def is_full(self):
        """
        Verifica se a pilha está cheia.
        Para pilhas encadeadas, nunca fica cheia (a menos que a memória acabe).
        Retorna sempre False.
        """
        return False

    def push(self, valor):
        """
        Adiciona um elemento ao topo da pilha.
        """
        new_node = Node(valor)  # Cria um novo nó com o valor fornecido
        new_node.next = self.top  # O novo nó aponta para o antigo topo
        self.top = new_node  # Atualiza o topo para o novo nó
        return True

    def pop(self):
        """
        Remove e retorna o elemento no topo da pilha.
        Retorna None se a pilha estiver vazia.
        """
        if self.is_empty():
            return None
        else:
            valor = self.top.data  # Armazena o valor do nó no topo
            self.top = self.top.next  # Atualiza o topo para o próximo nó
            return valor

    def peek(self):
        """
        Retorna o elemento no topo da pilha sem removê-lo.
        Retorna None se a pilha estiver vazia.
        """
        if self.is_empty():
            return None
        else:
            return self.top.data

    def print_stack(self):
        """
        Imprime os elementos da pilha do topo até a base.
        """
        current = self.top
        print("Pilha: ", end="")

        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_reverse(self):
        """
        Imprime os elementos da pilha na ordem inversa sem alterar a estrutura original.
        Utiliza uma pilha auxiliar para inverter os elementos.
        """
        if self.is_empty():
            print("Pilha Vazia")
            return

        temp_stack = Stack()  # Pilha auxiliar para inverter os elementos
        while not self.is_empty():
            temp_stack.push(self.pop())
        print("Pilha Invertida: ", end="")

        while not temp_stack.is_empty():
            print(temp_stack.pop(), end=" ")
        print()

    def release(self):
        """
        Remove todos os elementos da pilha, liberando memória.
        """
        while not self.is_empty():
            self.pop()
        self.top = None

    def palindrome(self, string):
        """
        Verifica se uma string é um palíndromo (lê-se igual de trás para frente).
        Ignora espaços e letras maiúsculas.
        """
        string = string.lower().replace(" ", "")  # Remove espaços e converte para minúsculas
        aux_stack = Stack()

        # Empilha todos os caracteres da string
        for char in string:
            aux_stack.push(char)

        reversed_string = ""
        # Remove os caracteres da pilha auxiliar para formar a string reversa
        while not aux_stack.is_empty():
            reversed_string += aux_stack.pop()

        return string == reversed_string  # Compara a string original com a reversa

    def eliminate(self, elemento):
        """
        Remove a primeira ocorrência de um elemento da pilha, mantendo a ordem dos demais.
        """
        if self.is_empty():
            return False

        temp_stack = Stack()  # Pilha auxiliar para armazenar os elementos temporariamente
        found = False  # Flag para indicar se o elemento foi encontrado

        while not self.is_empty():
            valor = self.pop()
            if valor == elemento and not found:
                found = True  # Marca o elemento como encontrado e não empilha novamente
            else:
                temp_stack.push(valor)

        # Reempilha os elementos de volta na pilha original
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        return found

    def impar_par(self):
        """
        Separa os elementos da pilha em duas novas pilhas:
        - Uma contendo os números pares
        - Outra contendo os números ímpares
        Imprime as duas pilhas resultantes.
        """
        pares = Stack()  # Pilha para números pares
        impares = Stack()  # Pilha para números ímpares

        while not self.is_empty():
            valor = self.pop()
            if valor % 2 == 0:
                pares.push(valor)
            else:
                impares.push(valor)

        print("Pilha de pares: ")
        pares.print_stack()
        print("\nPilha de Ímpares: ")
        impares.print_stack()


if __name__ == "__main__":
    # Testando a separação de pares e ímpares
    p = Stack()
    for i in range(16):
        p.push(i)

    p.impar_par()  # Exibe pilhas separadas de pares e ímpares
    p.release()  # Libera a memória da pilha
    p.print_stack()  # Mostra que a pilha está vazia

    print("\n")

    # Testando outras funcionalidades da pilha
    p1 = Stack()
    for i in range(16):
        p1.push(i)

    p1.pop()  # Remove o topo da pilha
    p1.pop()  # Remove o próximo elemento
    p1.print_stack()  # Exibe os elementos restantes na pilha
    p1.eliminate(4)  # Remove a primeira ocorrência do elemento 4
    p1.print_stack()  # Exibe a pilha após a remoção

    # Testando a função de palíndromo
    print(p1.palindrome('onibus'))  # False
    print(p1.palindrome('subi no onibus'))  # True
