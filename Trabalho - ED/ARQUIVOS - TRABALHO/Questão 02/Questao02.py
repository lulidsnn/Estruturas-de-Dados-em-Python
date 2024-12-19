class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def is_full(self):
        return False 
        # sempre False, pq pilha encadeada nunca fica cheia, a menos que, a memória se esgote.
    
    def push(self, valor):
        new_node = Node(valor)
        new_node.next = self.top
        self.top = new_node
        return True
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            valor = self.top.data
            self.top = self.top.next
            return valor
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data
    
    def print_stack(self):
        current = self.top
        print("Pilha: ", end="")
        
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
    def print_reverse(self):
        if self.is_empty():
            print("Pilha Vazia")
            return
        
        temp_stack = Stack()
        while not self.is_empty():
            temp_stack.push(self.pop())
        print("Pilha Invertida: ", end="")
            
        while not temp_stack.is_empty():
            print(temp_stack.pop(), end=" ")
        print()
        
    def release(self):
        while not self.is_empty():
            self.pop()
        self.top = None
    
    def palindrome(self, string):
        string = string.lower().replace(" ", "")
        aux_stack = Stack()
        
        for char in string:
            aux_stack.push(char)
        reversed_string = ""
        
        while not aux_stack.is_empty():
            reversed_string += aux_stack.pop()
            
        return string == reversed_string
    
    def eliminate(self, elemento):
        if self.is_empty():
            return False
        
        temp_stack = Stack()
        found = False
        
        while not self.is_empty():
            valor = self.pop()
            if valor == elemento and not found:
                found = True
            else:
                temp_stack.push(valor)
                
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
            
        return found
    
    def impar_par(self):
        pares = Stack()
        impares = Stack()
        
        while not self.is_empty():
            valor = self.pop()
            if valor % 2 == 0:
                pares.push(valor)
            else:
                impares.push(valor)
                
        print("Pilha de pares: ")
        pares.print_stack()
        print("Pilha de Ímpares: ")
        impares.print_stack()        
    