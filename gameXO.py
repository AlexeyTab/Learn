import random

Start = '''Игра крестики нолики.                # Правила игры здесь указаны
      Участники:
         Игрок, у него фишка – Х;
         Программа, у нее фишка – О.
      Правила:
         Первым всегда ходит Игрок.
         Игрок должен указать число от 1 до 9, которое соответствует свободному полю.
         Программа ставит свою фишку случайным образом.

         '''
print (Start)                                  # Покажем правила игры


FieldGame = {'R11':' ', 'R12':' ', 'R13':' ', 'R21':' ', 'R22':' ', 'R23':' ', 'R31':' ', 'R32':' ', 'R33':' '} # Ирговое поле, в виде справочника: место=ячейка (R**) и значения фишек в этом месте. В начале игры все места - пустые
Place=[1,2,3,4,5,6,7,8,9]               # Счетчик, для учета свободных мест на игровом поле, создаем список от 1 до 9


def gameResult(FieldGame):              # функция показа Игрового поля на экране  
    print('''Результат игры:''') 
    print(FieldGame['R11'],'|',FieldGame['R12'],'|',FieldGame['R13'],'|')     # Покажем значение фишки на месте игрового поля, разделив их вертикальной чертой
    print('--'*6)                                                             # Покажем просто линию 
    print(FieldGame['R21'],'|',FieldGame['R22'],'|',FieldGame['R23'],'|')
    print('--'*6)
    print(FieldGame['R31'],'|',FieldGame['R32'],'|',FieldGame['R33'],'|')


def finishGame(FieldGame):              # функция проверка на победу, на текущем игровом поле !!
    VictoryUser=['X','X','X']                   # эталонный список комбинации фишек для проверки победы Игрока
    VictoryComp=['O','O','O']                   # эталонный список комбинации  фишек для проверки победы Компа
    MatrixChip=[[FieldGame['R11'],FieldGame['R12'],FieldGame['R13']],[FieldGame['R21'],FieldGame['R22'],FieldGame['R23']],[FieldGame['R31'],FieldGame['R32'],FieldGame['R33']]]   # содаем матрицу (список в списке) со значениями фишек на каждом месте игрового поля
    Cell11=MatrixChip[0][0]                         # из матрицы извлекаем фишку в 1 ячейки  
    Cell21=MatrixChip[1][0]                         # из матрицы извлекаем фишки в 4 ячейки 
    Cell31=MatrixChip[2][0]                         # из матрицы извлекаем фишки в 7 ячейки  
    Сolumn1=[Cell11,Cell21,Cell31]                    # соберем список фишек первой колонки
    Cell12=MatrixChip[0][1]                         # из матрицы извлекаем фишки в во 2  ячейки (месте)
    Cell22=MatrixChip[1][1]                         # из матрицы извлекаем фишки в 5 ячейки 
    Cell32=MatrixChip[2][1]                         # из матрицы извлекаем фишки в 8 ячейки 
    Сolumn2=[Cell12,Cell22,Cell32]                    # соберемс писок фишек второй колонки
    Cell13=MatrixChip[0][2]                         # из матрицы извлекаем фишки в в 3 ячейки
    Cell23=MatrixChip[1][2]                         # из матрицы извлекаем фишки в 6 ячейки 
    Cell33=MatrixChip[2][2]                         # из матрицы извлекаем фишки в 9 ячейки 
    Сolumn3=[Cell13,Cell23,Cell33]                    # соберем список фишек третьей колонки
    Diagonal4=[Cell11,Cell22,Cell33]                    # соберем список фишек по диагонали 4
    Diagonal5=[Cell13,Cell22,Cell31]                    # соберем список фишек по диагонали 5
    if MatrixChip[0]==VictoryUser or MatrixChip[1]==VictoryUser or MatrixChip[2]==VictoryUser or Сolumn1==VictoryUser or Сolumn2==VictoryUser or Сolumn3==VictoryUser or Diagonal4==VictoryUser or Diagonal5==VictoryUser:  # сравниваем списки фишек с эталоном победы Пользователя
        ResultEnd=1                       # результат: ПОБЕДА ИГРОКА: если какой то список совпал с эталоным списком фишек Игрока: ряд 1-3, колонки 1-3, диагональ 4-5
    elif MatrixChip[0]==VictoryComp or MatrixChip[1]==VictoryComp or MatrixChip[2]==VictoryComp or Сolumn1==VictoryComp or Сolumn2==VictoryComp or Сolumn3==VictoryComp or Diagonal4==VictoryComp or Diagonal5==VictoryComp:  # сравниваем списки фишек с эталоном победы Компьютера
        ResultEnd=2                       # результат ПОБЕДА КОМПА: если какой то список совпал с эталоным списком  фишек Компа: ряд 1-3, колонки 1-3, диагональ 4-5
    else:
        ResultEnd=3                       # сравнение и чего не дало, значить результат НИЧЬЯ        
    return int(ResultEnd)                 # возвращаем результат функции

# ИГРА:
for step in range (1,11):               # запускаем шаги игры в диапазоне от 1 до 9
    if finishGame(FieldGame)==1:        # с помощью функции поверим, вдруг кто то уже победил. Если результат функции проверки н победу - 1 
        print ('ПОБЕДА ИГРОКА')         # сообщить о победе Игрока
        break                           # если результат 1, то прекратить игру 
    elif finishGame(FieldGame)==2:      # с помощью функции поверим, вдруг кто то уже победил. Если результат функции проверки н победу - 2
        print ('ПОБЕДА КОМПА')          # сообщить о победе Компа
        break                           # если результат 2, то прекратить игру 
    elif step==10:                      # если не получили результат 1 или 2 и дошли до 10 шага, значит счетчик свободных полей будет переполнен, поэтому  НИЧЬЯ
        print ('НИЧЬЯ')                 # сообщить о НИЧЬЕЙ
        break                           # прекратить игру, счетчик переполнен, т.к. мест для фишек больше нет 
    else:                               # никто не победил, и в счетчике есть свободные поля, играем дальше
        print ('''
                  Шаг'''+str(step)) 
        if (step % 2)==0:               # четный шаг, значит действует компьютер
            StepComp=random.choice(Place)      # Ход компьютера  - выбор случайного значения из оставшихся в игре свободных мест
            Place.remove(StepComp)             # удаляем Ход компьютера из списка свободных мест
            if StepComp==1:                    # если Ход компьютера - это место с №1
                FieldGame ['R11']='O'          # тогда на игровом поле ставим для места №1 значение "O"
                gameResult(FieldGame)          # покажем с помощью функции, Игровое поле на экране
            elif StepComp==2:
                FieldGame ['R12']='O'
                gameResult(FieldGame)   
            elif StepComp==3:
                FieldGame ['R13']='O'
                gameResult(FieldGame)   
            elif StepComp==4:
                FieldGame ['R21']='O'
                gameResult(FieldGame)    
            elif StepComp==5:
                FieldGame ['R22']='O'
                gameResult(FieldGame)   
            elif StepComp==6:
                FieldGame ['R23']='O'
                gameResult(FieldGame)   
            elif StepComp==7:
                FieldGame ['R31']='O'
                gameResult(FieldGame)   
            elif StepComp==8:
                FieldGame ['R32']='O'
                gameResult(FieldGame)   
            elif StepComp==9:
                FieldGame ['R33']='O'
                gameResult(FieldGame)   
        else:
            while True:                           # нечетный шаг, значит Игрок  
                print('Игрок, введите число от 1 до 9 (свобоное от фишек)')
                StepUser=int(input())                    # Игрок указывает место для своей фишки
                if StepUser in Place:                    # проверим, Игрок выбрал свободное место? 
                    if StepUser==1:                      # если Игрок указал место с №1
                        FieldGame ['R11'] ='X'           # тогда на игровом поле ставим для места №1 значение "X"
                        Place.remove (StepUser)          # удаляем Ход Игрока из списка свободных мест 
                        gameResult(FieldGame)            # покажем с помощью функции, Игровое поле на экране
                        break                            # т.к. ход игрока сделан, то все, можно к следующему ходу игры.
                    elif StepUser==2:
                        FieldGame ['R12'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)        
                        break
                    elif StepUser==3:
                        FieldGame ['R13'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    elif StepUser==4:
                        FieldGame ['R21'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    elif StepUser==5:
                        FieldGame ['R22'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    elif StepUser==6:
                        FieldGame ['R23'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    elif StepUser==7:
                        FieldGame ['R31'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    elif StepUser==8:
                        FieldGame ['R32'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    elif StepUser==9:
                        FieldGame ['R33'] ='X'
                        Place.remove (StepUser)
                        gameResult(FieldGame)
                        break
                    else:
                        err=1                      # вот я не знаю что здесь можно указать чтобы дальше работало, поэтому и присвоил белеберду. 
                else:
                    err=1

input()

