## А как ведут себя свойства при наследовании?
# Свойства в Python ведут себя при наследовании аналогично обычным методам и атрибутам.
# Когда класс-наследник получает свойства от родительского класса, он может их использовать, переопределять, или даже дополнять.
#
# Рассмотрим, как это происходит:
#
# 1. Наследование свойства без изменений
# Если в классе-наследнике ничего не изменяется, то свойство будет использоваться так, как оно определено в родительском классе.

class Parent:
    @property
    def value(self):
        return "Value from Parent"

class Child(Parent):
    pass

child = Child()
print(child.value)  # Value from Parent

# 2. Переопределение свойства
# Класс-наследник может переопределить свойство, чтобы изменить его поведение.

class Parent:
    @property
    def value(self):
        return "Value from Parent"

class Child(Parent):
    @property
    def value(self):
        return "Value from Child"

child = Child()
print(child.value)  # Value from Child

# 3. Дополнение свойства
# Можно использовать метод `super()` для того, чтобы дополнить поведение родительского свойства.

class Parent:
    @property
    def value(self):
        return "Value from Parent"

class Child(Parent):
    @property
    def value(self):
        return super().value + " and Value from Child"

child = Child()
print(child.value)  # Value from Parent and Value from Child

# 4. Наследование сеттера и геттера
# Если у свойства есть и геттер, и сеттер, они также наследуются, но могут быть переопределены в классе-наследнике.

class Parent:
    def __init__(self):
        self._value = "Initial Value"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Child(Parent):
    @property
    def value(self):
        return super().value.upper()

    @value.setter
    def value(self, new_value):  # наследование сеттера достаточно специфично
        super(Child, type(self)).value.__set__(self, new_value + " (modified)")

child = Child()
child.value = "New Value"
print(child.value)  # NEW VALUE (MODIFIED)