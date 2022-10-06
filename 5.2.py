def sentence(x):
    #x=x.strip()
    #print(x)
    #x=x.lower()
    #print(x)
    x=x.capitalize()
    print(x)
    while x.endswith('!') == True or x.endswith('?') == True or x.endswith('.') == True:
        x=x[:len(x) - 1]
    if x.endswith('.') == False:
        x=x+'.'
    print(x)

x = str(input('Введите предложение:'))
sentence(x)
