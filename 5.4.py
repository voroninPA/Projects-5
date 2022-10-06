import re
def auto_num(s):
    if re.fullmatch(r"[A-Za-z]{2}\d{3}[A-Za-z]{1}", s):
        print(s, 'Может быть автомобильным номером')
    else:
        print(s, 'НЕ может быть автомобильным номером')

x=str(input('Введите строку на проверку:'))
auto_num(x)
