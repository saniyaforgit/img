class Person:
    def __init__(self, name: str, age: int):
        self.__name = name     
        self.__age = age       
    
    def get_name(self):
        return self.__name

   
    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age < 0 or age > 120:
            print("Ошибка: возраст должен быть от 0 до 120")
            return
        self.__age = age
