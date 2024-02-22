def sumar(dos_numeros):
    return sum(dos_numeros)

if __name__ == "__main__":
    print("introduce dos digitos que quieras sumar.")
    numeros = []
    for _ in range(2):
        while True:
            try:
                numero = float(input("número: "))
                numeros.append(numero)
                break
            except ValueError:
                print(" introduce un digito válido.")
    resultado = sumar(numeros)
    print(f"la suma es: {resultado}")
