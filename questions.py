class Questions:
    def __init__(self):
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        self.init_questions()

    def init_questions(self):
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    @staticmethod
    def create_rock_question(index):
        return "Rock Question %s" % index

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
