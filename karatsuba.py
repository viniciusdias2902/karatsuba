def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0

def main():
    print("Bem-vindo ao Algoritmo de Karatsuba!")

    try:
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        return

    if x < 0 or y < 0:
        print("Este algoritmo só funciona com números inteiros não-negativos.")
        return

    resultado = karatsuba(x, y)

    print(f"O resultado de {x} multiplicado por {y} é: {resultado}")

if __name__ == "__main__":
    main()
