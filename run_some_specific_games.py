import subprocess


def run_games(number_of_games):
    outputs = list()
    for i in range(number_of_games):
        output = subprocess.check_output(['python', "trivia.py", f"{i}"], universal_newlines=True)
        outputs.append(output)
    return outputs


def save_outputs_to_file(outputs, output_file):
    with open(output_file, 'w') as file:
        for i, output in enumerate(outputs):
            file.write(f"Output {i + 1}:\n{output}\n\n")


if __name__ == "__main__":
    number_of_games = 100
    outputs = run_games(number_of_games)
    save_outputs_to_file(outputs, 'output.txt')
