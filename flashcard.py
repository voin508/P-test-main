import difflib

class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def display(self):
        return f"{self.term}: {self.definition}"

    def edit_flashcard(self, new_definition):
        self.definition = new_definition

    def check_similarity(self, user_answer, threshold=0.6):
        similarity_ratio = difflib.SequenceMatcher(None, self.definition.lower(), user_answer.lower()).ratio()
        return similarity_ratio >= threshold