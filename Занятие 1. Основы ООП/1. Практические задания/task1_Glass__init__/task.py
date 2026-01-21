from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError ("Объем стакана должен быть типом int или float")
        if capacity_volume <= 0:
            raise ValueError ("Объем стакана должен быть больше 0")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError ("Заполненный объем должен быть типом int или float")
        if occupied_volume < 0:
            raise ValueError ("Заполненный объем должен быть больше 0")
        if occupied_volume > capacity_volume:
            raise ValueError ("Заполненный объем должен быть меньше объема стакана")
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    glass_1 = Glass(500, 200)
    glass_2 = Glass(700, 500)
    try:
        ...  # TODO инициализировать не корректные объекты
        glass_3 = Glass(500, 700)
        glass_4 = Glass(-600, 300)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


