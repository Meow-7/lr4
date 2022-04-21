# Дано список чисел. Порахуйте, скільки в ньому пар елементів, рівних один одному. Вважається,
# що будь-які два елементи, рівні один одному, утворюють одну пару, яку необхідно порахувати.
s = str(input('enter string: '))


def count1_elements(s):
    two = 0
    for i in range(0, 10, 1):
        if s.count(str(i)) > 1:
            if s.count(str(i)) % 2 == 0:
                two = two + (s.count(str(i)) / 2)
            else:
                two = two + ((s.count(str(i)) - 1) / 2)
    print(two)


count1_elements(s)