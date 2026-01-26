# База данных книг для проверки
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """Конструктор класса Book.

        Args:
            id_ (int): Идентификатор книги
            name (str): Название книги
            pages (int): Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги в формате 'Книга "название_книги"'.

        Returns:
            str: Строковое представление книги
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        Returns:
            str: Строка для инициализации экземпляра
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Выводим информацию о книгах
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
    # print(repr(list_books))  # Вызов метода __repr__


