# Example 8.4

Compute the Laplace transform of the following time function

$$f (t) = 0. 2 + 2 e ^ {- 3 t} - 5 e ^ {- 6 t} + 8 \sin 4 t$$

The superposition (linearity) property Eq. (8.4) shows that the complete Laplace transform $F ( s )$ is the sum of the Laplace transforms of each individual time function. Using Table 8.1, each Laplace transform is

$$
\begin{array}{l} \mathcal {L} \{0. 2 \} = \frac {0 . 2}{s} \quad (\text { number   3   in   Table   8.1 }) \\ \mathcal {L} \{2 e ^ {- 3 t} \} = \frac {2}{s + 3} \quad (\text { number   6   in   Table   8.1 }) \\ \mathscr {L} \{- 5 e ^ {- 6 t} \} = \frac {- 5}{s + 6} \quad (\text { number   6   in   Table   8.1 }) \\ \mathscr {L} \{8 \sin 4 t \} = 8 \frac {4}{s ^ {2} + 4 ^ {2}} \quad (\text { number   8   in   Table   8.1 }) \\ \end{array}
$$

Therefore, the complete Laplace transform is the sum of these four transforms

$$F (s) = \frac {0 . 2}{s} + \frac {2}{s + 3} - \frac {5}{s + 6} + \frac {3 2}{s ^ {2} + 1 6}$$

The reader should be able to compute the original time function f (t) from the above Laplace transform $F ( s )$ and Table 8.1.
