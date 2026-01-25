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


# TODO Импортируйте и скопируйте ранее написанный класс Book
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

class Library:

    def __init__(self, books=None):
        """
        Не забудьте про 'Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь
        его не передал, то библиотека инициализируется с пустым списком книг.'
        :param books:
        """
        """
         Конструктор класса Library.

         Args:
             books (list, optional): Список книг для инициализации библиотеки. 
                                    Если не передан, используется пустой список.
         """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Необходимо узнать последнюю книгу в библиотеке, посмотреть атрибут 'id' этой книги и вернуть следующее
        значение после этого `id`
        :return:
        """
        pass # TODO дописать метод
        """   
        Возвращает идентификатор для добавления новой книги.

        Returns:
            int: 1 если библиотека пуста, иначе id последней книги + 1
        """
        if not self.books:
            return 1
        # Предполагаем, что у каждой книги есть атрибут 'id'
        last_book_id = self.books[-1].get('id') if isinstance(self.books[-1], dict) else self.books[-1].id
        return last_book_id + 1

    def get_index_by_book_id(self, id_):
        """
        Так как в библиотеке книги хранятся в списке, то данная функция возвращает индекс где книга с определенным
        `id` хранится в списке книг. Для примера. [Book(id=1, ...), Book(id=2, ...)] книга с id=2 хранится
        на индексе 1 списка книг
        :param id_: id книги
        :return: индекс, где лежит книга в списке книг
        """
        pass # TODO дописать метод
        """
        Возвращает индекс книги в списке по её идентификатору.
        Args:
            book_id (int): Идентификатор искомой книги
        Returns:
            int: Индекс книги в списке
        Raises:
            ValueError: Если книги с указанным id не существует
        """
        for index, book in enumerate(self.books):
            current_id = book.get('id') if isinstance(book, dict) else book.id
            if current_id == id_:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

    # Пример 3: Попытка найти несуществующую книгу
    # try:
    #     library_with_books.get_index_by_book_id(10)
    # except ValueError as e:
    #     print(e)  # "Книги с запрашиваемым id не существует"
