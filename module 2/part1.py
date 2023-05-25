def on_easy():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print((a ** 10 + b ** 10) ** 0.5)


def IMT():
    weight = float(input())
    height = float(input())
    imt = weight / (height * height)
    if imt < 18.5:
        print("Недостаточная масса")
    elif imt <= 25:
        print("Оптимальная масса")
    else:
        print("Избыточная масса")


def string_cost():
    cost = len(input())*60
    print(cost // 100, "р.", cost % 100, "коп.")


def word_count():
    print(len(input().split()))


def zodiac():
    names = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
    year = int(input())
    print(names[year % 12])


def reverse_number():
    num = input()
    num = num.replace(num[-5:], num[-1:-6:-1])
    print(int(num))


def SAC():
    num = input()[::-1]
    sac = ""
    for i in range((len(num) - 1) // 3):
        sac += num[3 * i:3 * i + 3] + ','
    sac += num[-((len(num) - 1) % 3) - 1:]
    print(sac[::-1])


def _task_of_Josephus():
    n = int(input())
    k = int(input())
    people = [1] * n
    idx = n - 1
    for _ in range(n - 1):
        count = 0
        while count < k:
            idx = (idx + 1) % n
            if people[idx] == 1:
                count += 1
        people[idx] = 0
    for i in range(n):
        if people[i] == 1:
            print(i + 1)
            break


if __name__ == '__main__':
    _task_of_Josephus()
