class Board:
    categories_by_place = {
        0: 'Pop',
        1: 'Science',
        2: 'Sports',
        3: 'Rock',
        4: 'Pop',
        5: 'Science',
        6: 'Sports',
        7: 'Rock',
        8: 'Pop',
        9: 'Science',
        10: 'Sports',
        11: 'Rock',
    }

    def get_category_at(self, place):
        return self.categories_by_place[place]
