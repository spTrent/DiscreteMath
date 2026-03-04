def scanf() -> tuple:
    k = int(input("Введите размерность линейной оболочки: "))
    n = int(input("Введите максимальную степень многочлена в базисе: "))
    n += 1
    polynoms = []
    for i in range(k):
        Gk = list(map(int, input(f"Введите коэффициенты G{i} через пробел:\n").split()))
        if (len(Gk)) <= n:
            Gk = [0] * (n - len(Gk)) + Gk
        else:
            raise ValueError("Слишком много коэффициентов")
        polynoms.append(Gk)
    return k, n, polynoms

def print_polynoms(polynoms, k, n) -> None:
    for i in range(k):
        print(f'G{i}: ')
        for j in range(n):
            if (j <= n - 2):
                print(f'{polynoms[i][j]} * x ^ {n - j - 1} + ', end='')
            else:
                print(f'{polynoms[i][j]} * x ^ {n - j - 1}')

def print_matrix(matrix, k, n):
    for i in range(n):
        for j in range(k):
            print(matrix[i][j], end=' ')
        print()

def construct_matrix(polynoms, k, n):
    matrix = [[0 for i in range(k)] for j in range(n)]
    for i in range(n):
        for j in range(k):
            matrix[i][j] = polynoms[j][i]
    return matrix

def solve(matrix, k, n, f_polynom):
    extented = [matrix[i] + [f_polynom[i]] for i in range(n)]
    row = 0
    basic = [-1] * n
    for col in range(k):
        find_row = -1
        for r in range(row, n):
            if extented[r][col] != 0:
                find_row = r
                basic[row] = col
                break
        if find_row == -1:
            continue
        
        extented[row], extented[find_row] = extented[find_row], extented[row]
        forward_el = extented[row][col]
        extented[row] = [extented[row][i] / forward_el for i in range(k + 1)]

        for r in range(row + 1, n):
            forward = extented[r][col]
            if forward == 0:
                continue
            extented[r] = [extented[r][i] - extented[row][i] * forward for i in range(k + 1)]
        row += 1

    for r in range(n):
        if all(extented[r][c] == 0 for c in range(k)) and extented[r][k] != 0:
            return False, None
        
    x = [0.0] * k
    for r in range(n - 1, -1, -1):
        curr_basic = basic[r]
        if curr_basic == -1:
            continue
        free_var = extented[r][k]
        for c in range(curr_basic + 1, k):
            free_var -= extented[r][c] * x[c]
        x[curr_basic] = free_var
    return True, x



def main():
    k, n, polynoms = scanf()
    matrix = construct_matrix(polynoms, k, n)
    f_polynom = list(map(int, input("Введите коэффициенты многочлена f через пробел:\n").split()))
    if (len(f_polynom) != n):
        raise ValueError("Неверное количество коэффициентов")
    flag, x = solve(matrix, k, n, f_polynom)
    if flag:
        print(x)

if __name__ == '__main__':
    main()