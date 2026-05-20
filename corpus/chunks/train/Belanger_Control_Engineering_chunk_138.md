# Example 3.17 (Active Suspension)

In the active suspension of Example 2.2 (Chapter 2), $y = x_{1} - x_{2}$ . Compute the diagonal Jordan form, and transform it to real, block-diagonal form.

Solution Proceeding as in Example 3.16 (MATLAB command eig), we obtain

$$
\begin{array}{l} \mathbf {z} = \left[ \begin{array}{c c c c} - 6. 1 5 + j 2 4. 5 & 0 & 0 & 0 \\ 0 & - 6. 1 5 - j 2 4. 5 & 0 & 0 \\ 0 & 0 & -. 8 4 8 + j 2. 9 4 & 0 \\ 0 & 0 & 0 & -. 8 4 8 - j 2. 9 4 \end{array} \right] \mathbf {z} \\ + \left[ \begin{array}{c c} - 9. 1 1 e - 3 + j 5. 5 1 e - 3 & 2 5 2 + j 1 7 8 \\ - 9. 1 1 e - 3 - j 5. 5 1 e - 3 & 2 5 2 - j 1 7 8 \\ 4. 5 0 e - 4 + j 1. 6 9 e - 3 & - 1. 9 2 + j 5. 0 4 \\ 4. 5 0 e - 4 - j 1. 6 9 e - 3 & - 1. 9 2 - j 5. 0 4 \end{array} \right] \left[ \begin{array}{l} u \\ y _ {R} \end{array} \right] \\ \end{array}
y = [ -. 0 2 5 4 + j. 0 3 1 7 -. 0 2 5 4 - j. 0 3 1 7 -. 2 8 2 - j. 0 4 1 4 -. 2 8 2 + j. 0 4 1 4 ] \mathbf {z}.
$$

Application of Equations 3.69 and 3.70 yields

$$
\frac {d}{d t} \left[ \begin{array}{c} R e z _ {1} \\ I _ {m} z _ {1} \\ R e z _ {2} \\ I _ {m} z _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} - 6. 1 5 & - 2 4. 5 & 0 & 0 \\ 2 4. 5 & - 6. 1 5 & 0 & 0 \\ 0 & 0 & -. 8 4 8 & - 2. 9 4 \\ 0 & 0 & 2. 9 4 & -. 8 4 8 \end{array} \right] \left[ \begin{array}{c} R e z _ {1} \\ I _ {m} z _ {1} \\ R e z _ {2} \\ I _ {m} z _ {2} \end{array} \right]

+ \left[ \begin{array}{c c} - 9. 1 1 e - 3 & 2 5 3 \\ 5. 5 0 e - 3 & - 1 7 9 \\ 4. 5 0 e - 4 & - 1. 9 3 \\ 1. 6 9 e - 3 & 5. 0 4 \end{array} \right] \left[ \begin{array}{l} u \\ y _ {r} \end{array} \right]

y = \left[ - 5. 0 8 e - 2 - 6. 3 4 e - 2 -. 5 6 3 8. 2 9 e - 2 \right] \left[ \begin{array}{l} R e z _ {1} \\ I _ {m} z _ {1} \\ R e z _ {2} \\ I _ {m} z _ {2} \end{array} \right]
$$
