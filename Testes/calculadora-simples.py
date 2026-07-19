#função que identifica o operador aritmético e realiza o calculo
def calcula_resultado(x, a, b):
    if x == 1:
        resultado = a + b
    elif x == 2:
        resultado = a - b
    elif x == 3:
        resultado = a * b
    else:
        resultado = a / b
    print(f"O resultado da operação é: {resultado:.2f}")
    print("-"*40)

#INICIO DO PROGRAMA
print("-"*40)
operador = int(input("Escolha a operação que deseja realizar:\n1.+\n2.-\n3.*\n4./\n5.Para sair\n>>>"))
while operador != 5:
    if 5>operador>0:
        num1 = float(input("Digite o primeiro número:\n>>>"))
        num2 = float(input("Digite o segundo número:\n>>>"))
        #chama a função
        calcula_resultado(operador, num1, num2)
    else:
        print("Está operação é invalida.")
        print("-"*40)
    operador = int(input("Escolha a operação que deseja realizar:\n1.+\n2.-\n3.*\n4./\n5.Para sair\n>>>"))