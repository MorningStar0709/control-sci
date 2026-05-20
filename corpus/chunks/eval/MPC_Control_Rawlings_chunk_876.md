# A.17 Conditional Probability and Bayes’s Theorem

Let $\xi$ and η be jointly distributed random variables with density $p _ { \xi , \eta } ( x , y )$ . We seek the density function of $\xi$ given a specific realization y of $\eta$ has been observed. We define the conditional density function as

$$p _ {\xi | \eta} (x | y) = \frac {p _ {\xi , \eta} (x , y)}{p _ {\eta} (y)}$$

Consider a roll of a single die in which η takes on values E or O to denote whether the outcome is even or odd and $\xi$ is the integer value of the die. The twelve values of the joint density function are simply computed

$$
\begin{array}{l} p _ {\xi , \eta} (1, \mathrm{E}) = 0 p _ {\xi , \eta} (1, \mathrm{O}) = 1 / 6 \\ p _ {\xi , \eta} (2, \mathrm{E}) = 1 / 6 p _ {\xi , \eta} (2, \mathrm{O}) = 0 \\ p _ {\xi , \eta} (3, \mathrm{E}) = 0 p _ {\xi , \eta} (3, \mathrm{O}) = 1 / 6 \\ p _ {\xi , \eta} (4, \mathrm{E}) = 1 / 6 p _ {\xi , \eta} (4, \mathrm{O}) = 0 \\ p _ {\xi , \eta} (5, \mathrm{E}) = 0 p _ {\xi , \eta} (5, \mathrm{O}) = 1 / 6 \\ p _ {\xi , \eta} (6, \mathrm{E}) = 1 / 6 p _ {\xi , \eta} (6, \mathrm{O}) = 0 \\ \end{array}
$$

The marginal densities are then easily computed; we have for $\xi$

$$p _ {\xi} (x) = \sum_ {y = 0} ^ {E} p _ {\xi , \eta} (x, y)$$

which gives by summing across rows of (A.33)

$$p _ {\xi} (x) = 1 / 6, \quad x = 1, 2, \dots 6$$

Similarly, we have for η

$$p _ {\eta} (y) = \sum_ {x = 1} ^ {6} p _ {\xi , \eta} (x, y)$$

which gives by summing down the columns of (A.33)

$$p _ {\eta} (y) = 1 / 2, \quad y = \mathrm{E}, \mathrm{O}$$

These are both in accordance of our intuition on the rolling of the die: uniform probability for each value 1 to 6 and equal probability for an even or an odd outcome. Now the conditional density is a different concept. The conditional density $p _ { \xi } | \eta ( x , y )$ tells us the density of x given that $\eta ~ = ~ y$ has been observed. So consider the value of this function

$$p _ {\xi | \eta} (1 | 0)$$

which tells us the probability that the die has a 1 given that we know that it is odd. We expect that the additional information on the die being odd causes us to revise our probability that it is 1 from 1/6 to 1/3. Applying the defining formula for conditional density indeed gives

$$p _ {\xi | \eta} (1 | \mathrm{O}) = p _ {\xi , \eta} (1, \mathrm{O}) / p _ {\eta} (\mathrm{O}) = \frac {1 / 6}{1 / 2} = 1 / 3$$

Consider the reverse question, the probability that we have an odd given that we observe a 1. The definition of conditional density gives

$$p _ {\eta , \xi} (0 | 1) = p _ {\eta , \xi} (0, 1) / p _ {\xi} (1) = \frac {1 / 6}{1 / 6} = 1$$
