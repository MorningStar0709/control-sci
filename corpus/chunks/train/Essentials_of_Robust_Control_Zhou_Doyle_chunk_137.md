Problem 5.7 The following procedure constructs a normalized right coprime factorization when G is strictly proper:

1. Get a stabilizable, detectable realization $A , B , C .$   
2. Do the Matlab command $F = - \mathrm { l q r } ( A , B , C ^ { \prime } C , I )$ .

3. Set

$$
{\left[ \begin{array}{l} N \\ M \end{array} \right]} (s) = {\left[ \begin{array}{c c} A + B F & B \\ \hline C & 0 \\ F & I \end{array} \right]}
$$

Verify that the procedure produces factors that satisfy $G = N M ^ { - 1 }$ . Now try the procedure on

$$
G (s) = \left[ \begin{array}{c c} {\frac {1}{s - 1}} & {\frac {1}{s - 2}} \\ {\frac {2}{s}} & {\frac {1}{s + 2}} \end{array} \right]
$$

Verify numerically that

$$N (j \omega) ^ {*} N (j \omega) + M (j \omega) ^ {*} M (j \omega) = I, \quad \forall \omega . \tag {5.17}$$

Problem 5.8 Use the procedure in Problem 5.7 to find the normalized right coprime factorization for

$$
G _ {1} (s) = \left[ \begin{array}{c c} \frac {1}{s + 1} & \frac {s + 3}{(s + 1) (s - 2)} \\ \frac {1 0}{s - 2} & \frac {5}{s + 3} \end{array} \right]

G _ {2} (s) = \left[ \begin{array}{c c} {\frac {2 (s + 1) (s + 2)}{s (s + 3) (s + 4)}} & {\frac {s + 2}{(s + 1) (s + 3)}} \end{array} \right]

G _ {3} (s) = \left[ \begin{array}{c c c c c c} - 1 & - 2 & 1 & 1 & 2 & 3 \\ 0 & 2 & - 1 & 3 & 2 & 1 \\ - 4 & - 3 & - 2 & 1 & 1 & 1 \\ \hline 1 & 1 & 1 & 0 & 0 & 0 \\ 2 & 3 & 4 & 0 & 0 & 0 \end{array} \right]

G _ {4} (s) = \left[ \begin{array}{c c c c} - 1 & - 2 & 1 & 2 \\ 0 & 1 & 2 & 1 \\ \hline 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \end{array} \right]
$$

Problem 5.9 Define the normalized left coprime factorization and describe a procedure to find such factorizations for strictly proper transfer matrices.
