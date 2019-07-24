from random import randint as rand

post = [1, 0]
quiting = False
sot = ["сложение", "вычитание", "макс. сумма", "way", "прав.отв", "не прав. отв", "пропущ."]
alright = False
saving = [True, False]

print ("Начало работы программы...")
print ("""\nПрограмма поддерживает управление пользователем.
В поле для ответа введите ответ на задачу или одну из существующих команд:
\"Пропустить" - если пример слишком трудный, его можно пропустить (учитывается в статистике);
\"Настройки\" - возможность изменить максимальную сумму;
\"Статус\" - отображение настроек и количество правильно решённых примеров;
\"Стереть прогресс\" - удаление статистики решённых примеров;
\"Включить/выключить сложение\";
\"Включить/выключить вычитание\";
\"Выйти\" - завершить работу программы. \n""")

try:
    blok = open ("TrNuSettings.txt", "r")
    allsod = (blok.readlines())
    for i in range(4):
        if allsod[i].endswith ("\n"):
            ling = len(allsod[i])
            sot[i] = int ((allsod[i])[:ling-1])
        else:
            sot[i] = int (allsod[i])
    blok.close()
except (NameError, FileNotFoundError, ValueError, IndexError):
    print ("Ошибка при воспроизведении настроек")
    
if (((sot[0] == 1) or (sot[0] == 0)) and
    ((sot[1] == 1) or (sot[1] == 0)) and
    ((sot[3] == 1) or (sot[3] == 2) or (sot[3] == 3)) and
    (sot[2] > 0)):
        alright = True
        post[0] = sot[0]
        post[1] = sot[1]
        mol_1 = sot[2]
        way = sot[3]
if alright == False:
    print ("Файл отсутствует или деформирован, установить дефолтные настройки? ")
    anss = input ("Ответ пользователя: ")
    anss = anss.lower()
    if anss == ('да'):
        blok = open ("TrNuSettings.txt", "w")
        blok.write (str(1) + "\n" +
                    str(0) + "\n" +
                    str(25) + "\n" +
                    str(1))
        blok.close()
        post[0] = int (1)
        post[1] = int (0)
        mol_1 = int (25)
        way = int (1)
    else:
        quiting = True

        
try:
    res = open ("TrNuStatistics.txt", "r")
    stats = (res.readlines())
    for i in range(3):
        if stats[i].endswith ("\n"):
            ling = len(stats[i])
            sot[4+i] = int ((stats[i])[:ling-1])
        else:
            sot[4+i] = int (stats[i])
    res.close()
except (FileNotFoundError):
    res = open ("TrNuStatistics.txt", "w")
    res.write (str(0) + "\n" + str(0) + "\n" + str(0))
    res.close()
    print ("Файл с сохранённым прогрессом отсутствует. Создан новый")
    for i in range(3):
        sot[4+i] = 0
except (NameError, ValueError, IndexError):
    print ("Файл с сохранённым прогрессом не подлежит чтению, прогресс обнулён")
    for i in range(3):
        sot[4+i] = 0
if (sot[4] < 0) or (sot[5] < 0) or (sot[6] < 0):
    print ("Файл с сохранённым прогрессом деформирован, прогресс обнулён")
    sot[4] = 0
    sot[5] = 0
    sot[6] = 0   


#функции
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def settings (x):
    while True:
        try:
            x = int (input('\n' + "Введите новое значение максимальной суммы: "))
            break
        except ValueError:
            print ("Требуется ввести число, повторите попытку")
    return x

while True:
    if quiting == True:
        break    
    s = rand (1, mol_1)
    a = rand (1, s)
    b = s - a
    if (post[0] == 0) and (post[1] == 0):
        way = 3
        print ("\nСложение и вычитание выключено, примеры не генерируются")
    if (post[0] == 1) and (post[1] == 1):
        way = rand(1, 2)
    if (way == 1):
        print (' ')
        prim = print (a, '+', b)
        prim = (str (a) + ' + ' + str (b))
    elif (way == 2):
        print (' ')
        print (s,  '-', b)
        prim = (str (s) + ' - ' + str (b))

    while True:
        if quiting == True:
            break
        ans = (input("Ответ пользователя: "))
        try:
            ans = int (ans)
        except ValueError:
            ans = str (ans.lower())
        if (way == 1) and (ans == (a+b)):
            print ("Верно!")
            sot[4] += 1
            break
        elif (way == 2) and (ans == (s-b)):
            print ("Верно!")
            sot[4] += 1
            break
        elif (isint(ans)):
            sot[5] += 1
            print ("Не верно, попробуй снова\n" + "\n" + prim)

        elif ans == ("выйти"):
            while True:
                if saving[0] == True:
                    print ("\nСохранить настройки генерации перед выходом?")
                    wha1 = (input ("Ответ пользователя: "))
                    wha1 = (wha1.lower())
                    if wha1 == ("да"):
                        saving[0] = False
                        saving[1] = True
                        blok = open ("TrNuSettings.txt", "w")
                        blok.write (str(post[0]) + "\n" +
                                    str(post[1]) + "\n" +
                                    str(mol_1) + "\n" +
                                    str (way))
                        blok.close()
                    elif wha1 == ("нет"):
                        saving[0] = False
                        saving[1] = True
                    else:
                        print ("Неверный синтаксис, повторите попытку")
                if saving [1] == True:
                    print ("\nСохранить прогресс правильно решённых примеров?")
                    wha2 = (input ("Ответ пользователя: "))
                    wha2 = (wha2.lower())
                    if wha2 == ("да"):
                        res = open ("TrNuStatistics.txt", "w")
                        res.write (str(sot[4]) + "\n" +
                                   str(sot[5]) + "\n" +
                                   str(sot[6]))
                        res.close()
                        quiting = True
                        break
                    elif wha2 == ("нет"):
                        quiting = True
                        break        
                    else:
                        print ("Неверный синтаксис, повторите попытку")

        elif ans == ("настройки"):
            mol_1 = settings (mol_1)
            break

        elif ans == ("пропустить"):
            print ("Пример пропущен. Действие учтено статистикой")
            sot[6] += 1
            break
    
        elif ans == ("включить вычитание"):
            if way == 3:
                way = 2
            post[1] = 1
            break

        elif ans == ("выключить вычитание"):
            way = 1
            post[1] = 0
            break

        elif ans == ("включить сложение"):
            if way == 3:
                way = 1
            post[0] = 1
            break

        elif ans == ("выключить сложение"):
            way = 2
            post[0] = 0
            break

        elif ans == ("стереть прогресс"):
            sot[4] = 0
            sot[5] = 0
            sot[6] = 0
            print ("Прогресс был успешно обнулён")
            break
        
        elif ans == ("статус"):
            print ("Максимальная сумма: ", mol_1)
            if post[0] == 1:
                print ("Сложение включено")
            elif post[0] == 0:
                print ("Сложение выключено")
            if post[1] == 1:
                print ("Вычетание включено")
            elif post[1] == 0:
                print ("Вычитание выключено")
            print ("Всего решённых примеров: {0}, из них правильно: {1}, неправильно: {2}, пропущено: {3}".format(sot[4]+sot[5]+sot[6], sot[4], sot[5], sot[6]))
            try:
                print ("Процентное соотношение правильно решённых примеров: {0}%".format(round(sot[4]/(sot[4]+sot[5]+sot[6])*100, 2)))
            except (ZeroDivisionError):
                print ("Статистика правильно решённых примеров недоступна")
            print ("\nОбратно к задаче: ")
            

        else:
            print ("Несуществующий запрос, повторите попытку")

input ("Конец программы, нажмите Enter для выхода")
