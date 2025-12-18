#calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão.

def selecionar_operacao(): 
    print("Escolha a operacao desejada:")
    print("Soma: 1 \nSubtracao: 2 \nDivisao: 3 \nMultiplicacao: 4 \n")
    n = int(input())
    return n

def soma():
    print("Digite os dois operandos:\n")
    n1 = float(input())
    n2 = float(input())
    result = n1 + n2
    return result

def sub():
    print("Digite os dois operandos:\n")
    n1 = float(input())
    n2 = float(input())
    result = n1 - n2
    return result

def div():
    print("Digite os dois operandos:\n")
    n1 = float(input())
    n2 = float(input())
    result = n1 / n2
    return result
def mult():
    print("Digite os dois operandos:\n")
    n1 = float(input())
    n2 = float(input())
    result = n1 * n2
    return result

operacao = selecionar_operacao()

if operacao > 4:
    print("Valor nao reconhecido!! \n\n")
    operacao = selecionar_operacao()
if operacao == 1 :
    print("Somando")
    resultado = soma()
if operacao == 2 :
    print("Subtraindo") 
    resultado = sub()
if operacao == 3:
    print("Dividindo")
    resultado = div()
if operacao == 4 :
    print("Multiplicando")
    resultado = mult()

print(f"Resultado : {resultado}")

