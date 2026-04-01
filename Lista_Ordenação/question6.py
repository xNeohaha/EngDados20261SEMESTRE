# Questão 6
# Demonstre a eficiência do Insertion Sort em uma lista quase ordenada, 
# contando o número de comparações realizadas e comparando com o pior caso teórico.

def insertion_sort(lista):
    count = 0
    
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0:
            count += 1  # conta a comparação lista[j] > chave
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
                
        lista[j + 1] = chave
        
    return count

      
# exemplo de uso
lista = [7,9,2,1,4,5]
count = insertion_sort(lista)
print(count)