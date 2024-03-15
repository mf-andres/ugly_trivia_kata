import pytest

from errors import UnplayableGameError
from run_some_specific_games import run_games, save_outputs_to_file
from trivia import Game


@pytest.fixture
def game():
    game_ = Game()
    game_.add_player("player1")
    game_.add_player("player2")
    return game_


def test_trivia_works_as_before():
    number_of_games = 100  # check that this number is equal in run_some_specific_games.py
    outputs = run_games(number_of_games)
    save_outputs_to_file(outputs, 'test_output.txt')
    assert text_files_are_equal("output.txt", "test_output.txt")


def text_files_are_equal(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        content1 = file1.read()

    with open(file2_path, 'r') as file2:
        content2 = file2.read()

    return content1 == content2


def test_first_player_is_first_added_player(game):
    assert game.current_player_object.name == "player1"


def test_when_player1_answers_is_player2_turn(game):
    game.handle_correct_answer()
    assert game.current_player_object.name == "player2"


def test_when_player2_answers_is_player1_turn_again(game):
    game.handle_correct_answer()  # for player1
    game.handle_correct_answer()  # for player2
    assert game.current_player_object.name == "player1"


def test_when_gets_6_coins_it_wins_the_game(game):
    game.current_player_object.coins = 6
    assert game.current_player_object.has_won()


def test_when_player_rolls_it_moves_places(game):
    game.handle_roll(1)
    assert game.current_player_object.place == 1


def test_when_player_rolls_it_moves_around(game):
    game.current_player_object.place = 11
    game.handle_roll(1)
    assert game.current_player_object.place == 0


def test_when_player_answers_wrongly_it_goes_to_penalty_box(game):
    game.handle_wrong_answer()
    first_player = game.players[0]
    assert first_player.is_in_penalty_box


def test_when_player_in_penalty_box_rolls_odd_it_gets_out_of_the_penalty_box(game):
    first_player = game.players[0]
    first_player.is_in_penalty_box = True
    game.handle_roll(3)
    assert first_player.is_getting_out_of_penalty_box


def test_when_player_answers_correctly_it_gets_one_coin(game):
    first_player = game.players[0]
    game.handle_correct_answer()
    assert first_player.coins == 1


def test_a_game_with_one_player_is_not_playable():
    game = Game()
    game.add_player("Chet")
    with pytest.raises(UnplayableGameError):
        game.play()
