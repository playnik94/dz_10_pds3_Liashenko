def my_function(a):
    try:
        a = int(input("Какой меся ? "))
    except ValueError as ex1:
        print(f'Нужна цыфра месяца: {ex1}')
    except Exception as ex:
        print(f'Unexpected: {ex1}')
    if a == 1:
        print("Январь ")
    if a == 2:
        print("Февраль ")
    if a == 3:
        print("Март ")
    if a == 4:
        print("Апрель" )
    if a == 5:
        print("Май")
    if a == 6:
        print("Июнь")
    if a == 7:
        print("Июль")
    if a == 8:
        print("Август")
    if a == 9:
        print("Сентябрь" )
    if a == 10:
        print("Октябрь")
    if a == 11:
        print("Ноябрь")
    if a == 12:
        print("Декабрь")

y = my_function(100)
