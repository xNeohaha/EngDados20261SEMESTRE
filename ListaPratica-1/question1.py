
# Questão 1 
# Crie uma lista heterogênea em Python com pelo menos 5 elementos de tipos diferentes (int, float, string, bool).
Lista = [42, 3.7, "Opa!", True, None]

# Em seguida:
# ●	(a) Imprima o tipo de cada elemento usando type()
print(type(Lista[0]))
print(type(Lista[1]))
print(type(Lista[2]))
print(type(Lista[3]))
print(type(Lista[4]))
# ●	(b) Acesse e imprima o primeiro e o último elemento pelo índice
print(Lista[0],Lista[4])  # Primeiro e último elemento
# ●	(c) Altere o segundo elemento para o valor 99
Lista[1] = 99
print(Lista)
# ●	(d) Exclua o terceiro elemento usando del
del Lista[2]
# ●	(e) Imprima a lista final
print(Lista)

