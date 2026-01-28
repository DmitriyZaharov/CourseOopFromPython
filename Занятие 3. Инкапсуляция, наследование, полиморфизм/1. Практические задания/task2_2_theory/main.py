# Как наследуются защищенные и приватные атрибуты?
# Наследование защищенных и приватных атрибутов в Python имеет свои особенности,
# которые необходимо учитывать при разработке классов.
# Защищенные атрибуты обозначаются одним подчеркиванием (_) перед именем атрибута.
# Они не предназначены для прямого использования вне класса или его подклассов,
# но могут быть унаследованы и использованы в подклассах.
# Приватные атрибуты обозначаются двумя подчеркиваниями (__) перед именем атрибута.
# Они предназначены для внутреннего использования в классе и не должны быть доступны вне его.

class Parent:
    public_class_attr = 0
    _protected_class_attr = 1
    __private_class_attr = 2

    def __init__(self):
        self.public_attr = 3
        self._protected_attr = 4
        self.__private_attr = 5


class Child(Parent):
    def get_public_class_attr(self):
        return self.public_class_attr

    def get_protected_class_attr(self):
        return self._protected_class_attr

    def get_private_class_attr(self):
        return self.__private_class_attr

    def get_public_attr(self):
        return self.public_attr

    def get_protected_attr(self):
        return self._protected_attr

    def get_private_attr(self):
        return self.__private_attr


if __name__ == "__main__":
    child = Child()

    print(child.get_public_class_attr())  # 0
    print(child.get_protected_class_attr())  # 1

    try:
        print(child.get_private_class_attr())
    except AttributeError as err:
        print(err)  # 'Child' object has no attribute '_Child__private_class_attr'

    print(child.get_public_attr())  # 3
    print(child.get_protected_attr())  # 4

    try:
        print(child.get_private_attr())
    except AttributeError as err:
        print(err)  # 'Child' object has no attribute '_Child__private_attr'

# Как видно публичные и защищенные атрибуты свободно наследуются, тоже касается и методов, однако приватные
# атрибуты и методы не наследуются напрямую. Если публичные и защищенные атрибуты и методы копируются при наследовании,
# то приватные остаются с тем классом, где были созданы первоначально, в этом и есть смысл приватности.