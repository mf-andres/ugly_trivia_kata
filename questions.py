class Questions:
    def __init__(self):
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        self.init_questions()

    def init_questions(self):
        for i in range(50):
            self.pop_questions.append(self.create_question("Pop", i))
            self.science_questions.append(self.create_question("Science", i))
            self.sports_questions.append(self.create_question("Sports", i))
            self.rock_questions.append(self.create_question("Rock", i))

    @staticmethod
    def create_question(category, index):
        return f"{category} Question {index}"

    def ask_question(self, category):
        print("The category is %s" % category)
        if category == 'Pop':
            print(self.pop_questions.pop(0))
        if category == 'Science':
            print(self.science_questions.pop(0))
        if category == 'Sports':
            print(self.sports_questions.pop(0))
        if category == 'Rock':
            print(self.rock_questions.pop(0))
