def validar(numero):
    while(numero < 0):
        numero = int(input("Tente Novamente: "))
    return numero

def factorial(numero):
    if(numero == 0):
        return 1
    else: 
        result = 1
        for cont in range(1, numero+1):
            result = result * cont; 
        return result

print("Factorial:", factorial(validar(int(input("Insira o Numero: ")))) )

