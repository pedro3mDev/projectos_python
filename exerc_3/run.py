def par_impar(numero):
    if (numero % 2 == 0): 
        return True
    return False

if(par_impar(int(input("Insira o Numero: "))) == True ):
    print("Par")
else:
    print("Impar")

