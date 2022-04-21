# Дано список. Виведіть ті його елементи, які зустрічаються в списку тільки один раз. Елементи
# потрібно виводити в тому порядку, в якому вони зустрічаються в списку.
s = str(input('enter string: '))


def count1_elements(s):
    count = 0
    for c in s:
        count = count + 1
    for i in range(0, count, 1):
        if s.count(s[i]) == 1:
            print(s[i])


count1_elements(s)
