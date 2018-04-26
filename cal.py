def perm():
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for k in range(4):
                if i == k or j == k:
                    continue
                l = 6 - i - j - k
                yield [i, j, k, l]


def main():
    line = input('Numbers:')
    nums = list(map(lambda x: int(x), line.split(' ')))

    calculator = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b,
                  '/': lambda a, b: a / b}

    for p in perm():
        for first in calculator.items():
            resulta = first[1](nums[p[0]], nums[p[1]])
            for second in calculator.items():
                resultb = second[1](resulta, nums[p[2]])
                for third in calculator.items():
                    resultc = third[1](resultb, nums[p[3]])
                    if resultc == 24:
                        print('{} {} {} {} {} {} {}'.format(nums[p[0]], first[0], nums[p[1]], second[0], nums[p[2]],
                                                            third[0], nums[p[3]]))


if __name__ == '__main__':
    main()