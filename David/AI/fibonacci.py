def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def print_fibonacci():
    try:
        n = int(input("Hasta dónde quieres que vaya la secuencia de Fibonacci: "))
        if n < 0:
            print("Ingrese un número entero positivo.")
        elif n == 0:
            print("Ingrese un número entero mayor a cero.")
        for i in range(n):
            if i == n-1:
                print(fibonacci(i), end='.')
            else:
                print(fibonacci(i), end=', ')
    except ValueError:
        print("Ingreso un valor inválido.")
    except Exception as exception:
        print(exception)


print_fibonacci()
