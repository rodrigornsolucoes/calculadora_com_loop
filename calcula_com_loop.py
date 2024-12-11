def calculadora(n1, n2, op):
    if op == 1:
        return n1 + n2
    elif op == 2:
        if n1 > n2:
            return n1 - n2
        else:
            return n2 - n1
    elif op == 3:
        return n1 * n2
    elif op == 4:
        if n1 == 0:
            return "Nao e possivel dividir um numero por zero."
        else:
            return n1 / n2
    elif op == 0:
        return "Essa opcao nao existe"
    
print('''Escolha uma uma opcao abaixo
    1: Soma
    2: Subtracao
    3: Multiplicacao
    4: Divisao
    0: Sair''')

opcao = int(input("Qual foi sua escolha? "))

while opcao > 0:
    num_1 = int(input("Digite o primeiro numero: "))
    nun_2 = int(input("Digite o segundo numero: "))
    print(calculadora(num_1, nun_2, opcao))
    print('''Escolha uma uma opcao abaixo
    1: Soma
    2: Subtracao
    3: Multiplicacao
    4: Divisao
    0: Sair''')
    opcao = int(input("Digite sua opcao aqui: "))
