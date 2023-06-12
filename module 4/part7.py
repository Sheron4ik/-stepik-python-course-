def matrix_addition():
    n, m = [int(el) for el in input().split()]
    matrix1 = [[int(el) for el in input().split()] for _ in range(n)]
    input()
    matrix2 = [[int(el) for el in input().split()] for _ in range(n)]
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    for li in result:
        print(*li)


def _matrix_multiplication():
    n, m1 = [int(el) for el in input().split()]
    matrix1 = [[int(el) for el in input().split()] for _ in range(n)]
    input()
    m2, k = [int(el) for el in input().split()]
    matrix2 = [[int(el) for el in input().split()] for _ in range(m2)]
    result = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for l in range(m1):
                result[i][j] += matrix1[i][l] * matrix2[l][j]
    for li in result:
        print(*li)


def _matrix_exponentiation():
    def multiply(m1, m2):
        result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for l in range(len(m2)):
                    result[i][j] += m1[i][l] * m2[l][j]
        return result

    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    m = int(input())
    res = [[matrix[i][j] for j in range(n)] for i in range(n)]
    for _ in range(m - 1):
        res = multiply(res, matrix)
    for li in res:
        print(*li)


if __name__ == '__main__':
    _matrix_exponentiation()
