# TODO Написать 3 класса с документацией и аннотацией типов
from book import Book
from vehicle import Vehicle
from social_media_account import SocialMediaAccount

if __name__ == "__main__":

    # Использование класса Book
    my_book = Book("Война и мир", 1225, "Лев Толстой")
    print(f"Время чтения: {my_book.get_reading_time(30)} часов")

    # Использование класса Vehicle
    my_car = Vehicle("Tesla", 250, 80)
    print(f"Может проехать 500 км: {my_car.can_travel(500, 100)}")

    # Использование класса SocialMediaAccount
    my_account = SocialMediaAccount("coder123", followers=150)
    my_account.publish_post("Мой первый пост!")
    my_account.publish_post("Мой второй пост!")
    my_account.publish_post("Мой третий пост!")
    print(f"Постов: {my_account.posts_count}")


# Запуск doctests для проверки примеров:
#
# bash:
# python -m doctest book.py -v
# python -m doctest vehicle.py -v
# python -m doctest social_media_account.py -v