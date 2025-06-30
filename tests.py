import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book('5 Элемент')
        assert '5 Элемент' in collector.books_genre

    @pytest.mark.parametrize("book_name", ["", "Очень длинное название фильма. Ну прям очеееень длинное"])
    def test_add_new_book_invalid_names(self, book_name, collector):
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_set_book_genre_valid_name(self, collector):
        collector.add_new_book('5 Элемент')
        collector.set_book_genre('5 Элемент', 'Фантастика')
        assert collector.books_genre['5 Элемент'] == 'Фантастика'

    def test_set_book_genre_does_not_accept_invalid_genre(self, collector):
        collector.add_new_book('Наруто')
        collector.set_book_genre('Наруто', 'Анимэ')
        assert collector.books_genre['Наруто'] == ''

    def test_set_book_genre_none_book(self, collector):
        collector.set_book_genre('Жигало', 'Фантастика')
        assert 'Жигало' not in collector.books_genre

    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('5 Элемент')
        collector.set_book_genre('5 Элемент', 'Фантастика')
        assert collector.get_book_genre('5 Элемент') == 'Фантастика'

    def test_get_book_genre_returns_none_for_unknown_book(self, collector):
        assert collector.get_book_genre('Жигало') is None

    def test_get_books_with_specific_genre_specific_genre(self, collector):
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        result = collector.get_books_with_specific_genre('Ужасы')
        assert result == ['Чужой']

    def test_get_books_with_specific_genre_invalid_specific_genre(self, collector):
        collector.add_new_book('Наруто')
        collector.set_book_genre('Наруто', 'Анимэ')
        result = collector.get_books_with_specific_genre('Анимэ')
        assert result == []

    def test_get_books_genre_returns_empty_dict(self, collector):
        result = collector.get_books_genre()
        assert result == {}

    def test_get_books_genre_returns_correct_dict(self, collector):
        collector.add_new_book('5 Элемент')
        collector.set_book_genre('5 Элемент', 'Фантастика')
        expected = {'5 Элемент': 'Фантастика'}
        result = collector.get_books_genre()
        assert result == expected

    def test_get_books_for_children_only_child_genre(self, collector):
        collector.add_new_book('5 Элемент')
        collector.set_book_genre('5 Элемент', 'Фантастика')
        expected = ['5 Элемент']
        result = collector.get_books_for_children()
        assert result == expected

    def test_get_books_for_children_not_child_genre(self, collector):
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        expected = []
        result = collector.get_books_for_children()
        assert result == expected

    def test_add_book_in_favorites_valid_book_if_book_not_add(self, collector):
        collector.add_new_book('5 Элемент')
        collector.add_book_in_favorites('5 Элемент')
        assert collector.favorites == ['5 Элемент']

    def test_add_book_in_favorites_valid_book_if_book_already_add(self, collector):
        collector.add_new_book('5 Элемент')
        collector.add_book_in_favorites('5 Элемент')
        collector.add_book_in_favorites('5 Элемент')
        assert collector.favorites == ['5 Элемент']

    def test_add_book_in_favorites_invalid_book(self, collector):
        collector.add_new_book('5 Элемент')
        collector.add_book_in_favorites('Наруто')
        assert collector.favorites == []

    def test_delete_book_from_favorites_if_book_already_add(self, collector):
        collector.add_new_book('5 Элемент')
        collector.add_book_in_favorites('5 Элемент')
        collector.delete_book_from_favorites('5 Элемент')
        assert collector.favorites == []

    def test_delete_book_from_favorites_invalid_book(self, collector):
        collector.add_new_book('5 Элемент')
        collector.add_book_in_favorites('5 Элемент')
        collector.delete_book_from_favorites('Жигало')
        assert collector.favorites == ['5 Элемент']

    def test_get_list_of_favorites_books_returns_expected_books(self, collector):
        collector.add_new_book('5 Элемент')
        collector.add_new_book('Наруто')
        collector.add_book_in_favorites('5 Элемент')
        collector.add_book_in_favorites('Наруто')
        result = collector.get_list_of_favorites_books()
        assert result  == ['5 Элемент', 'Наруто']


