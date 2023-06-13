def train_1():
    countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
    last = countries[-1]
    print(last)


def train_2():
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    print(primes[:6])


def train_3():
    countries = (
    'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon'
    )
    print(countries[2:])


def train_4():
    countries = (
    'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon'
    )
    print(countries[:-3])


def train_5():
    countries = (
    'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon'
    )
    print(countries[3:-2])


def train_6():
    countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
    number = len(countries)
    print(number)


def train_7():
    numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
    mini, maxi = min(numbers), max(numbers)
    print(mini + maxi)


def train_8():
    countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
    index = countries.index('Slovenia')
    print(index)


def train_9():
    countries = (
    'Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia',
    'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon'
    )
    number = countries.count('Spain')
    print(number)


def train_10():
    numbers1 = (1, 2, 3)
    numbers2 = (6,)
    numbers3 = (7, 8, 9, 10, 11, 12, 13)
    res = 2 * numbers1 + 9 * numbers2 + numbers3
    print(res)


def train_11():
    city_name = input()
    city_year = int(input())
    city = (city_name, city_year)
    print(city)


def train_12():
    tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
    non_empty_tuples = [nested_tuple for nested_tuple in tuples if len(nested_tuple) != 0]
    print(non_empty_tuples)


def train_13():
    tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
    new_tuples = [nested_tuple[:-1] + (100, ) for nested_tuple in tuples]
    print(new_tuples)


if __name__ == '__main__':
    train_13()
