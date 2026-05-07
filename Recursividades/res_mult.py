def mult(a,b):
    print(f"{a} + ({a} X {b})")
    if b == 0:
        print(f"Retornou 0")
        return 0
    elif b == 1:
        return a
    else:
        return a + mult(a, b - 1)

def main():
    print("====================================\n")
    print("Forneça a multiplicação\n")
    print("====================================\n")
    a = int(input("Digite o valor do numero a ser multiplicado: \n"))
    b = int(input("Digite o valor do multiplicador: \n"))

    results = mult(a,b)
    print("====================================\n")
    print(f"O resultado é {results}\n")

if __name__ == "__main__":
    main()