def train_1():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)


def train_2():
    list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
    sub_list = ['h', 'i', 'j']
    list1[2][1][2].extend(sub_list)
    print(list1)


def train_3():
    list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    maximum = -1
    for li in list1:
        if max(li) > maximum:
            maximum = max(li)
    print(maximum)


def train_4():
    list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    for li in list1:
        li.reverse()
    print(list1)


def train_5():
    list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    total = 0
    counter = 0
    for li in list1:
        total += sum(li)
        counter += len(li)
    print(total / counter)


if __name__ == '__main__':
    train_5()
