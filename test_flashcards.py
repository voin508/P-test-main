import unittest
from flashcard import Flashcard
from flashcard_deck import FlashcardDeck
from unittest.mock import patch, mock_open
import pickle


class TestFlashcardMethods(unittest.TestCase):

    def test_display(self):
        flashcard = Flashcard("Python", "A high-level programming language.")
        self.assertEqual(flashcard.display(), "Python: A high-level programming language.")

    def test_edit_flashcard(self):
        flashcard = Flashcard("Term", "Old definition.")
        flashcard.edit_flashcard("New definition.")
        self.assertEqual(flashcard.definition, "New definition.")

    def test_flashcard_simularity(self):
        example_flashcard = Flashcard("Programming", "Programming is an art of thinking.")
        user_answer = "Programming is a form of creative thinking."
        result = example_flashcard.check_similarity(user_answer)
        self.assertEqual(result, True)
    
class TestFlashcardDecMethods(unittest.TestCase):

    def test_add_flashcard(self):
        flashcard = Flashcard("Term", "Deff")
        deck = FlashcardDeck()
        deck.add_flashcard(flashcard)
        self.assertIn(flashcard, deck.flashcards)

    def test_study_flashcards_correct_answer(self):
        deck = FlashcardDeck()
        flashcard1 = Flashcard("Term1", "Definition1")
        deck.add_flashcard(flashcard1)

        with patch('builtins.input', return_value="Definition1"):
            with patch('builtins.print') as mock_print:
                deck.study_flashcards()

        mock_print.assert_called_with("Правильно")

    def test_study_flashcards_incorrect_answer(self):
        deck = FlashcardDeck()
        flashcard1 = Flashcard("Term1", "Definition1")
        deck.add_flashcard(flashcard1)

        with patch('builtins.input', return_value="IncorrectAnswer"):
            with patch('builtins.print') as mock_print:
                deck.study_flashcards()

        mock_print.assert_called_with("Ошибка! правельное определение: Definition1")

    def test_study_flashcards_exit(self):
        deck = FlashcardDeck()
        flashcard1 = Flashcard("Term1", "Definition1")
        deck.add_flashcard(flashcard1)

        with patch('builtins.input', return_value="*"):
            with patch('builtins.print') as mock_print:
                deck.study_flashcards()

        mock_print.assert_called_with("Выход в главное меню")
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('flashcard_deck.pickle.dump')
    def test_save_flashcard_deck(self, mock_pickle_dump, mock_open):
        deck = FlashcardDeck()
        flashcard = Flashcard("Term", "Definition")
        deck.flashcards.append(flashcard)

        deck.save_flashcard_deck("test_deck.pkl")

        mock_open.assert_called_once_with("test_deck.pkl", 'wb')

        mock_pickle_dump.assert_called_once_with([flashcard], mock_open.return_value)
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('flashcard_deck.pickle.load')
    def test_load_flashcard_deck(self, mock_pickle_load, mock_open):
        flashcard = Flashcard("Term", "Definition")
        flashcards = [flashcard]

        mock_open.return_value.__enter__.return_value.read.return_value = "data"
        mock_pickle_load.return_value = flashcards

        deck = FlashcardDeck()
        deck.load_flashcard_deck("test_deck.pkl")

        mock_open.assert_called_once_with("test_deck.pkl", 'rb')

        mock_pickle_load.assert_called_once_with(mock_open.return_value)

        self.assertEqual(deck.flashcards, flashcards)

    def test_load_flashcard_deck_file_not_found(self):
        deck = FlashcardDeck()
        
        with unittest.mock.patch('builtins.open', side_effect=FileNotFoundError):
            with unittest.mock.patch('builtins.print') as mock_print:
                deck.load_flashcard_deck("nonexistent_file.pkl")

        mock_print.assert_called_once_with(f"Ошибка: файл 'nonexistent_file.pkl' не найден.")


    def test_load_flashcard_deck_unpickling_error(self):
        deck = FlashcardDeck()

        with unittest.mock.patch('builtins.open', side_effect=pickle.UnpicklingError):
            with unittest.mock.patch('builtins.print') as mock_print:
                deck.load_flashcard_deck("corrupted_file.pkl")

        mock_print.assert_called_once_with(f"Ошибка: невозможно загрузить данные из 'corrupted_file.pkl'.")

class TestFlashcardIntegration(unittest.TestCase):

    def test_flashcard_deck_interaction(self):
        deck = FlashcardDeck()
        flashcard1 = Flashcard("Term1", "Definition1")
        deck.add_flashcard(flashcard1)

        with patch('builtins.input', return_value="IncorrectAnswer"):
            with patch('builtins.print') as mock_print:
                deck.study_flashcards()

        mock_print.assert_called_with("Ошибка! правельное определение: Definition1")
        self.assertEqual(flashcard1.check_similarity("IncorrectAnswer"), False)


if __name__ == '__main__':
    unittest.main()