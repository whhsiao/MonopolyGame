# MonopolyGame
This repo discussed some programs for solving a monopoly game problem and their extensions
## Introduction:
Some days ago I ran into the following post on reddit referring to a simplified version of monopoly game.
<https://www.reddit.com/r/askmath/comments/cr1g3y/the_game_of_monopoly_is_played_on_a_square_board/>

It reminds of some probability questions that may possibly appear in quantitative finance interviews. I was quite interested in this problem and therefore in this repo I will present two versions of numerical solutions, one with Monte Carlo simulation, the other utilizing Markov Chain evolution.
## Statement of the Problem:
The statement of the problem goes as follows.

*The game of monopoly is played on a square board with 10 spaces per side (so 40 in total). A player starts at the space marked "go" and on each turn rolls two sided dice, advancing forward a number of spaces equal to the sum of the two numbers that lands face up. (if a player rolls a sum that would normally cause them to advance past the 40th square, they will instead loop around, so if a player landed on a hypothetical 44th square, they will instead go to the 4th square on the board). Let P be the probability that a player after they "loop around" the board 10 times, lands on the space "Boardwalk" (the 40th square) before they "loop around" the board an eleventh time. Which integer is closest to the value 20P?*

## Solutions to the Problem:
-Monte Carlo Simulation:

The first method I present here is a direct simulation. I have a state variable (a positive integer mod 40) representing my current position and a loop_time variable representing the number of past loops. When the number of looping is lower than 10, I keep rolling the dices to update the position. During the 10th looping, I record if the state variable lands on "Boardwalk." After _N_ times of trials, the probability can be estimated by taking the ratio of the record to _N_.
The code is wrapped in the file ___test_47monopoly.py___.

-Markov Chain Evolution:

We note that the probability of landing on *i*th board equals sum over the probabilities of landing on *i-k*th board first and then rolling a sum of *k*. With this idea, we can start from the very first board with probability **1** and compute the probability landing on *i*th board for all the *i*>1 iteratively til the desired goal. This gives a direct computation rather than a estimate from simulation. The code is wrapped in the file ___test_48monopoly.py___.

## Results: 
Using Monte Carlo Simulation, one can obtain a value around **2.85**. Since the problem only asks about the closest integer, we may well conclude this integer should be **3**. The direct Markov Chain computation yields **2.85714...**, implying the same integer **3**. Nevertheless, it is worth noting that this number **2.85714** saturates as the number of looping excedes 5. From this observation, it is likely that we are entering a steady state of a Markov Chain, and therefore I speculate another shorter answer by solving the eigenstate of the transfer matrix. I shall post it as I get some spare time for it.
