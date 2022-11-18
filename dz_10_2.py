import sys

try:
    a = [0/0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 12, фывфыв,  11, 12, 13, 14, 15, 18, 12, 12, 19, 20]
    count = 0
    for i in a:
        if i == 12:
            count += 1
    else:
        print('цифр 12 в списке', count)

except ZeroDivisionError as ex1:
    print(f'На ноль : {ex1}', file=sys.stderr)

except Exception as ex2:
    print(f'допустимы только цыфры: {ex2}', file=sys.stderr)
