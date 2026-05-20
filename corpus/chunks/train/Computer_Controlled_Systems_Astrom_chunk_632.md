# Example 10.6 Generation of a stochastic signal

Assume that we for simulation purposes want to generate a stochastic signal with the spectral density

$$F (z) = \frac {1}{2 \pi} \cdot \frac {0 . 3 1 2 5 + 0 . 1 2 5 (z + z ^ {- 1})}{2 . 2 5 - 1 . 5 (z + z ^ {- 1}) + 0 . 5 (z ^ {2} + z ^ {- 2})} \tag {10.20}$$

The spectrum is shown in Fig. 10.6. Factorization of $F(z)$ gives the pole/zero pattern in Fig. 10.7 and the desired noise properties are obtained by filtering white noise through the filter

$$H (z) = \frac {0 . 5 z + 0 . 2 5}{z ^ {2} - z + 0 . 5}$$
