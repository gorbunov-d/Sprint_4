import pytest
from main import BooksCollector

# 1. Проверка добавления новой книги (валидное имя)
def test_add_new_book_adds_book():
    collector = BooksCollector()
    collector.add_new_book('Гарри Поттер')
    assert 'Гарри Поттер' in collector.get_books_genre()
    assert collector.get_book_genre('Гарри Поттер') == ''

# 2. Проверка, что нельзя добавить книгу с длинным именем (>40 символов)
def test_add_new_book_too_long_name():
    collector = BooksCollector()
    long_name = 'A' * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()

# 3. Проверка, что нельзя добавить одну и ту же книгу дважды
def test_add_new_book_duplicate():
    collector = BooksCollector()
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Гарри Поттер')
    assert list(collector.get_books_genre().keys()).count('Гарри Поттер') == 1

# 4. Проверка установки жанра книге (валидный жанр)
@pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы'])
def test_set_book_genre_valid(genre):
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', genre)
    assert collector.get_book_genre('Книга') == genre

# 5. Проверка, что жанр не устанавливается, если жанр невалидный
def test_set_book_genre_invalid_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Неизвестный жанр')
    assert collector.get_book_genre('Книга') == ''

# 6. Проверка получения книг по жанру
def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга1')
    collector.add_new_book('Книга2')
    collector.add_new_book('Книга3')
    collector.set_book_genre('Книга1', 'Фантастика')
    collector.set_book_genre('Книга2', 'Детективы')
    collector.set_book_genre('Книга3', 'Фантастика')
    assert set(collector.get_books_with_specific_genre('Фантастика')) == {'Книга1', 'Книга3'}
    assert set(collector.get_books_with_specific_genre('Детективы')) == {'Книга2'}

# Новый тест: Проверка метода get_book_genre
def test_get_book_genre_returns_correct_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга1')
    collector.set_book_genre('Книга1', 'Фантастика')
    assert collector.get_book_genre('Книга1') == 'Фантастика'

# Новый тест: Проверка метода get_books_genre
def test_get_books_genre_returns_all_books_with_genres():
    collector = BooksCollector()
    collector.add_new_book('Книга1')
    collector.add_new_book('Книга2')
    collector.set_book_genre('Книга1', 'Фантастика')
    collector.set_book_genre('Книга2', 'Детективы')
    assert collector.get_books_genre() == {'Книга1': 'Фантастика', 'Книга2': 'Детективы'}

# 7. Проверка, что книги с возрастным рейтингом не попадают в get_books_for_children
def test_get_books_for_children_excludes_age_rating():
    collector = BooksCollector()
    collector.add_new_book('Детектив')
    collector.add_new_book('Мультфильм')
    collector.set_book_genre('Детектив', 'Детективы')
    collector.set_book_genre('Мультфильм', 'Мультфильмы')
    children_books = collector.get_books_for_children()
    assert 'Детектив' not in children_books
    assert 'Мультфильм' in children_books

# 8. Проверка добавления книги в избранное
def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    assert 'Книга' in collector.get_list_of_favorites_books()

# 9. Проверка, что нельзя добавить в избранное несуществующую книгу
def test_add_book_in_favorites_not_in_collection():
    collector = BooksCollector()
    collector.add_book_in_favorites('Несуществующая')
    assert 'Несуществующая' not in collector.get_list_of_favorites_books()

# 10. Проверка удаления книги из избранного
def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.delete_book_from_favorites('Книга')
    assert 'Книга' not in collector.get_list_of_favorites_books()
