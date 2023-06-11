def chessboard():
    n, m = [int(el) for el in input().split()]
    for i in range(n):
        row = []
        if i % 2 == 0:
            row = list('.*' * (m // 2))
        else:
            row = list('*.' * (m // 2))
        if m % 2 == 1:
            row.append('.' if i % 2 == 0 else '*')
        print(*row)


def side_diagonal():
    n = int(input())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if j < n - i - 1:
                row.append(0)
            elif j == n - i - 1:
                row.append(1)
            else:
                row.append(2)
        matrix.append(row)
    for row in matrix:
        print(*row)


def fill_1():
    n, m = [int(el) for el in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(list(range(i * m + 1, i * m + 1 + m)))
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def fill_2():
    n, m = [int(el) for el in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(list(range(i + 1, n * m + 1, n)))
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def fill_3():
    n = int(input())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
        matrix[i][n - i - 1] = 1
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def fill_4():
    n = int(input())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n - i):
            matrix[i][j] = 1
        for j in range(n - i - 1, i + 1):
            matrix[i][j] = 1
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def _fill_5():
    n, m = [int(el) for el in input().split()]
    values = list(range(1, m + 1))
    matrix = []
    for i in range(n):
        matrix.append(values[i % m:] + values[:i % m])
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def snake_fill():
    n, m = [int(el) for el in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(list(range(i * m + 1, i * m + 1 + m)))
        if i % 2 == 1:
            matrix[i].reverse()
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def _diagonal_fill():
    n, m = [int(el) for el in input().split()]
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    number = 1
    for j in range(m):
        for k in range(min(n, j + 1)):
            matrix[k][j - k] = number
            number += 1
    for i in range(1, n):
        for k in range(min(n - i, m)):
            matrix[i + k][m - 1 - k] = number
            number += 1
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def ___spiral_fill():
    n, m = [int(el) for el in input().split()]
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    number = 1
    for k in range((min(n, m) + 1) // 2):
        for j in range(k, m - k):
            matrix[k][j] = number
            number += 1
        for i in range(k + 1, n - k):
            matrix[i][m - 1 - k] = number
            number += 1
        if k != (n - 1 - k):
            for j in range(m - k - 2, k - 1, -1):
                matrix[n - 1 - k][j] = number
                number += 1
        if k != (m - 1 - k):
            for i in range(n - k - 2, k, -1):
                matrix[i][k] = number
                number += 1
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


if __name__ == '__main__':
    ___spiral_fill()
