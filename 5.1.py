k=1
while k:
    print('Введите название файла для проверки:')
    x = str(input())
    if(x==''):
        print('Вы вышли из программы')
        break
    count = 0
    for char in x:
        if '<' in x or '>' in x or '/' in x or '\'' in x or '|' in x or '?' in x:
            print(x,'Не может быть именем файла типа .txt .doc .docx .odt .rtf')
            count+=1
            break
    if count==0:
        print(x,' может быть именем файла типа .txt .doc .docx .odt .rtf')
