#Complete as funcoes a seguir

def soma(a, b):
	#Insira o codigo aqui
    print("A SOMA:", a+b)

def subtrai(a, b):
	#Insira o codigo aqui
    print("A SUBTRACAO:", a-b)
def multiplica(a, b):
	#Insira o codigo aqui
    print("A MULTIPLICACAO:", a*b)
def divide(a, b):
	#Insira o codigo aqui
    if(b==0):
        print("A DIVISÃO NÃO PODE SER EXECUTADA POIS O segundo número não pode ser 0.")
    else:
        print("A DIVISAO:", a/b)

#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

