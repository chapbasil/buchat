print("Здаров, братиш! Как сам?")
def zapas():
    b = input()
    a = b.lower()
    fz = open("zapas.txt", "r")
    text = fz.read()
    fz.close
    if a in text:
        print ("Дивно!")
    else:
        print ("Мммм, понятно. А что так?")
        с = input()
        print('Я бы не доверял.')
zapas()
print('Я много читаю прогнозов про УКраину на 2023 год. КАк считаетшь, это всё прекратится в 2023 году?')

def ukr():
    v = input()
    g = v.lower()
    fz2 = open("ukr.txt", "r")
    text = fz2.read()
    fz2.close
    if g in text:
        print ("Дивно! Но, думаю, ошибся, ведь никто же не знает точно!")
    elif "не" in g:
        print('Я бы не доверял.')
    else:
        print('Ошибся. Я бы не доверял.')
        w = input()
        for n in range(4):
            print ("Мммм, понятно. Всё равно ты ошибся.")
            с = input()
        
ukr()
print("Ясно. Ну, пока! Заходи ещё. буду рад видеть.")
