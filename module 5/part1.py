def n_lists_element():
    inp = input().split()
    n = int(input())
    res = [[] for _ in range(n)]
    for i in range(len(inp)):
        res[i % n].append(inp[i])
    print(res)


def max_in_area2():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    maximum = matrix[0][-1]
    for i in range(1, n):
        for j in range(n - 1 - i, n):
            maximum = max(maximum, matrix[i][j])
    print(maximum)


def matrix_transposition():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        print(*row)


def snowflake():
    n = int(input())
    matrix = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = '*'
        matrix[i][n - 1 - i] = '*'
        matrix[i][n // 2] = '*'
        matrix[n // 2][i] = '*'
    for row in matrix:
        print(*row)


def symmetric_matrix():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    flag = True
    for j in range(n - 1, -1, -1):
        for i in range(n - j - 1):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print('YES')
    else:
        print('NO')


def _latin_square():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    flag = True
    for i in range(n):
        set_row = set()
        set_col = set()
        for j in range(n):
            if (1 <= matrix[i][j] <= n) and (1 <= matrix[j][i] <= n):
                set_row.add(matrix[i][j])
                set_col.add(matrix[j][i])
            else:
                flag = False
                break
        if (not flag) or (len(set_row) != n) or (len(set_col) != n):
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')


def queen_moves():
    field = [['.' for _ in range(8)] for _ in range(8)]
    k_j, k_i = input()
    k_j, k_i = ord(k_j) - ord('a'), 8 - int(k_i)
    field[k_i][k_j] = 'Q'
    for j in range(8):
        if j != k_j:
            field[k_i][j] = '*'
    for i in range(8):
        if i != k_i:
            field[i][k_j] = '*'
    i, j = k_i + 1, k_j + 1
    while (i < 8) and (j < 8):
        field[i][j] = '*'
        i += 1
        j += 1
    i, j = k_i - 1, k_j - 1
    while (i > -1) and (j > -1):
        field[i][j] = '*'
        i -= 1
        j -= 1
    i, j = k_i + 1, k_j - 1
    while (i < 8) and (j > -1):
        field[i][j] = '*'
        i += 1
        j -= 1
    i, j = k_i - 1, k_j + 1
    while (i > -1) and (j < 8):
        field[i][j] = '*'
        i -= 1
        j += 1
    for row in field:
        print(*row)


def diagonals_parallel_main_diagonal():
    n = int(input())
    line = list(range(n))
    res = []
    for i in range(n):
        row = line[i::-1]
        row.extend(line[1:n - i])
        res.append(row)
    for row in res:
        print(*row)


if __name__ == '__main__':
    diagonals_parallel_main_diagonal()
