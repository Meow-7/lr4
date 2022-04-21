# Дано непорожній рядок S. Вивести рядок, що містить символи рядка S, між якими вставлено по
# одному пробілу.
s = str(input('enter string: '))


def string_with_spaces(s):
    for c in s:
        print(c, end=" ")


string_with_spaces(s)
