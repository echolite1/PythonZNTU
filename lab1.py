class Person:
    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя
 
    def __del__(self):
        print("Object", self.name,"deleted\n")
    def display_info(self):
        print("Привет, меня зовут", self.name)
 
 
person1 = Person("Tom")
print("New object created")
person1.display_info()  # Привет, меня зовут Tom
del person1     # удаление из памяти


person2 = Person("Sam")
print("New object created")
person2.display_info()  # Привет, меня зовут Sam
del person2     # удаление из памяти



