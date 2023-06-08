def count_coordinates():
    first_quarter = 0
    second_quarter = 0
    third_quarter = 0
    fourth_quarter = 0
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        if (x > 0) and (y > 0):
            first_quarter += 1
        elif (x < 0) and (y > 0):
            second_quarter += 1
        elif (x < 0) and (y < 0):
            third_quarter += 1
        elif (x > 0) and (y < 0):
            fourth_quarter += 1
    print("Первая четверть:", first_quarter)
    print("Вторая четверть:", second_quarter)
    print("Третья четверть:", third_quarter)
    print("Четвертая четверть:", fourth_quarter)


def more_than_previous():
    numbers = list(map(int, input().split()))
    counter = 0
    for i in range(1, len(numbers)):
        if numbers[i - 1] < numbers[i]:
            counter += 1
    print(counter)


def swap_neighbors():
    numbers = list(map(int, input().split()))
    for i in range(len(numbers) // 2):
        numbers[2 * i], numbers[2 * i + 1] = numbers[2 * i + 1], numbers[2 * i]
    print(*numbers)


def right_shift():
    numbers = list(map(int, input().split()))
    res = numbers[-1:] + numbers[:-1]
    print(*res)


def different_elements():
    numbers = set(map(int, input().split()))
    print(len(numbers))


def multiplication_of_two():
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    possible = int(input())
    ans = "НЕТ"
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (numbers[i] * numbers[j]) == possible:
                ans = "ДА"
                break
        if ans == "ДА":
            break
    print(ans)


def who_win():
    timur = input()
    ruslan = input()
    if timur == ruslan:
        print("ничья")
    else:
        if timur == 'камень':
            if ruslan == 'ножницы':
                print("Тимур")
            else:
                print("Руслан")
        elif timur == 'ножницы':
            if ruslan == 'бумага':
                print("Тимур")
            else:
                print("Руслан")
        else:
            if ruslan == 'камень':
                print("Тимур")
            else:
                print("Руслан")


def _who_win_2():
    timur = input()
    ruslan = input()
    if timur == ruslan:
        print("ничья")
    else:
        if timur == 'камень':
            if ruslan == 'ножницы' or ruslan == 'ящерица':
                print("Тимур")
            else:
                print("Руслан")
        elif timur == 'ножницы':
            if ruslan == 'бумага' or ruslan == 'ящерица':
                print("Тимур")
            else:
                print("Руслан")
        elif timur == 'бумага':
            if ruslan == 'камень' or ruslan == 'Спок':
                print("Тимур")
            else:
                print("Руслан")
        elif timur == 'ящерица':
            if ruslan == 'бумага' or ruslan == 'Спок':
                print("Тимур")
            else:
                print("Руслан")
        else:
            if ruslan == 'камень' or ruslan == 'ножницы':
                print("Тимур")
            else:
                print("Руслан")


def orel_i_reshka():
    data = input()
    max_reshek, cur_reshek = 0, 0
    for i in range(len(data)):
        if data[i] == 'Р':
            cur_reshek += 1
        else:
            if cur_reshek > max_reshek:
                max_reshek = cur_reshek
            cur_reshek = 0
    print(max(max_reshek, cur_reshek))


def __silicon_valley():
    n = int(input())
    hacking = ['a', 'n', 't', 'o', 'n']
    for id in range(n):
        fridge = input()
        idx = 0
        for i in range(len(fridge)):
            if fridge[i] == hacking[idx]:
                idx += 1
                if idx == 5:
                    break
        if idx == 5:
            print(id + 1, end=' ')


def __ban_a():
    data = input() + " запретил букву"
    letters = sorted(set(data))[1:]
    data = list(data)
    for letter in letters:
        print(*(''.join(data).split()), letter)
        data = list(filter(lambda char: char != letter, data))


if __name__ == '__main__':
    __ban_a()
