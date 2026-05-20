# Example 5.3 (dc Servo)

A pure-gain controller $F(s) = k$ is proposed for the dc servo of Example 2.1 (Chapter 2). For what values of $k$ is the closed-loop system stable?

Solution The plant transfer function is

$$P (s) = \frac {8 8 . 7 6}{s (s + 2 1 . 5 2 6) (s + 2 . 4 7 4)} = \frac {N _ {P} (s)}{D _ {P} (s)}.$$

Since $F(s) = k, L(s) = kP(s)$ and the characteristic polynomial is

$$
\begin{array}{l} D _ {L} (s) + N _ {L} (s) = s (s + 2 1. 5 2 6) (s + 2. 4 7 4) + 8 8. 7 6 k \\ = s ^ {3} + 2 4. 0 0 s ^ {2} + 5 3. 2 5 5 s + 8 8. 7 6 k. \\ \end{array}
$$

The Routh array is

$$
\begin{array}{c c c c c} 3 & 1 & 5 3. 2 5 5 & 0 \\ 2 & 2 4. 0 0 & 8 8. 7 6 k & 0 \\ 1 & \frac {1 2 7 8 . 1 2 - 8 8 . 7 6 k}{2 4 . 0 0} & 0 \\ 0 & 8 8. 7 6 k \end{array}
$$

There are no sign changes in the first column if

$$1 2 7 8. 1 2 - 8 8. 7 6 k > 0 \quad \text { or } \quad k < 1 4. 4 0 0$$

and

$$8 8. 7 6 k > 0 \quad \text { or } \quad k > 0.$$

Therefore, stability is attained if

$$0 < k < 1 4. 4 0 0.$$

Note that if $k = 14.400$ , the elements of row 1 are all zero. From row 2, with $k = 14.400$ , we form the polynomial

$$
\begin{array}{l} p (s) = 2 4. 0 0 s ^ {2} + 8 8. 7 6 k \\ = 2 4. 0 0 s ^ {2} + 1 2 7 8. 1 2 \\ \end{array}
$$

whose roots are $s = \pm j7.298$ . The case $k = 14.400$ is the borderline case, and two roots are imaginary at $\pm j7.298$ . For that value of $k$ , row 1 is constructed from $dp / ds$ , and the array becomes

<table><tr><td>3</td><td>|</td><td>1</td><td>53.255</td><td>0</td></tr><tr><td>2</td><td>|</td><td>24.00</td><td>1278.12</td><td>0</td></tr><tr><td>1</td><td>|</td><td>48.00</td><td>0</td><td>0</td></tr><tr><td>0</td><td>|</td><td>1278.12</td><td></td><td></td></tr></table>

The positivity of the elements of the first column shows that the other roots are stable.
