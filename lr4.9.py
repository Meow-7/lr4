# Дано рядок, що містить принаймні один символ пробілу. Вивести підстроку, розташовану між
# першим і останнім пробілом початкового рядка. Якщо рядок містить тільки один пробіл, то вивести
# порожний рядок.
s = str(input('enter string: '))


def new_string(s):
    count = 0
    for c in s:
        if c == " ":
            count = count + 1
    if count == 1:
        print(" ")
    elif count == 0:
        print("String must have a space")
        exit(0)
    else:
        print(s[first:last])


count = 0
first = 0
last = 0
for c in s:
    count = count + 1
print(count)
for j in range(0, count-1, 1):
    if s[j] == " ":
        first = j
        break
for i in range(count-1, 0, -1):
    if s[i] == " ":
        last = i
        break


new_string(s)
