# Example 5.6

Compute the magnitude of

$$G _ {1} (j \omega) = \frac {1 0 ^ {5} (s + 1 2 . 7)}{(s + 0 . 1) (s + 1 0) (s + 5 0 0 0)}$$

for ω = 100 rad/sec. Express the magnitude in dB.

Plugging in

$$\left| G _ {1} (j 1 0 0) \right| = \frac {1 0 ^ {5} (1 2 . 7 + j 1 0 0)}{(0 . 1 + j 1 0 0) (1 0 + j 1 0 0) (5 0 0 0 + j 1 0 0)}$$

Evaluating the magnitude of each term:

$$| G _ {1} (j 1 0 0) | = \frac {1 0 ^ {5} (\sqrt {1 2 . 7 ^ {2} + 1 0 0 ^ {2}})}{(\sqrt {0 . 1 ^ {2} + 1 0 0 ^ {2}}) (\sqrt {1 0 ^ {2} + 1 0 0 ^ {2}}) (\sqrt {5 0 0 0 ^ {2} + 1 0 0 ^ {2}})}\left| G _ {1} (j 1 0 0) \right| = \frac {1 0 ^ {5} (1 0 0 . 8)}{(1 0 0 . 0 0 0 0 0 5) (1 0 0 . 5) (5 0 0 1)}$$

Combining

$$\left| G _ {1} (j 1 0 0) \right| = 0. 2 0 0 5 6$$

Some observations about this computation follow:

1. The computations have been carried out to excessive precision. Practical control plants are rarely known to even 1% accuracy.   
2. Another reason for excessive precision above is that we did not neglect any terms. In practice, a term like |0.1 + j100| can be instantly replaced with 100 since we know the 0.12 is going to be insignicant. (Don't do this when the real and imaginary parts are close in magnitude!)   
3. In an application where highly accurate numerical values must be obtained, we can use computer software. In modern engineering, hand calculations (even with a calculator) should only aim at quick approximate results.
