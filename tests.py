import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book_success(collector):
    collector.add_new_book("Алиса в стране чудес")
    assert "Алиса в стране чудес" in collector.get_books_genre()

def test_add_new_book_fail_long_name(collector):
    collector.add_new_book("A" * 41)
    assert "A" * 41 not in collector.get_books_genre()

def test_add_new_book_fail_existing_book(collector):
    collector.add_new_book("Алиса в стране чудес")
    collector.add_new_book("Алиса в стране чудес")
    assert len(collector.get_books_genre()) == 1

def test_set_book_genre(collector):
    collector.add_new_book("Алиса в стране чудес")
    collector.set_book_genre("Алиса в стране чудес", "Фантастика")
    assert collector.get_book_genre("Алиса в стране чудес") == "Фантастика"

def test_get_book_genre_not_existing(collector):
    assert collector.get_book_genre("Неизвестная книга") is None

def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Алиса в стране чудес")
    collector.set_book_genre("Алиса в стране чудес", "Фантастика")
    books = collector.get_books_with_specific_genre("Фантастика")
    assert "Алиса в стране чудес" in books

def test_get_books_for_children(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    books_for_children = collector.get_books_for_children()
    assert "Гарри Поттер" in books_for_children

def test_add_book_in_favorites(collector):
    collector.add_new_book("Алиса в стране чудес")
    collector.add_book_in_favorites("Алиса в стране чудес")
    assert "Алиса в стране чудес" in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites(collector):
    collector.add_new_book("Алиса в стране чудес")
    collector.add_book_in_favorites("Алиса в стране чудес")
    collector.delete_book_from_favorites("Алиса в стране чудес")
    assert "Алиса в стране чудес" not in collector.get_list_of_favorites_books()

@pytest.mark.parametrize("name", ["", " "])
def test_add_new_book_fail_empty_name(collector, name):
    collector.add_new_book(name)
    assert "Алиса в стране чудес" not in collector.get_books_genre()

@pytest.mark.parametrize("genre", ["Фантастика", "NonExistingGenre"])
def test_set_book_genre_non_existing(collector, genre):
    collector.add_new_book("Алиса в стране чудес")
    collector.set_book_genre("Алиса в стране чудес", genre)
    expected_genre = genre if genre in collector.genre else ""
    assert collector.get_book_genre("Алиса в стране чудес") == expected_genre
