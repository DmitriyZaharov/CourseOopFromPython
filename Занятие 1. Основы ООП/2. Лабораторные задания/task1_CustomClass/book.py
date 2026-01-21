import doctest

class Book:
    """
    Абстрактный класс, представляющий книгу.

    Атрибуты:
        title: Название книги
        pages: Количество страниц (должно быть положительным числом)
        author: Автор книги
    """

    def __init__(self, title: str, pages: int, author: str) -> None:
        """
        Инициализирует объект книги.

        Args:
            title: Название книги
            pages: Количество страниц (должно быть > 0)
            author: Автор книги

        Raises:
            ValueError: Если количество страниц <= 0 или название/автор пустые

        >>> book = Book("1984", 328, "George Orwell")
        >>> book.title
        '1984'
        >>> book.pages
        328
        """
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        if not author.strip():
            raise ValueError("Автор книги не может быть пустым")

        self.title = title
        self.pages = pages
        self.author = author

    def read_page(self, page_number: int) -> str:
        """
        Возвращает содержимое указанной страницы.

        Args:
            page_number: Номер страницы для чтения (1 <= page_number <= pages)

        Returns:
            Строку с содержимым страницы

        Raises:
            ValueError: Если номер страницы вне допустимого диапазона

        >>> book = Book("Test Book", 100, "Test Author")
        >>> book.read_page(50)
        'Содержимое страницы 50 из книги "Test Book"'

        >>> book.read_page(150)
        Traceback (most recent call last):
            ...
        ValueError: Страницы 150 не существует в книге на 100 страниц
        """
        if page_number < 1 or page_number > self.pages:
            raise ValueError(f"Страницы {page_number} не существует в книге на {self.pages} страниц")

        return f'Содержимое страницы {page_number} из книги "{self.title}"'

    def get_reading_time(self, pages_per_hour: int) -> float:
        """
        Рассчитывает время чтения книги.

        Args:
            pages_per_hour: Скорость чтения в страницах в час (должна быть > 0)

        Returns:
            Количество часов, необходимое для прочтения книги

        Raises:
            ValueError: Если скорость чтения <= 0

        >>> book = Book("Long Book", 300, "Author")
        >>> book.get_reading_time(50)
        6.0

        >>> book.get_reading_time(0)
        Traceback (most recent call last):
            ...
        ValueError: Скорость чтения должна быть положительной
        """
        if pages_per_hour <= 0:
            raise ValueError("Скорость чтения должна быть положительной")

        return self.pages / pages_per_hour

    def get_book_info(self) -> dict:
        """
        Возвращает информацию о книге в виде словаря.

        Returns:
            Словарь с информацией о книге

        >>> book = Book("Sample", 200, "Writer")
        >>> info = book.get_book_info()
        >>> info["title"]
        'Sample'
        >>> info["pages"]
        200
        """
        return {
            "title": self.title,
            "pages": self.pages,
            "author": self.author
        }

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

   # Ввести в терминале: "python -m doctest -v book.py"