calculator = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y, }

priority = {'+': 0,
            '-': 0,
            '*': 1,
            '/': 1,
            }


class Node:
    value = None
    left = None
    right = None

    def __init__(self, value=None):
        self.value = value

    def __abs__(self):
        if not self.value:
            return 0
        elif self.value in calculator:
            return calculator[self.value](abs(self.left), abs(self.right))
        else:
            return self.value

    def __repr__(self):
        if self.value in calculator.keys():
            return '{!r} {!r} {!r}'.format(self.value, self.left, self.right)
        else:
            return str(self.value)

    def __str__(self):
        if self.value in calculator.keys():
            if self.priority() > self.left.priority():
                left = '({})'.format(self.left)
            else:
                left = '{}'.format(self.left)
            if self.priority() >= self.right.priority():
                right = '({})'.format(self.right)
            else:
                right = '{}'.format(self.right)
            return '{} {} {}'.format(left, self.value, right)
        else:
            return str(self.value)

    def priority(self):
        if self.value == '*' or self.value == '/':
            return 1
        elif self.value == '+' or self.value == '-':
            return 0
        else:
            return 2


def build_tree(nums):

    all_set = {0, 1, 2, 3}

    for cal in calculator.keys():
        root = Node(cal)
        for left in calculator.keys():
            root.left = Node(left)
            for right in calculator.keys():
                root.right = Node(right)
                for first in all_set.copy():
                    root.left.left = Node(nums[first])
                    all_set.remove(first)
                    for second in all_set.copy():
                        root.left.right = Node(nums[second])
                        all_set.remove(second)
                        for third in all_set.copy():
                            root.right.left = Node(nums[third])
                            all_set.remove(third)
                            for fourth in all_set:
                                root.right.right = Node(nums[fourth])
                                yield root
                            all_set.add(third)
                        all_set.add(second)
                    all_set.add(first)

            for first in all_set.copy():
                root.right = Node(nums[first])
                all_set.remove(first)
                for leftleft in calculator.keys():
                    root.left.left = Node(leftleft)
                    for second in all_set.copy():
                        root.left.right = Node(nums[second])
                        all_set.remove(second)
                        for third in all_set.copy():
                            root.left.left.left = Node(nums[third])
                            all_set.remove(third)
                            for fourth in all_set:
                                root.left.left.right = Node(nums[fourth])
                                yield root
                            all_set.add(third)
                        all_set.add(second)
                all_set.add(first)


def main():
    line = input('Numbers:').strip()
    nums = list(map(lambda x: int(x), line.split(' ')))

    discovered = set()

    for tree in build_tree(nums):
        try:
            if abs(tree) == 24 and repr(tree) not in discovered:
                print(tree)
                discovered.add(repr(tree))
        except ZeroDivisionError:
            continue


if __name__ == '__main__':
    main()
