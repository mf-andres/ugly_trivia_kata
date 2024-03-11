1. We get to the project and observe that the code is messy, tangled and hard to read. 
2. We do not have enough time to study the code before doing changes, so we decide that we have to test it somehow. 
3. We conclude that a golden master is needed to allow for some changes
4. The golden master can be based on running the program and checking it's output but the output is always different
because of random values.
5. We make a little safe refactor to extract method play_game and inject a seed.
6. 