def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x<=y and x<=z and y<=z:
        print(str(x))
        print(str(y))
        print(str(z))
    elif y<=x and y<=z and x<=z:
        print(str(y))
        print(str(x))
        print(str(z))
    elif z<=y and z<=x and y<=x:
        print(str(z))
        print(str(y))
        print(str(x))
    elif z<=y and z<=x and x<=y:
        print(str(z))
        print(str(x))
        print(str(y))
    elif x<=y and x<=z and z<=y:
        print(str(x))
        print(str(z))
        print(str(y))
    elif y<=z and y<=x and z<=x:
        print(str(y))
        print(str(z))
        print(str(x))
    pass

if __name__=='__main__':
    main()
