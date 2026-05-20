# EXAMPLE 7.1 Two-armed bandit problem

Assume that $p = 0.6$ and that $q$ is uniformly distributed over the interval [0, 1]. If machine I is played all the time, the expected gain is 0.6 per play; if machine II is played all the time, the expected gain per play is 0.5. The open-loop strategy then suggests that machine I should be played all the time. However, for each game of length $N$ there is a probability that the $q$ has a larger value than 0.6. If infinitely many plays are available, the player can play machine II, estimate $q$ , and then decide which machine to play for the rest of the plays.

To determine the profit of knowledge of q, assume that the player is told the value of q before each game. The player's optimal strategy is then to play the machine having the highest probability. In this case the expected gain per play is $E\{\max(p,q)\}=0.68$ . This means that the expected gain can be increased by 13% compared with the open-loop strategy if q is estimated. Table 7.1 shows the average gain per play for different values of N. As the number of plays increases, the gain will approach the maximum value 0.68. Relatively many plays are needed to get close to the optimum.

Figure 7.2 shows the state transition diagram for the optimal strategy when N = 6. The player is initially in the state (0, 0) and starts to play machine II to find out if machine II has better winning probability than machine I. The numbers in the circles indicate the number of times machines I and II, respectively, have given a gain of one unit. In states (0, 0) and (0, 1) there will be a switch to machine I after the player loses once; after state (0, 2) the optimal strategy allows one loss before switching to machine I. □

Table 7.1 Average gain per play for different values of N for the two-armed bandit problem in Example 7.1.

<table><tr><td>N</td><td>Gain per play</td></tr><tr><td>6</td><td>0.62</td></tr><tr><td>10</td><td>0.64</td></tr><tr><td>25</td><td>0.655</td></tr><tr><td>100</td><td>0.6676</td></tr><tr><td>500</td><td>0.6755</td></tr><tr><td>1000</td><td>0.6773</td></tr></table>

![](image/a6077ba1fa7f553a745cd4d424f9414618701de9e2d2867e58729f761d97eabe.jpg)

<details>
<summary>flowchart</summary>
