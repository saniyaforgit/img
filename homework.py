# temperature=int(input("Введите температуру воздуха: "))
# if temperature > 0:
#     print("На улице тепло")
# else:
#     print("На улице холодно")

# password=int(input("Введите пароль: "))
# if password == 1234:
#     print("Пароль верный!")
# else:
#     print("Пароль неверный!")

# number=int(input("Введите число: "))
# if number>100:
#     print("Число больше 100")
# else:
#     print("Число не больше 100 или равно")
# 
# number=int(input("Введите число: "))
# if number % 2 == 0:
#     print(f"Число {number} - четное")
# else:
#     print(f"Число {number} - нечетное")

# name=input("Введите имя: ")
# age=int(input("Введите возраст: "))
# if age <= 18:
#     print(f"\n Привет, {name}! Ты еще школьник")
# else:
#     print(f"\n Привет, {name}! Ты уже студент")
# 
# num=int(input("Введите число: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# else:
#     print("Число не делится на 3 и 5 одновременно")  

# day=input("Введите день недели: ")
# if day=="Saturday" or day == "Sunday":
#     print("Сегодня выходной!")
# else:
#     print("Сегодня будний день!")

# temp=int(input("Введите температуру: "))
# if temp >20 and not "rain" == "да":
#     print("Можно")
# else:
#     print("Лучше остаться дома")       

# age=int(input("Введите возраст: "))
# if age <=0:
#     print("Некорректный возраст")
# elif age <=5:
#     print("Ребенок")
# elif age <=17:
#     print("Школьник")    
# else:
#     print("Взрослый")

# name=input("Введите имя: ")
# if name not in ["Admin" , "Root"]:
#     print("Имя допустимо")
# else:
#     print("Имя недопустимо")

# tempa=int(input("Введите температуру: "))
# if tempa <=0 or tempa >=35:
#     print("Экстремальная погода")
# else:
#     print("Погода нормальная")

# user=input("Введите имя: ")
# password=int(input("Введите пароль: "))
# if user=="admin" and password ==1234:
#     print("Вход разрешен!")
# else:
#     print("вход запрещен!")

# ticket=input("Имеется ли у вас билет?(да/нет): ")
# invitation=input("Имеетсяли у вас приглашение?(да/нет): ")
# if ticket =="да" or invitation=="да":
#     print("Допустимо")
# else:
#     print("Недопустимо")

# user=input("Введите имя: ")
# if user!="admin":
#     print("Вход разрешен")
# else:
#     print("Вход запрещен")

# age=int(input("Введите возраст: "))
# ban=input("Вы заблокированный? (да/нет): ")
# if age>=18 and not ban=="да":
#     print("Вход разрешен")
# else:
#     print("Вход запрещен")

# temp=int(input("Введите температуру: "))
# rain=input("Есть ли дождь или ветер? (да/нет): ")
# wind=input("Есть ли ветер? (да/нет): ")
# if temp>=15 and temp <=25 and rain !="да" and wind != "да":
#     print("Погода комфортная")
# else:
#     print("Лучше остаться дома")

# age=int(input("Введите ваш возраст: "))
# application=input("Подана ли заявка? (да/нет): ")
# finalist=input("Вы финалист? (да/нет): ")
# if age >=14 and application == "да" or finalist == "да":
#     print("Допустимо")
# else:
#     print("Недопустимо")

# week=int(input("Введите номер дня недели (1-7): "))
# if week ==1:
#     print("Понедельник")
# elif week==2:
#     print("Вторник")
# elif week==3:
#     print("Среда")
# elif week==4:
#     print("Четверг")
# elif week==5:
#     print("Пятница")
# elif week==6:
#     print("Суббота")
# elif week==7:
#     print("Воскресенье")
# else:
#     print("Такого дня недели нет")

# mounth=int(input("Введите номер месяца(1-12):"))
# mounths=["январь", "февраль", "март", "апрель","май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
# if mounth > 1 and mounth <= 12:
#     print(mounths [mounth-1])
# else:
#     print("Такого месяца нет")

# num=int(input("Введите число: "))
# if num >=0:
#     print("Number is positive")
# elif num <=0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")

# a=int(input("Введите первое число: "))
# b=int(input("Введите второе число: "))
# if a==b:
#     print("Числа равны")
# else:
#     if a<b:
#         print(a,b)
#     else:
#         print(b,a)
# 

# start=int(input("Введите начало диапазона: "))
# end=int(input("Введите конец диапазона: "))
# for num in range(start, end+1):
#     if num %7==0:
#         print(num)

# start=int(input("Введите начало диапазона: "))
# end=int(input("Введите конец диапазона: "))

# print("Все числа диапазона")
# for num in range(start,end+1):
#     print(num, end = " ")
# print()

# print("Все числа диапазона в убывающем порядке")
# for num in range(start, end -1, -1):
#     print(num,end = " ")
# print() 

# for num in range(start, end+1):
#     if num %7 == 0:
#         print(num, end = " ")
#     print()

# count=0
# for num in range(start, end +1):
#     if num % 5 == 0:
#         count +=1
# print("Количество чисел кратных 5:, count")

# start=int(input("Введите начало диапазона: "))
# end=int(input("Введите конец диапазона: "))

# for num in range(start, end +1):
#     if num % 3 == 0 and num % 5 ==0:
#         print("Fizz Buzz")
#     elif num % 3 ==0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# ; total=0

# ; while True:
# ;     print("\n---------МИНИ КАССА---------")
# ;     print("Меню:")
# ;     print("1 - Добавить товар")
# ;     print("2 - Показать общую сумму")
# ;     print(" 3 - Оплатить")
# ;     print("4 - Выход")

# ;     choice=int(input("Выберите пункт: "))
# ;     if choice==1:
# ;         name=input("\nВведите название товара: ")
# ;         if name == "":
# ;             print("Название не может быть пустым!")
# ;             continue

# ;         try:
# ;             price=int(input("Введите цену: "))
# ;         except ValueError:
# ;             print("Цена должна быть числом!")
# ;             continue

# ;         if price<0:
# ;             print("Цена не может быть отрицательной")
# ;             continue
        
# ;         total+=price
# ;         print(f"Товар добавлен! Текущая сумма: {total}")

# ;     elif choice == 2:
# ;         print(f"\nТекущая сумма всех товаров: {total}")

# ;     elif choice == 3:
# ;         print(f"\nИтого к оплате: {total}")
# ;         print("Оплачено!")
# ;         total = 0
    
# ;     elif choice == 4:
# ;         print("\nВыход из программы. До свидания!")
# ;         break

# ;     else:
# ;         print("Неверный пункт меню! Выберите снова.")


# nums=[10,30,44,17,3]
# print(nums[0])
# print(nums[-1])

# names=["Alex","Lena","Danelya","Karima"]
# names.append("Ailana")
# print(names)
    
# fruits=["banana", "mango", "apple"]
# fruits.insert(1,"apple")
# print(fruits)


# names=["Alex","Lena","Danelya","Dias","Karima"]
# names.remove("Dias")
# print(names)
        
# nums=[10,30,44,17,3]
# nums.pop()
# print(nums)

# fruits=["banana", "mango", "apple"]
# fruits.clear()
# print(fruits)

# fruits=["banana", "mango", "молоко", "apple"]
# index_of_milk = fruits.index("молоко")
# print(index_of_milk)

# nums=[10,30,5,44,17,5,5,3]
# count_of_fives= nums.count(5)
# print(count_of_fives)           

# nums=[10,30,5,44,17,5,5,3]
# print(nums.count(5))


# names=["Alex","Lena","Danelya","Dias","Karima"]
# names.sort()
# print("По возрастанию:",names)

# names.sort(reverse=True)
# print("По убыванию:", names)

# fruits=["banana", "mango", "молоко", "apple"]
# fruits.reverse()
# print(fruits)


# fruits=["banana", "mango", "молоко", "apple"]
# fruits_copy = fruits.copy()
# fruits_copy.append("orange")
# fruits_copy.remove("молоко")
# print("Оригинальный список:",fruits)
# print("Копия после изменения:",fruits_copy)

# nums=[10,30,5,44,17,5,5,3]
# total = sum(nums)
# print("Сумма всех чисел:", total)

# nums=[-10,-30,5,-44,17,-5,-5,-3]
# for num in nums:
#     if num > 0:
#         print(num)

# nums=[10,30,5,44,17,5,5,3]
# nums.extend([11,12])
# print(nums)


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     for element in row:
#         print(element,end=" ")
#     print()    

# nums=[10,30,5,44,17,5,5,3]
# total_sum=sum(nums)
# print("Сумма всех чисел:", total_sum)


# nums=[5,2,9,1]
# nums.sort()
# minimum=nums[0]
# maximum=nums[-1]
# print("Отсортированный список:", nums)
# print("Минимальный элемент:", minimum)
# print("Максимальный элемент:", maximum)

# nums=[]

# for i in range(5):
#     num=float(input(f"Введите число {i+1}: "))
#     nums.append(num)

#     average=sum(nums) / len(nums)
#     print("Списек чисел:", nums)
#     print("Среднее число:", average)


# names=["Alex","Lena","Danelya","Dias","Karima"]
# for name in names:
#     if len (name)>5: 
#         print(name)


# nums=[5,20,33,10,11,24]
# for num in nums[:]:
#     if num < 10:
#         nums.remove(num)
# print("Числа >=10:", nums)

# nums=[50, 75, 90, 100, 60]
# count_high_nums=0
# for num in nums:
#     if num>80:
#         count_high_nums +=1
# print("Количество оценок не меньше 80:", count_high_nums)        


# list1=[1,2,3]
# list2=[4,5,6]

# combined_list=list1+list2 
# print(combined_list)

# list1=[1,2,3]
# list2=[4,5,6]

# combined_list=list1.copy()
# combined_list.extend(list2)
# print(combined_list)

# nums=[10,20,30,40,50]
# squared_nums=[num**2 for num in nums]
# print(squared_nums)

# words=["apple","banana","strawberry","kiwi","orange"]
# longest_word=max(words,key=len)
# print(longest_word)


# items=[1,None,22,None,2,3,None,500]
# while None in items:
#     items.remove(None)
# print(items)    

# colors=["синий","коричневый","белый","фиолетовый"]
# print("Первый цвет:",colors[0])
# print("Последний цвет:",colors[-1])

# point=(4,7)
# x,y=point
# print("x=",x)
# print("y=",y)

# nums=[1,2,3]
# nums_tuple=tuple(nums)

# print("Кортеж:", nums_tuple)
# print("Тип:",type(nums_tuple))

# students=[
#     ("Анна", 20,95),
#     ("Иван", 19,88),
#     ("Мария",21,90),
#     ("Олег", 20,90),
#     ("Дмитрий", 22,85)

# ]

# for student in students:
#     if student[2]>=90:
#         print(student[0])

# nums=(1,2,3,5,50,5)
# if 5 in nums:
#     print("Есть")
# else:
#     print("Нет")