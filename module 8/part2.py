def timur_and_his_team():
    n = int(input())
    m = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    students = z + n + m - x - y + k
    print(students)


def _books_to_read():
    n = int(input())
    m = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    t = int(input())
    a = int(input())
    ones = n - (n + k - z - t) - t - (n + m - x - t)
    ones += m - (n + m - x - t) - t - (m + k - y - t)
    ones += k - (n + k - z - t) - t - (m + k - y - t)
    twos = (n + k - z - t) + (n + m - x - t) + (m + k - y - t)
    threes = a - ones - twos - t
    print(ones, twos, threes, sep='\n')


if __name__ == '__main__':
    _books_to_read()
