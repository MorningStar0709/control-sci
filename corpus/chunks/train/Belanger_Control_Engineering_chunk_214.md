# Example 4.6 (dc Servo)

For the dc servo of Example 2.1 (Chapter 2),

$$P (s) = \frac {8 8 . 7 6}{s (s + 2 1 . 5 3) (s + 2 . 4 7 4)}.$$

Choose an $S(s)$ such that (i) the interpolation conditions are satisfied; (ii) $S(0) = 0$ ; (iii) $S(s)$ has all its poles as multiple poles at $s = -2$ ; and (iv) the order of $S$ is the least required to ensure a proper $F(s)$ . Calculate $F(s)$ .

Solution Since $P(s)$ has a pole excess of 3, the leading three coefficients in the denominator and numerator of $S(s)$ must be identical if $F(s)$ is to be proper. On the other hand, $P$ has an unstable pole at $s = 0$ , so $S(0) = 0$ [which automatically takes care of (ii)]. This means that the numerator of $S$ has no term $s^0$ . We write

$$
\begin{array}{l} S (s) = \frac {a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s}{(s + 2) ^ {3}} \\ = \frac {a _ {3} s ^ {3} + a _ {2} s ^ {2} + a _ {1} s}{s ^ {3} + 6 s ^ {2} + 1 2 s + 8}. \\ \end{array}
$$

We must have $a_3 = 1, a_2 = 6$ , and $a_1 = 12$ , so

$$S (s) = \frac {s ^ {3} + 6 s ^ {2} + 1 2 s}{(s + 2) ^ {3}}T (s) = 1 - S = \frac {8}{(s + 2) ^ {3}}$$

and

$$
\begin{array}{l} F = \frac {T}{P S} = \frac {8}{s (s ^ {2} + 6 s + 1 2)} \frac {s (s + 2 1 . 5 3) (s + 2 . 4 7 4)}{8 8 . 7 6} \\ = . 0 9 0 1 \frac {(s + 2 1 . 5 3) (s + 2 . 4 7 4)}{s ^ {2} + 6 s + 1 2}. \\ \end{array}
$$
