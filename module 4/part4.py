def matrix_1():
    n, m = int(input()), int(input())
    inp = [[input() for __ in range(m)] for _ in range(n)]
    for li in inp:
        print(*li)


def matrix_2():
    n, m = int(input()), int(input())
    inp = [[input() for __ in range(m)] for _ in range(n)]
    for li in inp:
        print(*li)
    print()
    for i in range(m):
        for j in range(n):
            print(inp[j][i], end=' ')
        print()


def matrix_trace():
    n = int(input())
    trace = 0
    for i in range(n):
        trace += int(input().split()[i])
    print(trace)


def more_than_average():
    n = int(input())
    for _ in range(n):
        count = 0
        row = [int(el) for el in input().split()]
        average = sum(row) / n
        for el in row:
            count += 1 if el > average else 0
        print(count)


def max_in_area1():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    maximum = matrix[0][0]
    for i in range(1, n):
        maximum = max(maximum, max(matrix[i][:(i + 1)]))
    print(maximum)


def _max_in_area2():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    maximum = max(matrix[0][0], matrix[0][-1])
    for i in range(1, n):
        if i < n / 2:
            maximum = max(maximum, max(matrix[i][:(i + 1)]), max(matrix[i][n - i - 1:]))
        else:
            maximum = max(maximum, max(matrix[i][i:]), max(matrix[i][:n - i]))
    print(maximum)


def sums_quarters():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    up, right, down, left = 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if (i < j) and (i < n - 1 - j):
                up += matrix[i][j]
            elif (i < j) and (i > n - 1 - j):
                right += matrix[i][j]
            elif (i > j) and (i > n - 1 - j):
                down += matrix[i][j]
            elif (i > j) and (i < n - 1 - j):
                left += matrix[i][j]
    print(f'Верхняя четверть: {up}')
    print(f'Правая четверть: {right}')
    print(f'Нижняя четверть: {down}')
    print(f'Левая четверть: {left}')


if __name__ == '__main__':
    sums_quarters()
