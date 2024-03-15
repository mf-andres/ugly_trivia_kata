#!/usr/bin/env python3
import random
import sys

from board import Board
from player import Player
from questions import Questions


class Game:
    def __init__(self):
        self.players = []
        self.questions = Questions()
        self.board = Board()
        self.current_player = 0
        self.current_player_object = Player("NULL PLAYER")

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
            if self._roll_is_odd(roll):
                self._allow_player_to_leave_the_penalty_box()
                self._move_player(roll)
                self._ask_question()
            else:
                self.deny_player_to_leave_the_penalty_box()
        else:
            self._move_player(roll)
            self._ask_question()

    def _ask_question(self):
        current_player_place = self.current_player_object.place
        current_category = self.board.get_category_at(current_player_place)
        self.questions.ask_question(current_category)

    def deny_player_to_leave_the_penalty_box(self):
        print("%s is not getting out of the penalty box" % self.current_player_object.name)
        self.current_player_object.is_getting_out_of_penalty_box = False

    def _allow_player_to_leave_the_penalty_box(self):
        self.current_player_object.is_getting_out_of_penalty_box = True
        print("%s is getting out of the penalty box" % self.current_player_object.name)

    @staticmethod
    def _roll_is_odd(roll):
        return roll % 2 != 0

    def _move_player(self, roll):
        self.current_player_object.place += roll
        if self.current_player_object.place > 11:
            self.current_player_object.place -= 12
        print(f"{self.current_player_object.name}'s new location is {self.current_player_object.place}")

    def was_correctly_answered(self):
        if self.current_player_object.is_in_penalty_box:
            if self.current_player_object.is_getting_out_of_penalty_box:
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
        print(f"{self.current_player_object.name} now has {self.current_player_object.coins} Gold Coins.")

    def set_next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        self.current_player_object = self.players[self.current_player]

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.current_player_object.name + " was sent to the penalty box")
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
        game.roll(randrange(1, 6))

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
