strr=str(input('Введите главную строку:'))
undstrr=str(input('Введите исключаемую строку:'))
try:
    last_occurrence=strr.rindex(undstrr)
    print(strr)
except ValueError:
    pass
else:
    strr=strr[:last_occurrence].replace(undstrr, "") + strr[last_occurrence:]
    print(strr)
