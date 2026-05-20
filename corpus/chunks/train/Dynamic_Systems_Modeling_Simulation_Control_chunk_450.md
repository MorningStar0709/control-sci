$$\Theta (s) = \frac {a _ {1}}{s} + \frac {a _ {2} (s + 4)}{(s + 4) ^ {2} + 1 7 . 5 7 8 4 ^ {2}} + \frac {a _ {3} (1 7 . 5 7 8 4)}{(s + 4) ^ {2} + 1 7 . 5 7 8 4 ^ {2}} \tag {8.31}$$

The residue for the single pole at the origin is

$$\left. a _ {1} = s \Theta (s) \right| _ {s = 0} = \left. \frac {0 . 1 s ^ {2} + 0 . 8 s + 1 2 . 5}{s ^ {2} + 8 s + 3 2 5} \right| _ {s = 0} = \frac {1 2 . 5}{3 2 5} = 0. 0 3 8 5$$

The residues for the complex poles are determined from Eqs. (8.30) and (8.31)

$$
\begin{array}{l} (s ^ {2} + 8 s + 3 2 5) \Theta (s) | _ {s = - 4 + j 1 7. 5 7 8 4} = \left. \frac {0 . 1 s ^ {2} + 0 . 8 s + 1 2 . 5}{s} \right| _ {s = - 4 + j 1 7. 5 7 8 4} \\ = a _ {2} (- 4 + j 1 7. 5 7 8 4 + 4) + a _ {3} (1 7. 5 7 8 4) \tag {8.32} \\ \end{array}
$$

The left-hand side of Eq. (8.32) is

$$
\begin{array}{l} \left. \frac {0 . 1 s ^ {2} + 0 . 8 s + 1 2 . 5}{s} \right| _ {s = - 4 + j 1 7. 5 7 8 4} = \frac {0 . 1 (- 4 + j 1 7 . 5 7 8 4) ^ {2} + 0 . 8 (- 4 + j 1 7 . 5 7 8 4) + 1 2 . 5}{- 4 + j 1 7 . 5 7 8 4} \\ = \frac {- 2 0}{- 4 + j 1 7 . 5 7 8 4} = 0. 2 4 6 2 + j 1. 0 8 1 7 \tag {8.33} \\ \end{array}
$$

The right-hand side of Eq. (8.32) is

$$a _ {2} (- 4 + j 1 7. 5 7 8 4 + 4) + a _ {3} (1 7. 5 7 8 4) = 1 7. 5 7 8 4 a _ {3} + j 1 7. 5 7 8 4 a _ {2} \tag {8.34}$$

Equating the real and imaginary parts of Eqs. (8.33) and (8.34) yields the residues

$$a _ {2} = \frac {1 . 0 8 1 7}{1 7 . 5 7 8 4} = 0. 0 6 1 5a _ {3} = \frac {0 . 2 4 6 2}{1 7 . 5 7 8 4} = 0. 0 1 4 0$$

The numerical values of these residues could also be obtained by using Eqs. (8.30) and (8.31) evaluated at the conjugate pole $s = - 4 - j 1 7 . 5 7 8 4$ . Using the residues, the partial-fraction expansion (Eq. 8.31) becomes

$$\Theta (s) = \frac {0 . 0 3 8 5}{s} + \frac {0 . 0 6 1 5 (s + 4)}{(s + 4) ^ {2} + 1 7 . 5 7 8 4 ^ {2}} + \frac {0 . 0 1 4 0 (1 7 . 5 7 8 4)}{(s + 4) ^ {2} + 1 7 . 5 7 8 4 ^ {2}} \tag {8.35}$$

Taking the inverse Laplace transform (see numbers 3, 10, and 11 in Table 8.1) yields

$$\theta (t) = 0. 0 3 8 5 + 0. 0 6 1 5 e ^ {- 4 t} \cos 1 7. 5 7 8 4 t + 0. 0 1 4 0 e ^ {- 4 t} \sin 1 7. 5 7 8 4 t \text { rad } \tag {8.36}$$

Figure 8.3 shows the step response equation (8.36). Equation (8.36) and Fig. 8.3 show that the dynamic response of the mechanical system is the sum of an exponentially damped sinusoidal function plus a constant (0.0385 rad). The exponentially damped sine and cosine functions are the transient response as they decay to zero in about 1 s. Note that at time t = 0 we have $\theta ( 0 ) = 0 . 0 3 8 5 + 0 . 0 6 1 5 = 0 . 1$ rad as required in this example (recall that the initial angular position was zero in Example 7.8). The steady-state response is $\theta ( \infty ) = 0 . 0 3 8 5$ rad, which is identical to the steady-state response in Example 7.8.
