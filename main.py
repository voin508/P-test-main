from flashcard import Flashcard
from flashcard_deck import FlashcardDeck

class ConsoleFlashcard:
    def __init__(self):
        self.deck = FlashcardDeck()

    def display_menu(self):
        print("\n==== Флешкарты ====")
        print("1. Добавить карточку")
        print("2. Вывести список карт")
        print("3. Учить карты")
        print("4. Сохранить карты")
        print("5. Загрузить карточки")
        print("6. Изменить карточку")
        print("0. Выход")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_flashcard()
            elif choice == "2":
                print("Флешкарты:")
                for card in self.deck.flashcards:
                    print(card.display())
            elif choice == "3":
                self.deck.study_flashcards()
            elif choice == "4":
                filename = input("Ввведите название файла для сохранения: ")
                self.save_flashcard_deck(filename)
            elif choice == "5":
                filename = input("Ввведите название файла для загрузки: ")
                self.load_flashcard_deck(filename)
            elif choice == "6":
                self.edit_flashcard(self.deck)
            elif choice == "0":
                break
            else:
                print("Неправельный ввод")

    def add_flashcard(self):
        term = input("Введите термин: ")
        definition = input("Введите определение: ")
        flashcard = Flashcard(term, definition)
        self.deck.add_flashcard(flashcard)
        print("Карточка добавлена")

    def save_flashcard_deck(self, filename):
        self.deck.save_flashcard_deck(filename)

    def load_flashcard_deck(self, filename):
        self.deck.load_flashcard_deck(filename)

    def edit_flashcard(self, deck):
        term = input("Ввведите термин для изменения: ")
        for card in deck.flashcards:
            if card.term == term:
                new_definition = input("введите новое определение: ")
                card.edit_flashcard(new_definition)
                break
        else:
            print(f"Карточка с термином '{term}' не найдена")

if __name__ == "__main__":
    app = ConsoleFlashcard()
    app.run()