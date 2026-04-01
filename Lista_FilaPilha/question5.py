#  Questão 5 
# Dada a lista L = [1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23] do documento, escreva um programa que demonstre todas as operações de fatiamento apresentadas:

Lista = [1,3,5,9,11,13,15,17,19,21,23]

status = False
while status == False:
    Option = input("Escolha as letras de A até E para ver os exemplos\n")
    match Option:
        case "A": # ●	(a) Os 3 primeiros elementos — L[0:3]
            print(Lista[0:3])
        case "B": # ●	(b) Do índice 4 ao 9 — L[4:10]
            print(Lista[4:10])
        case "C": # ●	(c) Os 5 primeiros — L[:5]
            print(Lista[:5])
        case "D": # ●	(d) Do índice 5 em diante — L[5:]
            print(Lista[5:])
        case "E": # ●	(e) De 3 em 3, do índice 0 ao 8 — L[0:8:3]  
            print(Lista[0:8:3]) 
        case _:
            print("Entrada Inválida:", Option)