# Questão 18
# Implemente os três algoritmos com visualização textual do estado do array a cada passo, 
# destacando os elementos sendo comparados e trocados.

def bubble_sort(lista):
    n = len(lista)
    print("\n=== Bubble Sort ===")
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Mostrar comparação
            visual = ""
            for k in range(len(lista)):
                if k == j or k == j + 1:
                    visual += f"[{lista[k]}] "
                else:
                    visual += f"{lista[k]} "
            print("Comparando:", visual)
            
            if lista[j] > lista[j + 1]:
                print("→ Trocando!")
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print("Estado atual:", lista)
    
    print("Resultado final:", lista)

def selection_sort(lista):
    n = len(lista)
    print("\n=== Selection Sort ===")
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            
            visual = ""
            for k in range(len(lista)):
                if k == min_index or k == j:
                    visual += f"[{lista[k]}] "
                else:
                    visual += f"{lista[k]} "
            print("Comparando:", visual)
            
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            print(f"→ Trocando {lista[i]} com {lista[min_index]}")
            lista[i], lista[min_index] = lista[min_index], lista[i]
            print("Estado atual:", lista)
    
    print("Resultado final:", lista)

def insertion_sort(lista):
    print("\n=== Insertion Sort ===")
    
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        print(f"\nInserindo [{chave}] na parte ordenada")
        
        while j >= 0 and lista[j] > chave:
            
            visual = ""
            for k in range(len(lista)):
                if k == j:
                    visual += f"[{lista[k]}] "
                else:
                    visual += f"{lista[k]} "
            print("Comparando:", visual)
            
            lista[j + 1] = lista[j]
            j -= 1
            print("Movendo elemento:", lista)
        
        lista[j + 1] = chave
        print("Estado após inserção:", lista)
    
    print("Resultado final:", lista)

lista = [5, 3, 8, 4, 2]

bubble_sort(lista.copy())
selection_sort(lista.copy())
insertion_sort(lista.copy())
