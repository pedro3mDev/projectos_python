numero = "0000.2345.10.1"
titular = "Fulano de Tal"
banco = "BFA"
saldo = 20000.00
limite = 100000.00
print ("\nNumero: ",numero,"\nTitular: ",titular, "\nBanco: ",banco,"\nSaldo: ",saldo,"\nLimite: ",limite)


def criar_conta(numero, titular, banco, saldo, limite):
    conta = { "numero":numero, "titular":titular, "banco":banco, "saldo":saldo, "limite":limite}
    return conta

