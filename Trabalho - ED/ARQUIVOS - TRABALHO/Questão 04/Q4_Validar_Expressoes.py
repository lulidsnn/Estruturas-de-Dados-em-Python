def validar_expressao(expressao):
    pilha = []
    delimitador = {')': '(', ']': '[', '}': '{'}

    for char in expressao:
        # Verifica se o caractere é um delimitador de abertura
        if char in '([{':
            pilha.append(char)
        # Verifica se o caractere é um delimitador de fechamento
        elif char in ')]}':
            if not pilha:
                return False  # Delimitador de fechamento sem abertura correspondente
            top = pilha.pop()
            if delimitador[char] != top:
                return False  # Ordem incorreta dos delimitadores
        # Verifica se é um caractere ASCII válido para uma expressão matemática ou literal permitido
        elif not (char.isdigit() or char in '+-*/.^ ' or char in 'ABCDEFGHIJ' or char in 'abcdefghij'):
            return False

    # Certifica-se de que todos os delimitadores foram fechados
    return not pilha

def validar_precedencia(expressao):
    pilha = []

    for char in expressao:
        if char in '{[(':
            pilha.append(char)
        elif char in ')]}':
            if not pilha:
                return False
            top = pilha.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False
        
        # Verifica a precedência
        if pilha:
            top_pilha = pilha[-1]
            if (char == ')' and top_pilha not in '([{') or \
               (char == ']' and top_pilha not in '{[') or \
               (char == '}' and top_pilha != '{'):
                return False

    return not pilha

def validar_tudo(expressao):
    """
    Valida a expressão matemática com base
    na precedência correta dos delimitadores.
    """
    if not validar_expressao(expressao):
        return False
    return validar_precedencia(expressao)

if __name__ == "__main__":
    expressao = input("Digite a expressão matemática: ")
    if validar_tudo(expressao):
        print("Expressão válida!")
    else:
        print("Expressão inválida!")
