# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#                       ЗАДАЧИ ПО ПРОГРАММИРОВАНИЮ
#                               ПО ГЛАВАМ
# Книга: Начинаем программировать на Python. Тони Гэддис. 4-е издание. 2019г.
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#                   Глава 4. Структуры с повторением
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 1. Сборщик ошибок. Сборщик ошибок собирает ошибки каждый день в течение
# пяти дней.  Напишите программу, которая ведет учет нарастающего итога ошибок,
# собранных в течение пяти дней. Цикл должен запрашивать количество ошибок,
# собираемых в течение каждого дня, и когда цикл завершается, программа должна
# вывести общее количество собранных ошибок.

# mistakes = 0.0    # аккумулятор (переменная для накоплений)
#
# for i in range(1, 6):
#     print('Количество ошибок', i, 'дня', end='')
#     mistake = int(input(': '))
#     mistakes += mistake
#
# print('Количество ошибок за 5 дней - ', int(mistakes))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 2. Сожженные калории. Бег на беговой дорожке позволяет сжигать 4,2 калорий
# в минуту.Напишите программу, которая применяет цикл для вывода количества
# калорий, сожженных после 10, 15, 20, 25 и 30 минут бега.

# calories_in_minute = 4.2
#
# for i in range(10,31,5):
#     calories = i * calories_in_minute
#     print('После', i, 'минут бега сожжется', calories, 'калория')
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 3. Анализ бюджета. Напишите программу, которая просит пользователя ввести
# сумму, выделенную им на один месяц. Затем цикл должен предложить пользователю
# ввести суммы отдельных статей его расходов за месяц и подсчитать их
# нарастающим итогом. По завершению цикла программа должна вывести сэкономленную
# или перерасходованную сумму.

# budget = float(input('Введите сумму, выделенную на один месяц: '))
# sum = 0.0     # аккумулятор (сумма трат)
# print('ВВедите сумму, выделенную на расход или 0 для прекращения ввода!')
#
# running = True
#
# while running:
#     expenses = int(input('ВВедите сумму, выделенную на расход: '))
#     sum += expenses
#
#     if expenses == 0:    # Выход из программы
#         running = False
#
# # Высчитываю сэкономили или превысили бюджет в этом месяце
# if budget >= sum:   # если бюджет > трат
#     difference = budget - sum   # остаток бюджета после трат
#     print('Вы сэкономили в этом месяце', difference, 'рублей')
# else:
#     # остаток бюджета после трат (чтобы минуса не было)
#     difference = sum - budget
#     print('Вы превысили бюджет в этом месяце на', difference, 'рублей')
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 4. Пройденное расстояние. Пройденное транспортным средством расстояние можно
# вычислить следующим образом:
#             расстояние = скорость x время.
# Например, если поезд движется со скоростью 90 км/ч в течение трех часов, то
# пройденное расстояние составит 270 км. Напишите программу, которая запрашивает
# у пользователя скорость транспортного средства (в км/ч) и количество часов,
# которое оно двигалось. Затем она должна применить цикл для вывода расстояния,
# пройденного транспортным средством для каждого часа этого периода времени.
# Вот пример требуемого результата:
#
# Какая скорость транспортного средства в км/ч? 40 [Enter]
# Сколько часов оно двигалось? 3 [Enter]
# Час     Пройденное расстояние
# ------------------------------
# 1               40
# 2               80
# 3              120

# Запрос данных от пользователя
# speed = int(input('Какая скорость транспортного средства в км/ч? '))
# time = int(input('Сколко часов она двигалось? '))
#
# print('Час', 'Пройденное расстояние', sep = '\t')
# print('---------------------------')
#
# speed_hour = speed / time     # расстояние за 1 час
# for t in range(1, time + 1):
#     speed_hours = speed_hour * t   # расстояние за 1 час * за каждый час
#     print(t, int(speed_hours), sep='\t\t')
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 5. Средняя толщина дождевых осадков. Напишите программу, которая применяет
# вложенные циклы для сбора данных и вычисления средней толщины дождевых осадков
# за ряд лет. Программа должна сначала запросить количество лет. Внешний цикл
# будет выполнять одну итерацию для каждого года. Внутренний цикл будет делать
# двенадцать итераций, одну для каждого месяца. Каждая итерация внутреннего цикла
# запрашивает у пользователя миллиметры дождевых осадков в течение этого месяца.
# После всех итераций программа должна вывести количество месяцев, общее количество
# миллиметров дождевых осадков и среднюю толщину дождевых осадков в месяц в течение
# всего периода.

# years = int(input('Введите количество лет: '))
# o_m = 0.0     # аккумулятор (общее кол-во мм осадков)
#
# for y in range(1, years+1):    # итерация каждого года
#     for m in range(1, 13):    # итерация каждого месяца
#         print('Введите миллиметры дождевых осадков в течение',
#               y, 'года', m, 'месяца', end='')
#         mm = float(
#             input(': '))    # ввод данных по осадкам
#         o_m += mm     # прибавление каждого данного по осадкам к общему кол-ву
#
# Вычисление среднего кол-ва мм осадков
# average_mm = o_m / (y * m)
#
# Вывод результатов
# print('Количество месяцев -', y * m)
# print('Общее количество миллиметров дождевых осадков', o_m, 'мм')
# print('Среднюю толщину дождевых осадков в месяц в течение всего периода',
#       format(average_mm, '.1f'), 'мм')
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 6. Таблица соответствия между градусами Цельсия и градусами Фаренгейта.
# Напишите программу, которая выводит таблицу температур по шкале Цельсия от 0
# до 20 и их эквиваленты по Фаренгейту. Формула преобразования температуры из шкалы
# Цельсия в шкалу Фаренгейта:
#                               F=(9/5)*C+32,
# где F - это температура по шкале Фаренгейта; С - температура по шкале Цельсия.
# Для вывода этой таблицы ваша программа должна применить цикл.

# print('Градусы по шкалам (эквивалентны):')
# print('Цельсия', '\t', 'Фаренгейта')
# print('----------------------------')
#
# for t in range(1,21):
#     far = (9/5) * t + 32   # перевод градусов в другую шкалу
#     print(t, '\t\t', format(far, '.1f'))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 7. Мелкая монета для зарплаты. Напишите программу, которая вычисляет сумму денег,
# которую человек заработает в течение периода времени, если в первый день его
# зарплата составит одну копейку, во второй день две копейки и каждый последующий
# день будет удваиваться. Программа должна запросить у пользователя количество дней,
# вывести таблицу, показывающую зарплату за каждый день, и затем показать заработную
# плату до налоговых и прочих удержаний в конце периода. Итоговый результат должен
# быть выведен в рублях, а не в количестве копеек.

# # Данные
# days = int(input('Введите количество рабочих дней: '))
# salary = 0.0    # аккумулятор (суммарная зарплата)
# f_salary = 0.01   # (1 копейка) начальная зарплата
#
# # Начало таблицы
# print('День', '\t', 'Зарплата')
# print(1, '\t',f_salary, 'копеек') # запись в таблицу первой зарплаты
#
# # Начинаю удвоение, считая со 2 дня (+ запись в таблицу)
# for d in range(2, days + 1):
#     salary += f_salary  # к зп прибавляется ежедневно заработанное
#     f_salary *=2    # предыдущая зарплата удваивается
#     print(d, '\t', format(f_salary, '.2f'), 'копеек')
#
# all_salary = salary + f_salary # прибавляю 1 день зарплаты
# all_salary /= 100    # переводим из копеек в рубли
#
# print('Итоговая зарплата составляет', format(all_salary, '.2f'), 'рублей')
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 8. Сумма чисел. Напишите программу с циклом, которая просит пользователя ввести ряд
# положительных чисел. Пользователь должен ввести отрицательное число в качестве
# сигнала конца числового ряда. После того как все положительные числа будут введены,
# программа должна вывести их сумму.

# print('Предупреждение!')
# print('Для прекращения ввода чисел нужно ввести отрицательное число!')
# print('')
#
# sum = 0.0       # аккумулятор (суммирующие положит-ые числа)
# enter = float(input('Введите положительное число: '))
# sum += enter
#
# while enter > 0:
#         enter = float(input('Введите положительное число: '))
#         sum += enter
#         if enter < 0:
#            sum -= enter  # чтобы не суммировалось введенное отриц-ое число
#         elif enter == 0:
#             print('Ноль не является положительным числом!')
#             enter = float(input('Введите положительное число: '))
# print(sum)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 9. Уровень океана. Допустим, что уровень океана в настоящее время повышается
# примерно на 1,6 мм в год. С учетом этого создайте приложение, которое
# выводит количество миллиметров, на которые океан будет подниматься каждый
# год в течение следующих 25 лет.

# all = 0.0     # аккумулятор (кол-во мм повышения уровня океана)
# mm = 1.6
# print('Год', '\t', 'Повышение уровня окана на')
#
# for i in range(1, 26):
#     all += mm
#     print(i, '\t',format(all, '.1f'), 'mm')
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 10. Рост платы за обучение. В заданном университете обучение студента-очника
# составляет 45 000 рублей в семестр. Было объявлено, что плата за обучение
# будет повышаться на 3% каждый год в течение следующих 5 лет. Напишите
# программу с циклом, который выводит плановую сумму за обучение в семестр
# в течение следующих 5 лет.

# payment = 45000 * 2 # 2 семестра в году
# upp = 0.03  # повышение на 3%
# print('Год', '\t', 'Плата')
#
# for i in range(1,6):
#     payment = payment * (1 + upp)   # формула повышения
#     print(i, '\t', format(payment,'.1f'))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 11. Потеря массы. Если умеренно активный человек будет сокращать свое
# потребление в калориях на 500 калорий в день, то, как правило, он может
# похудеть примерно на 1,5 кг в месяц. Напишите программу, которая позволяет
# пользователю ввести его исходную массу и затем создает и выводит таблицу,
# показывающую, каким будет его ожидаемая масса в конце каждого месяца
# в течение следующих 6 месяцев, если он останется на этой диете.

# initial_body = float(input('Введите массу своего тела: '))
# loss = 1.5        # 1.5кг потеря каждый месяц
# print('Месяц', '\t', 'Вес, кг')
#
# for i in range(1,7):      # 6 месяцев
#     initial_body -= loss
#     print(i, '\t', initial_body)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 12. Вычисление факториала числа. В математике запись в форме п! обозначает
# факториал неотрицательного целого числа п. Факториал n - это произведение
# всех неотрицательных целых чисел от 1 до п. Например,
#   7! = 1 х 2 х 3 х 4 х 5 х 6 х 7 = 5040
#                   и
#       4! = 1 х 2 х 3 х 4 = 24.
# Напишите программу, которая позволяет пользователю ввести неотрицательное
# целое число и затем применяет цикл для вычисления факториала этого числа
# и показывает факториал.

# number = int(input('Введите неотрицательное целое число! '))
# f = 1
#
# if number < 0:
#     print('Факториал неотрицательного числа не существует!')
# elif number == 0:
#     print('Факториал нуля равен 1')
# else:
#     for n in range(1, number + 1):
#         f *= n
#
# print(str(number) + '! =', f)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 13. Популяция. Напишите программу, которая предсказывает приблизительный
# размер популяции организмов. Приложение должно использовать текстовые поля,
# чтобы дать пользователю ввести стартовое количество организмов,
# среднесуточное увеличение популяции (как процент) и количество дней,
# которые организмам будет дано на размножение. Например, допустим, что
# пользователь вводит приведенные ниже значения:
# • стартовое количество: 2;
# • среднесуточное увеличение: 30%;
# • количество дней для размножения: 10.
# Программа должна вывести показанную ниже таблицу данных:
# День    Популяция
# 1       2
# 2       2,6
# 3       3,38
# 4       4,394
# 5       5,7122
# 6       7,42586
# 7       9,653619
# 8       12,5497
# 9       16,31462
# 10      21,209

# number = int(input('Введите стартовое количество организмов: '))
# population = int(input('Введите среднесуточное увеличение популяции (в %): '))
# days = int(input('Введите количество дней для размножения: '))
#
# population = population / 100   # перевожу из проценты в десятичную дробь
#
# # Начало таблицы
# print('День', '\t', 'Популяция')
# print(1, '\t', number)  # в 1 день остается стартовое кол-во
#
# for d in range(2, days + 1):
#     number = number * (1 + population)
#     print(d, '\t', format(number, '.3f'))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# 14. Напишите программу, которая применяет вложенные циклы для рисования
# этого узора:
# *******
# ******
# *****
# ****
# ***
# **
# *

# for i in range(7, 0, -1):   # пересчет от 7 до 1 (столбики)
#     for c in range(i):  # в каждом столбике выводится кол-во '*' (от 7 до 1)
#         print('*', end="")
#     print()
# ------------------------------------------------------------

# ----------------------------------------------------------------------------
# 15. Напишите программу, которая применяет вложенные циклы для рисования
# этого узора:
#       ##
#       # #
#       #  #
#       #   #
#       #    #
#       #     #

# for i in range(7):      # 7 строк (от 0 до 6)
#     print('#', end='')      # в начале каждой строки выводится '#'
#     # На каждой строке выводится кол-во элементов равное номеру строки (от 0 до 6)
#     for c in range(i):
#         print(' ', end='')      # вывод ' ' в каждой строке определенное кол-во
#     print('#')  # в конце каждой строки выводится '#'
# ----------------------------------------------------------------------------
