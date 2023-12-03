import random
import pickle

class FlashcardDeck:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def study_flashcards(self):
            for card in self.flashcards:
                user_answer = input(f"Какое определение у термина'{card.term}'? (Введите * чтобы выйти) ")
                if user_answer == "*":
                    print("Выход в главное меню")
                    break
                if card.check_similarity(user_answer):
                    print("Правильно")
                else:
                    print(f"Ошибка! правельное определение: {card.definition}")

    def save_flashcard_deck(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.flashcards, file)

    def load_flashcard_deck(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.flashcards = pickle.load(file)
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден.")
        except pickle.UnpicklingError:
            print(f"Ошибка: невозможно загрузить данные из '{filename}'.")
