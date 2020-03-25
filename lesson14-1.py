# Реализовать свой класс исключения. Добавить метод записи в файл. Вызвать своё исключение и записать ошибку в файл.
class MyError(Exception):
    def __init__(self, text):
        self.txt = text
    def fr(self):
        my_file = open("some.txt", "a")
        my_file.write(self.txt)
        my_file.close()

a = input("Input positive integer: ")

try:
    a = int(a)
    if a < 0:
        raise MyError("You give negative!")
except ValueError:
    print("Error type of value!")
except MyError as mr:
    print(mr)
    mr.fr()

else:
    print(a)