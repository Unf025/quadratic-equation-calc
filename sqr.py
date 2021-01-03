# Задачи
# Самое главное решить проблеммы с коментарием начинающимся на !!err
# 1. защита от дурака:
#	a. добавить условие при num не равном ни 1 ни 2, в котором будет вывдиться сообщение что введены неверные данные и пусть вводит их заново
#   б. добавить проверку первого коэффициента-если он равен нулю то алгоритм выдаст ошибку, нужно сказать юзеру что если а=0 то это уже не квадратное уравнение поскольку X^2 исчезнет 
#	в. так же в проверке можно определять если а=1 то уравнение приведенное, если b=0 или с=0 то уравнение не полное
# 2. выводить график функции (удалить все # !! uncom  и тогда появится пример)

import numpy as np # подключение крутой библиотеки numpy -https://pythonworld.ru/numpy/1.html. !!! поначалу может быть непонятно
import matplotlib.pyplot as plt # подключение крутой библиотеки  matplotlib - https://nbviewer.jupyter.org/github/whitehorn/Scientific_graphics_in_python/blob/master/P1%20Chapter%201%20Pyplot.ipynb

from math  import sqrt 
def MenuSelEquat():
	print("Выберите нужный пункт меню.")
	print("1. Решение квадратного уравнения.")
	print('2. Решение биквадратного уравнения.')
	print("EXIT")
	return input("")

num = MenuSelEquat()
def GetInputData():
    data  = { 'a' : int(input("a= ")), # поскольку из названии функции нам ясно что данные вводимые, то назовем словарь просто дата
              'b' : int(input("b= ")),
              'c' : int(input("c= "))            
    }
    return data # функция возвращает данный словарь. 



def SolvQuadEquat(input):
		d = input['b']**2 - 4 * input['a'] * input['c'] #Нахождение дискриминанта.
		print('Дискриминант = ', d) 
		if d > 0:
			print("2 корня")
			x1 = (-input['b'] + sqrt(d)) / (2*input['a']) # Нахождение корней.
			x2 = (-input['b'] - sqrt(d)) / (2*input['a'])
		elif d == 0:
			print("1 корень")
			x1 = -input['b']/(2*input['a'])
			x2 = None
		else:
			x1 = None
			x2 = None
			print('Нет действительных корней') # на самом деле корни есть, но они находяться на мнимой оси координат, которую в школе не проходят)	
		return ({"x1":x1,"x2":x2, "d":d}) 


while num != "exit":
	if num == '1': #Квадратное уравнение. 
		print("ax^2 + bx + c = 0") #Вид квадратного уравнения.

		input_data = GetInputData()
		
		result = SolvQuadEquat(input_data)
		print("Ответ:")
		print("x1= %.2f" % (result['x1']))
		print("x2= %.2f" % (result['x2']))
		#print("Ответ: x1= %.2f; x2= %.2f" % (result['x1'], result['x2']))

		
	elif num == '2': #Биквадратное уравнение
		print("ax^4 + bx^2 + c = 0") # Вид биквадратного уравнения. 
		print('x^2 = t')
		print('at^2 + bt + c = 0')
		input_data = GetInputData()
		
		result = SolvQuadEquat(input_data)
		print (result)

		if result ["d"] > 0:
			# биквадратное
			print("x^2= %.2f; x^2= %.2f" % (result['x1'], result['x2']))

			if result['x1'] > 0:
				print('x1=+- %.2f' % (sqrt(result['x1'])))#Вывод на экран корней.
			if result['x2'] > 0:
				print('x2=+- %.2f' % (sqrt(t2)))
				print("Ответ:" 'x1=+- %.2f;x2=+- %.2f' % (sqrt(result['x1']), sqrt(result['x2'])))
			else:
				print('Решений нет!')
		elif result ['d'] == 0: 
			# биквадратное
			print('x^2= ', t)
			print("x= ", sqrt(t))
		else:
			print('Нет действительных корней')
	else:
		print("Вы выбрали несуществующий пункт меню!")
	num = MenuSelEquat()