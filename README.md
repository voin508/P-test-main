[![CI/CD GitHub Actions](https://github.com/Samvel228/P-test/actions/workflows/python-app.yml/badge.svg)](https://github.com/Samvel228/P-test/actions/workflows/python-app.yml)
[![Coverage Status](https://coveralls.io/repos/Samvel228/P-test/badge.svg?branch=main)](https://coveralls.io/github/Samvel228/P-test?branch=main)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Samvel228_P-test&metric=alert_status)](https://sonarcloud.io/dashboard?id=Samvel228_P-test)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Samvel228_P-test&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Samvel228_P-test)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=Samvel228_P-test&metric=code_smells)](https://sonarcloud.io/dashboard?id=Samvel228_P-test)

# План тестирования

## Атестационное тестирование:  
Тест А1  
Действие: Запуск программы  
Ожидаемый результат: Выводится меню с шестью пунктами

Тест А2  
Действие: Вводится 1 (выбран пункт меню "Добавить карточку"). Вводится термин "Python" и определение "A high-level programming language."  
Ожидаемый результат: Карточка с термином "Python" и определением "A high-level programming language." добавлена в self.deck.flashcards

Тест А3  
Действие: Вводится 2 (выбран пункт меню "Вывести список карт")  
Ожидаемый результат: Выводится список карточек.

Тест А4  
Действие: Вводится 3 (выбран пункт меню "Учить карты"). Вводится определение.  
Ожидаемый результат: Выводится сообщение "Правильно" если ответ был введн вырный или "Ошибка! правильное определение: ..." если не правельный. После выводится следующий термин.

Тест А5  
Действие: Вводится 3 (выбран пункт меню "Учить карты"). Вводится *.  
Ожидаемый результат: Выводится сообщение "Выход в главное меню" и возвращает к выбору действий

Тест А6  
Действие: Вводится 4 (выбран пункт меню "Сохранить карты""). Вводится "kls".  
Ожидаемый результат: Создается файл в текущей дирректории с данными о карточках

Тест А6  
Действие: Вводится 5 (выбран пункт меню "Загрузить карточки"). Вводится "kls".  
Ожидаемый результат: Загружается пак карточек из указанного файла если он это возможно, "Ошибка: файл 'kls' не найден", если файл не найден, "Ошибка: невозможно загрузить данные из 'ksl'", если файл не возможно загрузить.

Тест А7  
Действие: Вводится 6 (выбран пункт меню "Изменить карточку"). Вводится "kls", "ss".  
Ожидаемый результат: Выводит "Ввведите термин для изменения: " Если в паке находится карточка с термином: "kls", то выводит "введите новое определение: " и меняет его на введенное, иначе выдает "Карточка с термином 'kls' не найдена".

Тест А8  
Действие: Вводится 0 (выбран пункт меню "Выход").  
Ожидаемый результат: Программа завершается  

## Блочное тестирование:

### Класс `Flashcard`
#### Тест Б1.1:  

Входные данные: Создается объект Flashcard с термином "Python" и определением "A high-level programming language."  
Ожидаемый результат: Метод display возвращает строку "Python: A high-level programming language."

#### Тест Б1.2:  

Входные данные: Создается объект Flashcard с термином "Term" и определением "Old definition."  
Ожидаемый результат: После вызова метода edit_flashcard с новым определением "New definition.", значение definition в объекте изменяется на "New definition."

#### Тест Б1.3:  

Входные данные: Создается объект Flashcard с термином "Programming" и определением "Programming is an art of thinking."  
Ожидаемый результат: Метод check_similarity возвращает True при сравнении с ответом пользователя "Programming is a form of creative thinking."

### Класс `FlashcardDeck`
#### Тест Б2.1:

Входные данные: Создается объект FlashcardDeck и объект Flashcard с термином "Term" и определением "Deff".  
Ожидаемый результат: Метод add_flashcard добавляет созданный объект Flashcard в атрибут flashcards объекта FlashcardDeck.

#### Тест Б2.2:

Входные данные: Создается объект FlashcardDeck и объект Flashcard с термином "Term1" и определением "Definition1".  
Ожидаемый результат: При вводе "Definition1" пользователем в процессе обучения (study_flashcards), выводится "Правильно".

#### Тест Б2.3:

Входные данные: Создается объект FlashcardDeck и объект Flashcard с термином "Term1" и определением "Definition1".  
Ожидаемый результат: При вводе "IncorrectAnswer" пользователем в процессе обучения (study_flashcards), выводится "Ошибка! правильное определение: Definition1".

#### Тест Б2.4:

Входные данные: Создается объект FlashcardDeck и добавляется фиктивная карточка.  
Ожидаемый результат: При вызове метода save_flashcard_deck с аргументом "test_deck.pkl", функция open вызывается с ожидаемыми аргументами, и функция pickle.dump вызывается с ожидаемыми аргументами.

#### Тест Б2.5:

Входные данные: Создается объект FlashcardDeck и подготавливаются данные для загрузки.  
Ожидаемый результат: При вызове метода load_flashcard_deck с аргументом "test_deck.pkl", функция open вызывается с ожидаемыми аргументами, и функция pickle.load вызывается с ожидаемыми аргументами. После этого атрибут flashcards в объекте FlashcardDeck обновляется с ожидаемыми данными.

#### Тест Б2.6:

Входные данные: Создается объект FlashcardDeck и имитируется несуществующий файл.  
Ожидаемый результат: При вызове метода load_flashcard_deck функция выдаст ошибку: Ошибка: файл 'nonexistent_file.pkl' не найден.

#### Тест Б2.7:

Входные данные: Создается объект FlashcardDeck и имитируется файл, который нельзя прочитать. 
Ожидаемый результат: При вызове метода load_flashcard_deck функция выдаст ошибку: Ошибка: невозможно загрузить данные из 'corrupted_file.pkl'.

## Интеграционное тестирование:

#### Тест И1:
Методы: FlashcardDeck.study_flashcards(), Flashcard.check_similarity(user_answer, threshold=0.6):  
Описание: Проверяем взаимодействие метода study_flashcards класса FlashcardDeck с методом check_similarity класса Flashcard.  
Ожидаемый результат: При вводе "IncorrectAnswer" в метод study_flashcards должно быть выведено сообщение "Ошибка! правильное определение: Definition1".Метод check_similarity должен вернуть False при сравнении с введенным ответом "IncorrectAnswer".  
