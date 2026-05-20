Figure 8–22 Unit-step response curves of system with K=2, a=0.9; K=2.2, a=0.9; and K=2.4, a=0.9.   
![](image/a1d80c64d0d9deb2500a62bd26bf1250e65756a1021b195dedd1e8566ddea61e.jpg)

<details>
<summary>line</summary>

| Time (sec) | K = 2.4, a = 0.9 | K = 2.2, a = 0.9 | K = 2 |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 1.0 | ~1.1 | ~1.05 | ~0.95 |
| 2.0 | ~1.05 | ~1.0 | ~1.0 |
| 3.0 | ~1.0 | ~1.0 | ~1.0 |
| 4.0 | ~1.0 | ~1.0 | ~1.0 |
| 5.0 | ~1.0 | ~1.0 | ~1.0 |
</details>

To plot the unit-step response curve of the system with any set shown in the sorted table, we specify the K and a values by entering an appropriate sortsolution command.

Note that for a specification that the maximum overshoot be between 10% and 5%, there would be three sets of solutions:

$$
\begin{array}{l} K = 2. 0 0 0 0, \quad a = 0. 9 0 0 0, \quad m = 1. 0 6 1 4 \\ K = 2. 2 0 0 0, \quad a = 0. 9 0 0 0, \quad m = 1. 0 7 7 2 \\ K = 2. 4 0 0 0, \quad a = 0. 9 0 0 0, \quad m = 1. 0 9 2 3 \\ \end{array}
$$

Unit-step response curves for these three cases are shown in Figure 8–22. Notice that the system with a larger gain K has a smaller rise time and larger maximum overshoot.Which one of these three systems is best depends on the system’s objective.
