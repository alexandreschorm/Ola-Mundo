def calcula_resultado(x, num1, num2):
    if x == "+":
        resultado = num1 + num2
    elif x == "-":
        resultado = num1 - num2
    elif x == "*":
        resultado = num1 * num2
    else:
        resultado = num1 / num2
    return resultado

x = input("Escolha a operação que deseja realizar (+, -, * ou /): ")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado = calcula_resultado(x, a, b)

print(f"O resultado de {a} e {b} é: {resultado}")