def der(polynom, degree):
    if degree == 0:
        return polynom
    n = len(polynom) - 1
    der_polynom = [polynom[i] * (n - i) for i in range(len(polynom) - 1)]
    return der(der_polynom, degree-1)

def lim_to_inf(f, g, deg_f, deg_g):
    if (deg_f > deg_g or deg_g < 0 or len(g) == 0):
        return float('inf')
    if (deg_f < deg_g or deg_f < 0 or len(f) == 0):
        return 0
    return f[0] / g[0]

def lim_to_a(f, g, deg_f, deg_g, a):
    sum_f = sum(f[deg_f - i] * a ** i for i in range(deg_f + 1))
    sum_g = sum(g[deg_g - i] * a ** i for i in range(deg_g + 1))
    if sum_g != 0:
        return sum_f / sum_g
    if sum_f != 0:
        return float('inf')
    return lim_to_a(der(f, 1), der(g, 1), deg_f - 1, deg_g - 1)


def main():
    deg_f = int(input("Введите степень многочлена f: "))
    deg_g = int(input("Введите степень многочлена g: "))
    f = list(map(int, input("Введите коэффициенты многочлена f:\n").split()))
    g = list(map(int, input("Введите коэффициенты многочлена g:\n").split()))
    print(f'lim to inf (f / g) = {lim_to_inf(f, g, deg_f, deg_g)}')
    a = int(input("Введите a: "))
    print(f'lim to {a} (f / g) = {lim_to_a(f, g, deg_f, deg_g, a)}')

if __name__ == '__main__':
    main()