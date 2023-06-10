def multiplication_table():
    n, m = int(input()), int(input())
    mult = [[i * j for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            print(str(mult[i][j]).ljust(3), end=' ')
        print()


def max_in_table():
    n, m = int(input()), int(input())
    index = None
    maximum = None
    for i in range(n):
        row = [int(el) for el in input().split()]
        for j in range(m):
            if i == 0 and j == 0:
                maximum = row[j]
                index = (i, j)
            elif maximum < row[j]:
                maximum = row[j]
                index = (i, j)
    print(*index)


def column_swapping():
    n, m = int(input()), int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    j1, j2 = [int(j) for j in input().split()]
    for i in range(n):
        matrix[i][j1], matrix[i][j2] = matrix[i][j2], matrix[i][j1]
        print(*matrix[i])


def symmetric_matrix():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print('YES')
    else:
        print('NO')


def swap_diagonals():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    for j in range(n):
        matrix[j][j], matrix[n - j - 1][j] = matrix[n - j - 1][j], matrix[j][j]
    for i in range(n):
        print(*matrix[i])


def mirroring():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    for i in range((n + 1) // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    for li in matrix:
        print(*li)


def matrix_rotation():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j]
    for li in new_matrix:
        print(*li)


def knight_moves():
    field = [['.' for _ in range(8)] for _ in range(8)]
    k_j, k_i = input()
    k_j, k_i = ord(k_j)-ord('a'), 8 - int(k_i)
    field[k_i][k_j] = 'N'
    move_i = [-2, -2, -1, -1, 1, 1, 2, 2]
    move_j = [-1, 1, -2, 2, -2, 2, -1, 1]
    for i, j in zip(move_i, move_j):
        if (0 <= k_i + i <= 7) and (0 <= k_j + j <= 7):
            field[k_i + i][k_j + j] = '*'
    for row in field:
        print(*row)


def _magic_square():
    n = int(input())
    matrix = []
    numbers = set()
    flag = True
    for _ in range(n):
        row = [int(el) for el in input().split()]
        for el in row:
            if 1 <= el <= n*n:
                numbers.add(el)
            else:
                flag = False
                break
        if not flag:
            break
        matrix.append(row)
    if (not flag) or (len(numbers) != n*n):
        print('NO')
    else:
        suma = sum(matrix[0])
        diag1, diag2 = 0, 0
        for i in range(n):
            col_sum, row_sum = 0, 0
            for j in range(n):
                col_sum += matrix[j][i]
                row_sum += matrix[i][j]
            if not((col_sum == row_sum) and (row_sum == suma)):
                flag = False
                break
            diag1 += matrix[i][i]
            diag2 += matrix[i][n - i - 1]
        if (not flag) or (diag1 != diag2) or (diag1 != suma):
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    _magic_square()
