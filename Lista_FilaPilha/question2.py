# Questão 2 
# Crie 2 listas — uma com 5 nomes (João, Maria, Kleber, Caio, Sarah) e outra com 5 saldos em reais (2350.20, 540.50, 300.00, 830.15, 150.00). Usando laços de repetição, imprima os dados no formato:
# LISTA DE CLIENTES - BANCO XXXXXXXX NOME      SALDO nome0     saldo0 ...

cliente = ["João","Maria","Kleber","Caio", "Sarah"]
saldo = [2350.20, 540.50, 300.00, 830.15, 150.00]
print("LISTA DE CLIENTES - BANCO XXXXXXXX")
print("Nome\tSaldo")
for i in range(len(cliente)):
    print(cliente[i]," ", f"{saldo[i]:.2f}") 