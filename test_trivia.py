from run_some_specific_games import run_games, save_outputs_to_file


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
