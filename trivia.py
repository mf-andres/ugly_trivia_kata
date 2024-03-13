#!/usr/bin/env python3
import random
import sys

from player import Player


class Game:
    def __init__(self):
        self.players = []
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.current_player_object = Player("NULL PLAYER")
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add_player(self, player_name):
        new_player = Player(player_name)
        self.players.append(new_player)
        self.current_player_object = self.players[0]  # first player is first added player

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.current_player_object.name)
        print("They have rolled a %s" % roll)

        if self.current_player_object.is_in_penalty_box:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player].name)
                self.move_player(roll)
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player].name)
                self.is_getting_out_of_penalty_box = False
        else:
            self.move_player(roll)
            print("The category is %s" % self._current_category)
            self._ask_question()

    def move_player(self, roll):
        self.current_player_object.place += roll
        if self.current_player_object.place > 11:
            self.current_player_object.place -= 12
        print(self.current_player_object.name + \
              '\'s new location is ' + \
              str(self.current_player_object.place))

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.current_player_object.place == 0: return 'Pop'
        if self.current_player_object.place == 4: return 'Pop'
        if self.current_player_object.place == 8: return 'Pop'
        if self.current_player_object.place == 1: return 'Science'
        if self.current_player_object.place == 5: return 'Science'
        if self.current_player_object.place == 9: return 'Science'
        if self.current_player_object.place == 2: return 'Sports'
        if self.current_player_object.place == 6: return 'Sports'
        if self.current_player_object.place == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.current_player_object.is_in_penalty_box:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.give_coin_to_current_player()
                self.set_next_player()
                return
            else:
                self.set_next_player()
                return



        else:

            print("Answer was corrent!!!!")
            self.give_coin_to_current_player()
            self.set_next_player()
            return

    def give_coin_to_current_player(self):
        self.current_player_object.coins += 1
        print(self.current_player_object.name + \
              ' now has ' + \
              str(self.current_player_object.coins) + \
              ' Gold Coins.')

    def set_next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        self.current_player_object = self.players[self.current_player]

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player].name + " was sent to the penalty box")
        self.current_player_object.is_in_penalty_box = True
        self.set_next_player()
        return

    def has_anyone_won(self):
        return any(player.has_won() for player in self.players)


from random import randrange


def play_game(seed):
    random.seed(seed)

    game = Game()
    game.add_player('Chet')
    game.add_player('Pat')
    game.add_player('Sue')
    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            game.wrong_answer()
        else:
            game.was_correctly_answered()

        if game.has_anyone_won():
            return


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing args")
        print("python trivia.py seed")
        sys.exit()
    seed = sys.argv[1]
    play_game(seed)
