import timeit


def solution_original(integers):
    for i in range(len(integers) - 1):
        if integers[i] % 2 == integers[i + 1] % 2:
            continue
        else:
            try:
                if integers[i] % 2 == integers[i + 2] % 2:
                    return integers[i + 1]
                else:
                    return integers[i]
            except IndexError:
                return integers[i + 1]


def solution_pavel(ints):
    rule = ints[0] % 2 == 0 and ints[1] % 2 == 0 or \
           ints[0] % 2 == 0 and ints[2] % 2 == 0 or \
           ints[1] % 2 == 0 and ints[2] % 2 == 0
    for item in ints:
        if item % 2 == rule:
            return item


def solution_biskinis(integers):
    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n


def solution_g964(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


def solution_conq3r(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


if __name__ == '__main__':
    lst = list(range(0, 10000, 2)) + [13]
    for func in [solution_original, solution_pavel, solution_biskinis, solution_g964, solution_conq3r]:
        import_str = "from __main__ import lst, %s" % func.__name__
        res = timeit.timeit('%s(lst)' % func.__name__, number=100, setup=import_str)
        print(func.__name__.ljust(20), res)
