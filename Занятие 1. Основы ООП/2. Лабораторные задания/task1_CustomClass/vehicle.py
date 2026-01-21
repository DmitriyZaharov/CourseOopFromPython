import doctest

class Vehicle:
    """
    Абстрактный класс, представляющий транспортное средство.

    Атрибуты:
        brand: Марка транспортного средства
        max_speed: Максимальная скорость в км/ч (должна быть >= 0)
        fuel_level: Уровень топлива в процентах (0-100)
    """

    def __init__(self, brand: str, max_speed: float, fuel_level: float) -> None:
        """
        Инициализирует объект транспортного средства.

        Args:
            brand: Марка транспортного средства
            max_speed: Максимальная скорость в км/ч (>= 0)
            fuel_level: Уровень топлива в процентах (0-100)

        Raises:
            ValueError: Если скорость < 0 или уровень топлива вне диапазона 0-100

        >>> car = Vehicle("Toyota", 180.5, 75.0)
        >>> car.brand
        'Toyota'
        >>> car.max_speed
        180.5
        """
        if not brand.strip():
            raise ValueError("Марка транспортного средства не может быть пустой")
        if max_speed < 0:
            raise ValueError("Максимальная скорость не может быть отрицательной")
        if fuel_level < 0 or fuel_level > 100:
            raise ValueError("Уровень топлива должен быть в диапазоне от 0 до 100")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel_level = fuel_level

    def travel_distance(self, hours: float, speed: float) -> float:
        """
        Рассчитывает пройденное расстояние за указанное время.

        Args:
            hours: Количество часов в пути (>= 0)
            speed: Скорость движения в км/ч (0 <= speed <= max_speed)

        Returns:
            Пройденное расстояние в километрах

        Raises:
            ValueError: Если время < 0 или скорость вне допустимого диапазона

        >>> vehicle = Vehicle("Test", 120, 50)
        >>> vehicle.travel_distance(2, 60)
        120

        >>> vehicle.travel_distance(2, 150)
        Traceback (most recent call last):
            ...
        ValueError: Скорость 150 превышает максимальную скорость 120
        """
        if hours < 0:
            raise ValueError("Время в пути не может быть отрицательным")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if speed > self.max_speed:
            raise ValueError(f"Скорость {speed} превышает максимальную скорость {self.max_speed}")

        return hours * speed

    def refuel(self, amount: float) -> float:
        """
        Заправляет транспортное средство.

        Args:
            amount: Количество топлива для добавления в процентах (> 0)

        Returns:
            Новый уровень топлива

        Raises:
            ValueError: Если количество топлива <= 0 или превышает 100%

        >>> vehicle = Vehicle("Test", 100, 50)
        >>> vehicle.refuel(30)
        80

        >>> vehicle.refuel(60)
        Traceback (most recent call last):
            ...
        ValueError: Заправка приведет к переполнению бака (текущий уровень: 80)
        """
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным")

        new_level = self.fuel_level + amount
        if new_level > 100:
            raise ValueError(f"Заправка приведет к переполнению бака (текущий уровень: {self.fuel_level})")

        self.fuel_level = new_level
        return self.fuel_level

    def can_travel(self, distance: float, average_speed: float) -> tuple[bool, str]:
        """
        Проверяет, может ли транспортное средство преодолеть указанное расстояние.

        Args:
            distance: Расстояние в километрах (>= 0)
            average_speed: Средняя скорость в км/ч (0 <= speed <= max_speed)

        Returns:
            Кортеж (может_ли_преодолеть, причина_если_нет)

        >>> vehicle = Vehicle("Test", 100, 50)
        >>> vehicle.can_travel(200, 80)
        (True, '')

        >>> vehicle.can_travel(1000, 90)
        (False, 'Недостаточно топлива')
        """
        if distance < 0:
            return False, "Расстояние не может быть отрицательным"

        if average_speed > self.max_speed:
            return False, f"Скорость {average_speed} превышает максимальную {self.max_speed}"

        # Предполагаем, что расход топлива зависит от скорости
        required_fuel = distance * (average_speed / 100) * 0.1

        if required_fuel > self.fuel_level:
            return False, "Недостаточно топлива"

        return True, ""

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации

    # Ввести в терминале: "python - m doctest - v vehicle.py"