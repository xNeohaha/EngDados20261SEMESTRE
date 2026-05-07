def inver(mstring,lg):
    if lg >= 0:
        print(mstring[lg], end = " ")
        inver(mstring,lg-1)

def main():
    msg = input("Digite uma mensagem para ser invertida!\n")
    size = len(msg)-1
    results = inver(msg, size)
    print()
if __name__ == "__main__":
    main()