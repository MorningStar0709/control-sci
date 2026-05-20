# Example 11.3

Apply Tustin's method to convert $C ( s )$ into $G ( z )$ for T =1 sec. where

$$C (s) = \frac {F (s)}{E (s)} = \frac {5 0}{(s + 1 0)}$$

Applying Tustin's method, plug in $\textstyle { \frac { 2 ( z - 1 ) } { T ( z + 1 ) } }$ for s:

$$C (z) = \frac {F (z)}{E (z)} = \frac {5 0}{\left(\frac {2 (z - 1)}{T (z + 1)} + 1 0\right)}C (z) = \frac {5 0 T (z + 1)}{2 (z - 1) + 1 0 T (z + 1)}$$

Applying $T = 1$

$$C (z) = \frac {5 0 (z + 1)}{2 z - 2 + 1 0 z + 1 0} = 5 0 \frac {(z + 1)}{1 2 z + 8}C (z) = \frac {5 0}{1 2} \frac {(z + 1)}{(z + 0 . 6 6 6 7)}$$

As with continuous time transfer functions, we get a ratio of polynomials (this time in $z )$ and we want to normalize them.

Note: For reasons we will see in Section 11.7, $T = 1$ would NOT be fast enough for this control system.
