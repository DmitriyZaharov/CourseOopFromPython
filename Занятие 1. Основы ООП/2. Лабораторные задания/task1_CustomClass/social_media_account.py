import doctest

class SocialMediaAccount:
    """
    Абстрактный класс, представляющий аккаунт в социальной сети.

    Атрибуты:
        username: Имя пользователя (должно быть уникальным в системе)
        followers: Количество подписчиков (>= 0)
        posts_count: Количество опубликованных постов (>= 0)
    """

    def __init__(self, username: str, followers: int = 0, posts_count: int = 0) -> None:
        """
        Инициализирует объект аккаунта в социальной сети.

        Args:
            username: Имя пользователя (не может быть пустым)
            followers: Количество подписчиков (по умолчанию 0)
            posts_count: Количество постов (по умолчанию 0)

        Raises:
            ValueError: Если имя пользователя пустое или количество подписчиков/постов отрицательное

        >>> account = SocialMediaAccount("john_doe", 150, 25)
        >>> account.username
        'john_doe'
        >>> account.followers
        150
        """
        if not username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        if followers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным")
        if posts_count < 0:
            raise ValueError("Количество постов не может быть отрицательным")

        self.username = username
        self.followers = followers
        self.posts_count = posts_count

    def publish_post(self, content: str) -> int:
        """
        Публикует новый пост.

        Args:
            content: Текст поста (не может быть пустым и должен содержать не более 1000 символов)

        Returns:
            Новое общее количество постов

        Raises:
            ValueError: Если текст поста пустой или слишком длинный

        >>> account = SocialMediaAccount("test_user")
        >>> account.publish_post("Привет, мир!")
        1
        >>> account.posts_count
        1

        >>> account.publish_post("")
        Traceback (most recent call last):
            ...
        ValueError: Текст поста не может быть пустым
        """
        if not content.strip():
            raise ValueError("Текст поста не может быть пустым")

        if len(content) > 1000:
            raise ValueError("Текст поста не может превышать 1000 символов")

        self.posts_count += 1
        return self.posts_count

    def gain_followers(self, count: int) -> int:
        """
        Увеличивает количество подписчиков.

        Args:
            count: Количество новых подписчиков (> 0)

        Returns:
            Новое общее количество подписчиков

        Raises:
            ValueError: Если количество новых подписчиков <= 0

        >>> account = SocialMediaAccount("user", 100)
        >>> account.gain_followers(50)
        150

        >>> account.gain_followers(0)
        Traceback (most recent call last):
            ...
        ValueError: Количество новых подписчиков должно быть положительным
        """
        if count <= 0:
            raise ValueError("Количество новых подписчиков должно быть положительным")

        self.followers += count
        return self.followers

    def calculate_engagement_rate(self, likes_per_post: float, comments_per_post: float) -> float:
        """
        Рассчитывает уровень вовлеченности аудитории.

        Args:
            likes_per_post: Среднее количество лайков на пост (>= 0)
            comments_per_post: Среднее количество комментариев на пост (>= 0)

        Returns:
            Уровень вовлеченности в процентах

        Raises:
            ValueError: Если значения лайков или комментариев отрицательные

        >>> account = SocialMediaAccount("influencer", 1000, 10)
        >>> account.calculate_engagement_rate(150, 25)
        17.5

        >>> account.calculate_engagement_rate(-10, 25)
        Traceback (most recent call last):
            ...
        ValueError: Количество лайков не может быть отрицательным
        """
        if likes_per_post < 0:
            raise ValueError("Количество лайков не может быть отрицательным")
        if comments_per_post < 0:
            raise ValueError("Количество комментариев не может быть отрицательным")

        if self.followers == 0:
            return 0.0

        total_interactions = likes_per_post + comments_per_post
        engagement_rate = (total_interactions / self.followers) * 100

        return engagement_rate


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

# Ввести в терминале: "python -m doctest social_media_account.py -v"