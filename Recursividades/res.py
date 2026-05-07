def divide(a,b):
    print(f"Operação:\n A: {a}\n B: {b}\n")
    if a < b:
        print(f"Retornou 0")
        return 0
    else:
        return 1 + divide(a - b, b)
    
def main():
    print("====================================\n")
    print("Forneça os dividendos e os divisores\n")
    print("====================================\n")
    a = int(input("Digite o valor do dividendo: \n"))
    b = int(input("Digite o valor do divisor: \n"))

    results = divide(a,b)
    print("====================================\n")
    print(f"O resultado é {results}\n")

if __name__ == "__main__":
    main()