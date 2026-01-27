# Наследование это своего рода `полное внутреннее копирование класса`, со всеми его `атрибутами и методами`.
class A:
    class_attr = 10  # классовый атрибут

    def __init__(self, param):
        self.param = param  # экземплярный атрибут

    @classmethod
    def change_class_attr(cls, value):
        cls.class_attr = value

    def get_param(self):  # экземплярный метод
        return self.param


class B(A):  # Так происходит наследование, теперь в классе B есть все тоже самое, что и в классе A
    ...
    new_attr = 'Это классовый атрибут класса B'

    @staticmethod
    def hello():  # Добавили метод которого не было в классе A
        print("Привет из класса B")


if __name__ == "__main__":
    obj_a = A(20)
    obj_b = B(40)  # хотя мы и не писали __init__(self, param) в классе B, но оно полностью скопировалось из класса A

    print(obj_a.get_param())  # 20
    print(obj_b.get_param())  # 40  Скопировали все методы

    print(obj_a.class_attr)  # 10
    print(obj_b.class_attr)  # 10 Атрибуты тоже скопировались

    obj_a.change_class_attr(20)  # Изменили классовый атрибут класса А
    obj_b.change_class_attr(30)  # Изменили классовый атрибут класса B

    print(obj_a.class_attr)  # 20
    print(obj_b.class_attr)  # 30  Копирование есть копирование, даже классовых атрибутов, они теперь независимые

    print(obj_b.class_attr)  # 10 Есть атрибут скопированный из класса А
    print(obj_b.new_attr)  # 'Это классовый атрибут класса B' и новый атрибут которого нет в классе A

    print(obj_b.get_param())  # 40 Есть метод скопированный из класса А
    obj_b.hello()  # "Привет из класса B" и новый метод которого нет в классе A


