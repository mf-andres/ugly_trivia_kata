# Introduction

This code is a solution to the ugly trivia game kata.

The kata is about dealing with some legacy code that has neither documentation nor tests.

To understand the solution of this kata you should check the steps taken section. 
Also, you should check the changes made commit by commit.

# The code

The code implements a game of trivia. It has the following rules:

* Players play by turn
* On its turn a players rolls a d6 and moves the resulting places
* Then the player is asked a question
* The category of the question is determined by the place where the player is standing
* If the player answers correctly it is given a coin
* If the player answer incorrectly it goes to the penalty box 
* If a player in the penalty box rolls and odd number, it gets out of the penalty box and moves
* If a player stays in the penalty box it is not asked a question
* If a player gets 6 coins, it wins the game

# Running the game

~~~
python -m trivia.trivia
~~~

# Steps taken

1. We get to the project and observe that the code is messy, tangled and hard to read. 
2. We do not have enough time to study the code before doing changes, so we decide that we have to test it somehow. 
3. We conclude that a golden master is needed to allow for some changes
4. The golden master can be based on running the program and checking it's output but the output is always different
because of random values.
5. We make a little safe refactor to extract method play_game and inject a seed.
6. Now we make a script to play some game with a collection of seeds, and we collect the output. 
7. Then we make a test to run the same games and check if the output was the same.
8. Now that we have a basic test, we can make some small changes and play safe knowing that the code keeps functional
9. We can begin by making a Player class and moving functionality to this class
10. However, everything is pretty tangled to the current_player value and the game arrays (purses, positions...)
11. If we change the current_player value to be a Player object, everything will crash
12. We can however, declare a temporal attribute current_player_object to substitute functionality progressively
13. Also, while doing refactorings, we learn about the code, and we can begin to make some unit tests
14. We also reorganize the files
15. Lastly we fill the README with some docummentaiton