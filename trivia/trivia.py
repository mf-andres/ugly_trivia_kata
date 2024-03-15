#!/usr/bin/env python3
import random
import sys
from random import randrange
from typing import List

from trivia.board import Board
from trivia.errors import UnplayableGameError
from trivia.player import Player
from trivia.questions import Questions


class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.questions: Questions = Questions()
        self.board: Board = Board()
        self.current_player: int = 0
        self.current_player_object: Player = Player("NULL PLAYER")

    def add_player(self, player_name):
        new_player = Player(player_name)
        self.players.append(new_player)
        self.current_player_object = self.players[0]  # first player is first added player
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))
        return

    def play(self):
        if self._is_not_playable():
            raise UnplayableGameError()
        while True:
            self.play_turn(self._d6_roll)
            if self.player_has_won():
                break

    def play_turn(self, roll_fn):
        self.handle_roll(roll_fn())

        if self.current_player_object.is_in_penalty_box:
            print(f"{self.current_player_object.name} skips turn")
            return

        self.ask_question()

        if self._player_answered_wrongly():
            self.handle_wrong_answer()
        else:
            self.handle_correct_answer()

    def _is_not_playable(self) -> bool:
        return len(self.players) < 2

    @staticmethod
    def _d6_roll() -> int:
        return randrange(1, 6)

    @staticmethod
    def _player_answered_wrongly() -> bool:
        return randrange(9) == 7

    def handle_roll(self, roll):
        print("%s is the current player" % self.current_player_object.name)
        print("They have rolled a %s" % roll)
        if self.current_player_object.is_in_penalty_box and not self._roll_is_odd(roll):
            self._deny_player_from_leaving_the_penalty_box()
            return
        if self.current_player_object.is_in_penalty_box and self._roll_is_odd(roll):
            self._allow_player_to_leave_the_penalty_box()
        self._move_player(roll)

    def _deny_player_from_leaving_the_penalty_box(self):
        print("%s is not getting out of the penalty box" % self.current_player_object.name)

    def _allow_player_to_leave_the_penalty_box(self):
        self.current_player_object.is_in_penalty_box = False
        print("%s is getting out of the penalty box" % self.current_player_object.name)

    def ask_question(self):
        current_player_place = self.current_player_object.place
        current_category = self.board.get_category_at(current_player_place)
        self.questions.ask_question(current_category)

    @staticmethod
    def _roll_is_odd(roll) -> bool:
        return roll % 2 != 0

    def _move_player(self, roll):
        self.current_player_object.place += roll
        if self.current_player_object.place > 11:
            self.current_player_object.place -= 12
        print(f"{self.current_player_object.name}'s new location is {self.current_player_object.place}")

    def handle_correct_answer(self):
        print("Answer was correct!!!!")
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

    def handle_wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.current_player_object.name + " was sent to the penalty box")
        self.current_player_object.is_in_penalty_box = True
        self.set_next_player()
        return

    def player_has_won(self) -> bool:
        return any(player.has_won() for player in self.players)


def play_game(seed):
    random.seed(seed)
    game = Game()
    game.add_player('Chet')
    game.add_player('Pat')
    game.add_player('Sue')
    game.play()


if __name__ == '__main__':
    # if wrong params, exit
    if len(sys.argv) != 2:
        print("Missing args")
        print("python trivia.py seed")
        sys.exit()
    # take params
    seed = sys.argv[1]
    play_game(seed)
