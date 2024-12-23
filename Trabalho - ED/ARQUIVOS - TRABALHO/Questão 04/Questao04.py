def validar_expressao(expressao):
    
    pilha = []
    abertos = tuple('({[')
    fechados = tuple(')}]')
    pares = dict(zip(abertos, fechados))

    for char in expressao:
        if char in abertos:
            pilha.append(char)
        elif char in fechados:
            if not pilha or pares[pilha.pop()] != char:
                return False
    return not pilha

if __name__ == "__main__":
    expressao = input("Digite a expressão matemática: ")
    if validar_expressao(expressao):
        print("Expressão válida!")
    else:
        print("Expressão inválida!")