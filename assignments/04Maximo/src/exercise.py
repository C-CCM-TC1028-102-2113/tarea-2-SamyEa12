def main():
    #escribe tu código abajo de esta línea
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))
    if num1>=num2 and num1>=num3:
        print(str(num1))
    elif num2>=num1 and num2>=num3:
        print(str(num2))
    elif num3>=num1 and num3>=num2:
        print(str(num3))
    pass

if __name__=='__main__':
    main()
