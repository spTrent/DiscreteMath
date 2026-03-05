def caratsuba(a, b):
    divisor = b[0] * b[0] + b[1] * b[1]
    real_part = (a[0] * b[0] + a[1] * b[1]) / divisor
    imagine_part = ((a[0] + a[1]) * (b[0] - b[1]) - a[0] * b[0] + a[1] * b[1]) / divisor
    return real_part, imagine_part
    #Итог: 3 умножения по Карацубе в числителе (z1 * (сопряженное к z2)),
    # 2 умножения b0 ** 2 и b1 ** 2, и 2 деления почленно на знаменатель. минимум 7 делений

def main():
    a = list(map(int, input("Введите коэффициенты a0 и a1: ").split()))
    b = list(map(int, input("Введите коэффициенты b0 и b1: ").split()))
    print(f'z1 = {a[0]} + {a[1]}i')
    print(f'z2 = {b[0]} + {b[1]}i')
    res = caratsuba(a, b)
    print(f'z1/z2 = {res[0]} + {res[1]}i')

if __name__ == '__main__':
    main()