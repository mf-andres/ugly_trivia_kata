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
13. Also, while doing refactorings, we learn about the code and we can begin to make some unit tests