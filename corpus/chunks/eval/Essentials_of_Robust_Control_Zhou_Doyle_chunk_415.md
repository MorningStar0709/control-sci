and let $L = - Y C ^ { * }$ . Then the left coprime factorization $( \tilde { M } , \tilde { N } )$ given by

$$
\left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] = \left[ \begin{array}{c c} A - Y C ^ {*} C & B \quad - Y C ^ {*} \\ \hline C & 0 \quad I \end{array} \right]
$$

is a normalized left coprime factorization (see Chapter 12). Let $\left\| \cdot \right\| _ { H }$ denote the Hankel norm (i.e., the largest Hankel singular value). Then we have the following result.

Corollary 16.2 Let $D = 0$ and $L = - Y C ^ { * }$ , where $Y \geq 0$ is the stabilizing solution to

$$A Y + Y A ^ {*} - Y C ^ {*} C Y + B B ^ {*} = 0.$$

Then $P = \tilde { M } ^ { - 1 } \tilde { N }$ is a normalized left coprime factorization and

$$
\begin{array}{l} \inf _ {K \text {stabilizing}} \left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} = \frac {1}{\sqrt {1 - \lambda_ {\max} (Y Q)}} \\ = \left(1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}\right) ^ {- 1 / 2} =: \gamma_ {\min} \\ \end{array}
$$

where Q is the solution to the following Lyapunov equation:

$$Q (A - Y C ^ {*} C) + (A - Y C ^ {*} C) ^ {*} Q + C ^ {*} C = 0.$$

Moreover, $i f$ the preceding conditions hold, then for any $\gamma > \gamma _ { \mathrm { m i n } }$ a controller achieving

$$
\left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} <   \gamma
$$

is given by

$$
K (s) = \left[ \begin{array}{c c} A - B B ^ {*} X _ {\infty} - Y C ^ {*} C & - Y C ^ {*} \\ \hline - B ^ {*} X _ {\infty} & 0 \end{array} \right]
$$

where

$$X _ {\infty} = \frac {\gamma^ {2}}{\gamma^ {2} - 1} Q \left(I - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y Q\right) ^ {- 1}.$$

Proof. Note that the Hamiltonian matrix associated with $X _ { \infty }$ is given by

$$
H _ {\infty} = \left[ \begin{array}{c c} A + \frac {1}{\gamma^ {2} - 1} Y C ^ {*} C & - B B ^ {*} + \frac {1}{\gamma^ {2} - 1} Y C ^ {*} C Y \\ - \frac {\gamma^ {2}}{\gamma^ {2} - 1} C ^ {*} C & - (A + \frac {1}{\gamma^ {2} - 1} Y C ^ {*} C) ^ {*} \end{array} \right].
$$

Straightforward calculation shows that

$$
H _ {\infty} = \left[ \begin{array}{c c} I & - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y \\ 0 & \frac {\gamma^ {2}}{\gamma^ {2} - 1} I \end{array} \right] H _ {q} \left[ \begin{array}{c c} I & - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y \\ 0 & \frac {\gamma^ {2}}{\gamma^ {2} - 1} I \end{array} \right] ^ {- 1}
$$

where
