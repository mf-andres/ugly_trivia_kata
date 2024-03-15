from typing import List


class Questions:
    def __init__(self):
        self.pop_questions: List[str] = []
        self.science_questions: List[str] = []
        self.sports_questions: List[str] = []
        self.rock_questions: List[str] = []
        self.init_questions()

    def init_questions(self):
        for i in range(50):
            self.pop_questions.append(self.create_question("Pop", i))
            self.science_questions.append(self.create_question("Science", i))
            self.sports_questions.append(self.create_question("Sports", i))
            self.rock_questions.append(self.create_question("Rock", i))

    @staticmethod
    def create_question(category: str, index: int) -> str:
        return f"{category} Question {index}"

    def ask_question(self, category: int):
        print("The category is %s" % category)
        if category == 'Pop':
            print(self.pop_questions.pop(0))
        if category == 'Science':
            print(self.science_questions.pop(0))
        if category == 'Sports':
            print(self.sports_questions.pop(0))
        if category == 'Rock':
            print(self.rock_questions.pop(0))

    def left(self) -> int:
        return (
                len(self.pop_questions)
                + len(self.rock_questions)
                + len(self.science_questions)
                + len(self.pop_questions)
        )
