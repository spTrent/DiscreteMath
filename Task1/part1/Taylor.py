def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def der(polynom, degree):
    if degree == 0:
        return polynom
    n = len(polynom) - 1
    der_polynom = [polynom[i] * (n - i) for i in range(len(polynom) - 1)]
    return der(der_polynom, degree-1)

def taylor_formule(polynom, n):
    res = []
    for k in range(n + 1):
        fk = der(polynom, k)
        k_factorial = factorial(k)
        fk = [fk[i] / k_factorial for i in range(len(fk))]
        res.insert(0, fk)
    return res



def main():
    n = int(input("Введите степень многочлена: "))
    polynom = list(map(int, input("Введите коэффициенты многочлена:\n").split()))
    if len(polynom) != n + 1:
        raise ValueError("Неверное количество коэффициентов")
    res = taylor_formule(polynom, n)
    print(res)

if __name__ == '__main__':
    main()