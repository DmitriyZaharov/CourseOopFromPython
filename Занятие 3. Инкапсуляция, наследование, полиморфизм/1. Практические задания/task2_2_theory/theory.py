class Parent:
    __private_class_attr = 2

    def __init__(self):
        self.__private_attr = 'Parent'

    def get_private_attr(self):
        return self.__private_attr

    @classmethod
    def get_private_class_attr(cls):
        return cls.__private_class_attr


class Child(Parent):
    def get_private_child_attr(self):
        return self.__private_attr

    @classmethod
    def get_private_class_child_attr(cls):
        return cls.__private_class_attr


if __name__ == "__main__":
    child = Child()

    print(child.get_private_class_attr())  # 2
    try:
        print(child.get_private_class_child_attr())
    except AttributeError as err:
        print(err)

    print(child.get_private_attr())  # Parent

    try:
        print(child.get_private_child_attr())
    except AttributeError as err:
        print(err)

# В данном коде созданы методы в классе Parent и методы в классе Child.
# И те и те возвращают приватные атрибуты экземплярные и классовые, но как видно через наследование и методы можно
# получить доступ к приватному атрибуту родителя, но вот у дочернего не создается приватного атрибута,
# как по примеру защищенного.
# Приватные атрибуты или методы чаще всего используются если необходимо гарантировать,
# что атрибуты или методы класса не будут случайно изменены или использованы в подклассах или извне.