from math import comb

def main():
    k = int(input("Введите степень многочлена: "))
    polynom = list(map(int, input("Введите коэффициенты многочлена:\n").split()))
    if (len(polynom) != k + 1):
        raise ValueError("Неверное количество коэффициентов")
    a = int(input("Введите a: "))
    b = int(input("Введите B: "))
    d = b - a
    new_polynom = [0] * (k + 1)
    for i in range(k + 1):
        for j in range(i + 1):
            new_polynom[j] += polynom[k - i] * comb(i, j) * d ** (i - j)
    print(new_polynom[::-1])

if __name__ == '__main__':
    main()