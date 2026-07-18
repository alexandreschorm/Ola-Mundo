#função que identifica o operador aritmético e realiza o calculo
def calcula_resultado(x, a, b):
    if x == "+":
        resultado = a + b
    elif x == "-":
        resultado = a - b
    elif x == "*":
        resultado = a * b
    else:
        resultado = a / b
    #escreve o resultado da operação na tela
    print(f"O resultado da operação é: {resultado:.2f}")

#funcao que identifica se é uma operação valida
def validacao(x):
    operacoes = ["+", "-", "*", "/"]
    eh_valido = False
    for i in range(4):
        if x == operacoes[i]:
            eh_valido = True
    return eh_valido

ope = input("Escolha a operação que deseja realizar (ex: +, -, * ou /): ")
valido = validacao(ope)
if valido:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    calcula_resultado(ope, num1, num2)
else:
    print("Está operação é invalida.")