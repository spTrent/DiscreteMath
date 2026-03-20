from math import sin, cos, e, log2, log


def a(x):
    return sin(x) - 2 * x ** 2 + 0.5 # ([-0.5, 0] и [0.5, 1])

def da(x):
    return cos(x) - 4 * x

def b(x):
    a, n = 1, 2
    return x ** n - a # для нечетных: x = a ** (1/n)
                    #для четных: x = +- a ** (1/n)

def db(x):
    a, n = 1, 2
    return n * x ** (n-1)

def c(x):
    return (1 - x ** 2) ** 1/2 - e ** x + 0.1 # ([-1, -0.5] и [0, 0.5])

def dc(x):
    return -2*x / 2 * (1 - x ** 2) ** 1/2 - e ** x

def d(x):
    return x ** 6 - 5 * x ** 3 - 2 # ([-1, -0.5], [1.5, 2])

def dd(x):
    return 6 * x ** 5 - 15 * x ** 2

def e(x):
    return log2(x) - 1 / (1 + x**2) # ([1, 1.5])

def de(x):
    return 1 / (x * log(2)) + (2 * x) / (1 + x**2)**2

def f(x):
    return sin(x / 2) - 1 # ([2, 4], [-10, -8], [14, 16])

def df(x):
    return 0.5 * cos(x / 2)

def g(x):
    return log(x) - 1 # ([2, 3])

def dg(x):
    return 1 / x


def newton_method(n, f, df, a, b, max_iter=100):
    eps = 10 ** (-n)
    x = (a + b) / 2
    print(f'Шаг 0: x0 = {x}')

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-12:
            print(f'Шаг #{i}: производная = 0')
            return None

        x1 = x - fx / dfx
        print(f'Шаг #{i}: x{i} = {x1}')

        if abs(x1 - x) < eps:
            return x1

        x = x1

    print('Достигнуто максимальное число итераций')
    return None

print(newton_method(3, a, da, -0.5, 0))
