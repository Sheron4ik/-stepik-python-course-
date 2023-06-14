def train_1():
    numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
    res = 1
    for num in numbers:
        res *= num
    print(res)


def train_2():
    data = 'Python для продвинутых!'
    letters = tuple(data)
    print(letters)


def train_3():
    poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
    poet_data = poet_data[:2] + ('Москва', )
    print(poet_data)


def train_4():
    numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
    res = []
    for number in numbers:
        res.append(sum(number) / len(number))
    print(res)


def top_of_parabola():
    a, b, c = int(input()), int(input()), int(input())
    x0 = -b / (2 * a)
    y0 = (4 * a * c - b * b) / (4 * a)
    print((x0, y0))


def competitive_selection():
    n = int(input())
    students = []
    for _ in range(n):
        name, grade = input().split()
        students.append((name, int(grade)))
        print(name, grade)
    print()
    for student in students:
        if student[1] >= 4:
            print(student[0], student[1])


def tribonacci_sequence():
    n = int(input())
    t1, t2, t3 = 1, 1, 1
    for i in range(n):
        if i == 0:
            print(t1, end=' ')
        elif i == 1:
            print(t2, end=' ')
        elif i == 2:
            print(t3, end=' ')
        else:
            t1, t2, t3 = t2, t3, t1 + t2 + t3
            print(t3, end=' ')


if __name__ == '__main__':
    tribonacci_sequence()
