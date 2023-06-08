def list_1():
    n = int(input())
    list1 = [list(range(1, n + 1)) for _ in range(n)]
    for li in list1:
        print(li)


def list_2():
    n = int(input())
    list1 = [list(range(1, i + 2)) for i in range(n)]
    for li in list1:
        print(li)


def pascal_1():
    def pascal(i):
        if i == 0 or i == 1:
            return [1] * (i + 1)
        pred = pascal(i - 1)
        res = [1]
        for i in range(len(pred) - 1):
            res.append(pred[i] + pred[i + 1])
        res.append(1)
        return res

    n = int(input())
    print(pascal(n))


def pascal_2():
    def pascal(i):
        if i == 0:
            print(1)
            return [1]
        pred = pascal(i - 1)
        res = [1]
        for i in range(len(pred) - 1):
            res.append(pred[i] + pred[i + 1])
        res.append(1)
        print(*res)
        return res

    n = int(input())
    pascal(n - 1)


def packing_duplicates():
    inp = input().split()
    res = []
    for char in inp:
        if res and char in res[-1]:
            res[-1].append(char)
        else:
            res.append([char])
    print(res)


def chunking():
    def chunked(char_list, n):
        res = []
        for i in range(0, len(char_list), n):
            res.append(char_list[i:(i + n)])
        return res

    print(chunked(input().split(), int(input())))


def sublists_list():
    inp = input().split()
    res = [[]]
    for length in range(1, len(inp) + 1):
        for i in range(len(inp) - length + 1):
            res.append(inp[i:(i + length)])
    print(res)


if __name__ == '__main__':
    sublists_list()
