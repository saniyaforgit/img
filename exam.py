1. Условия if / elif / else

for num in range(start, end +1):
    if num % 3 == 0 and num % 5 ==0:
        print("Fizz Buzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

2. Логические операторы 

temp=int(input("Введите температуру: "))
if temp >20 and not "rain" == "да":
    print("Можно")
else:
    print("Лучше остаться дома")  

3. Циклы while и for  

цикл for используется, когда известна последовательность или количество итераций
Перебирает элементы (список, строку, кортеж, range)

Цикл while используется, когда неизвестно заранее количество повторений, а есть условие.
Работает до тех пор, пока условие истинно True.

4. Функция range()

num[]
for i in range(5):
num=float(input(f"Введите число {i+1}: "))
nums.append(num)

average=sum(nums) / len(nums)
print("Списек чисел:", nums)
print("Среднее число:", average)

5. Проход по строке 

s="Привет"
for ch in s:
    print(ch)

6. Списки (list)

names=["Alex","Lena","Danelya","Karima"]
names.append("Ailana")
print(names)  

a=[1,2,3]
a.insert(1,100)
print(a)

a=[5,10,15]
print(len(a))

7. Словари (dict)

1.ключ это имя по которому мы находим значение
2. int,float,str,bool,tuple
3. get/in 

student = {
    "name": "Dias",
    "age": 20
}
print(student.get("name"))      
print(student.get("grade"))     
print(student.get("grade", 0))  

d = {
    "id": 1,
    10: "ten",
    (1, 2): "tuple key",
    True: "yes"
}

if "key" in my_dict:
    value = my_dict["key"]


8. Кортежи (tuple)

1.tuple неизменяемый
2. list изменяемый

9. Основы ООП

Класс это шаблон,по которому создаются объекты
Объект это конкретный экземпляр. 

10. Инкапсуляция и наследование

Инкапсуляция это скрытые внутреней реализации объекта и предоставление данные через методы. 
Наследование это способность одного класса получать свойства и методы другого класса.

Задача 1 — Условия (if / elif / else)

nums=[10,20,30,40]
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

Задача 2 — Циклы + range

n=int(input("Введите число n: "))
total=0
for i in range(1,n+1):
    total+=i
print("Сумма чисел от 1 до ",n, "равна", total)

Задача 4 — list + dict

nums=[1,2,3,4,5,6,7,8,9,10]
result={"even":[],"odd":[]}
for num in nums:
    if num%2==0:
        result["even"].append(num)
    else:
        result["odd"].append(num)
for key,value in result.items():
    print(f"{key.capitalize()}:{",".join(map(str,value))}")

Задача 5 — Классы, инкапсуляция, наследование

class Character:
    def __init__(self, name, hp):
        self.name = name
        self._hp = hp 

    def take_damage(self, amount):
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0  

    def info(self):
        print(f"{self.name} — HP: {self._hp}")

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)  
        self.mana = mana

    def cast(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} cast a spell! Mana left: {self.mana}")
        else:
            print("not enough mana")


