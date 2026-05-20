# Example 11.4

Apply Tustin's method to convert G(s) into G(z) for T =0.01 sec. where

$$G (s) = \frac {1 0 (s + 4)}{(s + 0 . 1) (s + 1 0 0)}G (s) = \frac {1 0 (s + 4)}{(s + 0 . 1) (s + 1 0 0)} = \frac {1 0 (s + 4)}{s ^ {2} + 1 0 0 . 1 s + 1 0}G (z) = \frac {1 0 (\frac {2 (z - 1)}{T (z + 1)} + 4)}{(\frac {2 (z - 1)}{T (z + 1)}) ^ {2} + 1 0 0 . 1 (\frac {2 (z - 1)}{T (z + 1)}) + 1 0}$$

Let's multiply through by $T ^ { 2 } ( z + 1 ) ^ { 2 } { \mathrm { : } }$

$$= \frac {1 0 (2 (z - 1) T (z + 1) + 4 T ^ {2} (z + 1) ^ {2})}{4 (z ^ {2} - 2 z + 1) + 1 0 0 . 1 (2 (z - 1) T (Z + 1)) + 1 0 T ^ {2} (z + 1) ^ {2}}$$

Here's a couple of intermediate results we can plug in twice below:

$$2 (z - 1) T (z + 1) = 0. 0 2 \left(z ^ {2} - 1\right) \quad T ^ {2} (z + 1) ^ {2} = 1 0 ^ {- 4} \left(z ^ {2} + 2 z + 1\right)G (z) = \frac {1 0 (0 . 0 2 (z ^ {2} - 1) + 4 \times 1 0 ^ {- 4} (z ^ {2} + 2 z + 1))}{4 z ^ {2} - 8 z + 4 + 2 . 0 2 (z ^ {2} - 1) + 1 0 ^ {- 3} (z ^ {2} + 2 z + 1)}= \frac {0 . 2 0 4 z ^ {2} + 0 . 0 0 8 z - 0 . 1 9 6 0}{6 . 0 2 1 z ^ {2} - 8 . 0 0 2 z + 1 . 9 8 1}G (z) = 0. 3 3 9 \frac {z ^ {2} + 0 . 0 3 9 2 2 z - 0 . 9 6 0 8}{z ^ {2} - 1 . 3 2 9 0 z + 0 . 3 2 9 0}$$

Note: For reasons we will see in Section 11.7, T = 0.01 would NOT be fast enough for this control system.
