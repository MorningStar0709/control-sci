# 6.6.1 Calculation of Roots

At rst glance it seems stability is trivial to assess. If any poles have positive real parts, the system is unstable. The tricky part comes from closed loop negative feedback systems. Consider the system of Figure 6.9. In our terminology,

$$G (s) = \frac {K}{(s + 1) (s + 2) (s + 3)}$$

where K is a positive real constant (we refer to terms like K as $\mathrm { ~ a ~ } g a i n )$ and H = 1. Clearly $G ( s )$ is stable since the poles are $s = \{ - 1 , - 2 , - 3 \}$ . But what about when we consider the closed loop gain?

$$= \frac {\frac {K}{(s + 1) (s + 2) (s + 3)}}{1 + \frac {K}{(s + 1) (s + 2) (s + 3)}}$$

Multiplying through by the poles of $G ( s )$ we get the closed-loop transfer function

$${\frac {Y (s)}{X (s)}} = {\frac {K}{(s + 1) (s + 2) (s + 3) + K}}$$

The denominator $( s + 1 ) ( s + 2 ) ( s + 3 ) + K$ is called the characteristic equation and it has dierent roots than the poles of $G ( s )$ . Multiplying out the poles of $G ( s )$ , the poles of the closed loop transfer function are solutions to

$$s ^ {3} + 6 s ^ {2} + 1 1 s + 6 + K = 0$$

Below are the roots of this characteristic polynomial, solved by computer for various values of $K \colon$ :

$$
\begin{array}{l} \mathrm{K=0.0} \\ - 3. - 2. - 1. \\ \mathrm{K} = 2. 0 \\ - 3. 5 2 1 3 7 9 7, - 1. 2 3 9 3 1 0 1 - 0. 8 5 7 8 7 3 6 \mathrm{i}, - 1. 2 3 9 3 1 0 1 + 0. 8 5 7 8 7 3 6 \mathrm{i} \\ \mathrm{K} = 4. 0 \\ - 3. 7 9 6 3 2 1 9, - 1. 1 0 1 8 3 9 - 1. 1 9 1 6 7 0 8 \mathrm{i}, - 1. 1 0 1 8 3 9 + 1. 1 9 1 6 7 0 8 \mathrm{i} \\ \mathrm{K} = 6. 0 \\ - 4. \quad - 1. \quad - 1. 4 1 4 2 1 3 6 \mathrm{i}, \quad - 1. + 1. 4 1 4 2 1 3 6 \mathrm{i} \\ \mathrm{K} = 8. 0 \\ - 4. 1 6 6 3 1 2 7 - 0. 9 1 6 8 4 3 6 - 1. 5 8 7 3 5 1 \mathrm{i} - 0. 9 1 6 8 4 3 6 + 1. 5 8 7 3 5 1 \mathrm{i} \\ \mathrm{K-10.0} \\ - 4. 3 0 8 9 0 7 3, - 0. 8 4 5 5 4 6 3 - 1. 7 3 1 5 5 7 \mathrm{i}, - 0. 8 4 5 5 4 6 3 + 1. 7 3 1 5 5 7 \mathrm{i} \\ \end{array}
$$
