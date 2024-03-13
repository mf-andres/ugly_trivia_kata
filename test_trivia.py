from run_some_specific_games import run_games, save_outputs_to_file
from trivia import Game


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


def test_first_player_is_first_added_player():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    assert game.current_player_object.name == "player1"


def test_when_player1_answers_is_player2_turn():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    game.was_correctly_answered()
    assert game.current_player_object.name == "player2"


def test_when_player2_answers_is_player1_turn_again():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    game.was_correctly_answered()  # player1
    game.was_correctly_answered()  # player2
    assert game.current_player_object.name == "player1"


def test_when_gets_6_coins_it_wins_the_game():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    game.current_player_object.coins = 6
    assert game.current_player_object.has_won()


def test_when_player_rolls_it_moves_places():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    game.roll(1)
    assert game.current_player_object.place == 1


def test_when_player_rolls_it_moves_around():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    game.current_player_object.place = 11
    game.roll(1)
    assert game.current_player_object.place == 0


def test_when_player_answers_wrongly_it_goes_to_penalty_box():
    game = Game()
    game.add_player("player1")
    game.add_player("player2")
    game.wrong_answer()
    first_player = game.players[0]
    assert first_player.is_in_penalty_box
