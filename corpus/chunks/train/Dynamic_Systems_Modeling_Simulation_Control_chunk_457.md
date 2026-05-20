$$Y (s) = \frac {a _ {1}}{s} + \frac {a _ {2}}{s + 5 0 0} + \frac {a _ {3} (s + 2 0 0)}{(s + 2 0 0) ^ {2} + 3 6 7 . 4 2 ^ {2}} + \frac {a _ {4} (3 6 7 . 4 2)}{(s + 2 0 0) ^ {2} + 3 6 7 . 4 2 ^ {2}} \tag {8.54}$$

The two residues associated with the real poles are

$$\left. a _ {1} = s Y (s) \right| _ {s = 0} = \left. \frac {2 0 0 , 0 0 0}{(s + 5 0 0) (s ^ {2} + 4 0 0 s + 1 7 5 , 0 0 0)} \right| _ {s = 0} = \frac {2 0 0 , 0 0 0}{5 0 0 \times 1 7 5 , 0 0 0} = 0. 0 0 2 2 8 6\left. a _ {2} = (s + 5 0 0) Y (s) \right| _ {s = - 5 0 0} = \left. \frac {2 0 0 , 0 0 0}{s \left(s ^ {2} + 4 0 0 s + 1 7 5 , 0 0 0\right)} \right| _ {s = - 5 0 0} = \frac {2 0 0 , 0 0 0}{- 5 0 0 \times 2 2 5 , 0 0 0} = - 0. 0 0 1 7 7 8$$

The third and fourth residues are determined from the two equations evaluated at the two complex conjugate poles

$$
\begin{array}{l} (s ^ {2} + 4 0 0 s + 1 7 5, 0 0 0) Y (s) | _ {s = - 2 0 0 + j 3 6 7. 4 2} = \left. \frac {2 0 0 , 0 0 0}{s (s + 5 0 0)} \right| _ {s = - 2 0 0 + j 3 6 7. 4 2} \\ = a _ {3} (- 2 0 0 + j 3 6 7. 4 2 + 2 0 0) + a _ {4} (3 6 7. 4 2) \tag {8.55} \\ \end{array}
$$

and

$$
\begin{array}{l} (s ^ {2} + 4 0 0 s + 1 7 5, 0 0 0) Y (s) | _ {s = - 2 0 0 - j 3 6 7. 4 2} = \left. \frac {2 0 0 , 0 0 0}{s (s + 5 0 0)} \right| _ {s = - 2 0 0 - j 3 6 7. 4 2} \\ = a _ {3} (- 2 0 0 - j 3 6 7. 4 2 + 2 0 0) + a _ {4} (3 6 7. 4 2) \tag {8.56} \\ \end{array}
$$

After substituting the complex values for the poles, Eqs. (8.55) and (8.56) become

$$- 0. 9 9 0 4 9 - j 0. 1 8 6 6 3 = a _ {3} (j 3 6 7. 4 2) + a _ {4} (3 6 7. 4 2) \tag {8.57}- 0. 9 9 0 4 9 + j 0. 1 8 6 6 3 = a _ {3} (- j 3 6 7. 4 2) + a _ {4} (3 6 7. 4 2) \tag {8.58}$$

Equations (8.57) and (8.58) yield $a _ { 3 } = - 5 . 0 7 9 5 ( 1 0 ^ { - 4 } )$ and $a _ { 4 } = - 0 . 0 0 2 6 9 6$ . Therefore, the partial-fraction expansion (Eq. 8.54) becomes

$$Y (s) = \frac {0 . 0 0 2 2 8 6}{s} + \frac {- 0 . 0 0 1 7 7 8}{s + 5 0 0} + \frac {- 5 . 0 7 9 5 (1 0 ^ {- 4}) (s + 2 0 0)}{(s + 2 0 0) ^ {2} + 3 6 7 . 4 2 ^ {2}} + \frac {- 0 . 0 0 2 6 9 6 (3 6 7 . 4 2)}{(s + 2 0 0) ^ {2} + 3 6 7 . 4 2 ^ {2}} \tag {8.59}$$

The inverse Laplace transform of Eq. (8.59) consists of a constant, exponential function, and two exponentially damped sinusoidal terms (entries 10 and 11 in Table 8.1). Rounding to four decimal places, the spool-valve response is

$$y (t) = 0. 0 0 2 3 - 0. 0 0 1 8 e ^ {- 5 0 0 t} - 0. 0 0 0 5 e ^ {- 2 0 0 t} \cos 3 6 7. 4 2 t - 0. 0 0 2 7 e ^ {- 2 0 0 t} \sin 3 6 7. 4 2 t \mathrm{m} \tag {8.60}$$

This solution can be verified by applying MATLAB’s ilaplace command to the Laplace transform Eq. (8.53).
