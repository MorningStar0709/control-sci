# Example 8.8

Compute the inverse Laplace transform of

$$Y (s) = \frac {2 s + 9}{s ^ {2} + 6 s + 2 5}$$

The two poles are computed by solving $s ^ { 2 } + 6 s + 2 5 = 0$ , which yields the complex poles $s = - 3 \pm j 4$ . Note that we can “complete the square” and rewrite the denominator of $Y ( s )$ as the sum of two squared terms

$$Y (s) = \frac {2 s + 9}{(s + 3) ^ {2} + 4 ^ {2}} \tag {8.19}$$

This form of the Laplace transform matches entries 10 and 11 in Table 8.1, which are the transforms of exponentially damped sine and cosine functions:

$$\mathcal {L} \{e ^ {- a t} \sin \omega t \} = \frac {\omega}{(s + a) ^ {2} + \omega^ {2}}\mathcal {L} \{e ^ {- a t} \cos \omega t \} = \frac {s + a}{(s + a) ^ {2} + \omega^ {2}}$$

Comparing these transforms with Eq. (8.19) we see that a = 3 and ?? = 4. Next, we must rewrite Eq. (8.19) as the sum of two fractions that match the transformed damped sine and cosine functions:

$$Y (s) = \frac {2 s + 9}{(s + 3) ^ {2} + 4 ^ {2}} = \frac {2 (s + 3)}{(s + 3) ^ {2} + 4 ^ {2}} + \frac {(0 . 7 5) (4)}{(s + 3) ^ {2} + 4 ^ {2}} \tag {8.20}$$

Now we can take the inverse Laplace transform of Eq. (8.20), which yields the two exponentially damped harmonic functions

$$y (t) = 2 e ^ {- 3 t} \cos 4 t + 0. 7 5 e ^ {- 3 t} \sin 4 t$$
