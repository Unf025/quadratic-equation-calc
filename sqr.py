# Тут был костян!
# При выборе меню под номером 1, вычисления происходят из меню 2.
# наши поезда самые поездатые поезда!
from math  import sqrt 

print("Выберите нужный пункт меню.")
print("1. Решение квадратного уравнения.")
print('2. Решение биквадратного уравнения.')

num = input("") #Ввод номера меню.
## как я понял он читает введенное с клавиатуры значение как строковое num='1'
## а ниже единица без апострофов '' значит проверяешь строковое значение num= '1' с числовым 1, а это разные типы
## Добавим скобки в проверку, говорит что теперь 1 не число а строковое значение и тогда они будут равны
if num == '1': #Квадратное уравнение. 
		print("ax^2 + bx + c = 0") #Вид квадратного уравнения.

		a = int(input("a= "))#Ввод 1го числа.
		b = int(input("b= "))#Ввод 2го числа .
		c = int(input("c= "))  #Ввод 3го числа.

		d = b**2 - 4 * a * c #Нахождение дискриминанта.
		print('Дискриминант = ', d) 
		if d > 0:
			print("2 корня")
			x1 = (-b + sqrt(d)) / (2*a) # Нахождение корней.
			x2 = (-b - sqrt(d)) / (2*a)
			print("x1= ", x1)
			print("x2= ", x2)
			print("Ответ: x1= %.2f; x2= %.2f" % (x1, x2))
		elif d == 0:
			print("1 корень")
			print('x=', -b/(2*a))# Нахождение единственного корня.
			print("Ответ: x= %.2f")		
		else:
			print('Корней не имеет!') 


elif num == '2': #Биквадратное уравнение
	print("ax^4 + bx^2 + c = 0") # Вид биквадратного уравнения. # Не работает(
		
a1= int(input("a= "))# Ввод чисел.
b1= int(input("b= "))
c1= int(input("c= "))
print('x^2 = t')
print('at^2 + bt + c = 0')
d1 = b1**2 - 4 * a1 * c1 #Нахождение дискриминанта.
print('Дискриминант = ', d1) 
if d1 > 0:
	print("2 корня")
	t1 = (-b1 + sqrt(d1)) / (2*a1) #Нахождение корней.
	t2 = (-b1 - sqrt(d1)) / (2*a1)
	print("t1= ", t1)
	print("t2= ", t2)
	print("x^2= %.2f; x^2= %.2f" % (t1, t2))
	if t1 > 0:
		print('x1=+- %.2f' % (sqrt(t1)))#Вывод на экран корней.
	if t2 > 0:
		print('x2=+- %.2f' % (sqrt(t2)))
		print("Ответ:" 'x1=+- %.2f;x2=+- %.2f' % (sqrt(t1), sqrt(t2)) )
	else:
		print('Решений нет!')
elif d1 == 0:
	print("1 корень")
	t= -b1/(2*a1)
	print('t=', -b1/(2*a1))#Нахождение единстветнного корня.
	print('x^2= ', t)
	print("x= ", sqrt(t))
else:
	print('Корней не имеет!')
