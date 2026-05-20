# 4.6 Problems

Problem 4.1 Let $G ( s )$ be a matrix in $\mathcal { R H } _ { \infty }$ . Prove that

$$
\left\| \left[ \begin{array}{c} G \\ I \end{array} \right] \right\| _ {\infty} ^ {2} = \| G \| _ {\infty} ^ {2} + 1.
$$

Problem 4.2 (Parseval relation) Let $f ( t ) , g ( t ) \in \mathcal { L } _ { 2 } , F ( j \omega ) = \mathcal { F } \{ f ( t ) \}$ , and $G ( j \omega ) =$ ${ \mathcal { F } } \{ g ( t ) \}$ . Show that

$$\int_ {- \infty} ^ {\infty} f (t) g (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F (j \omega) G ^ {*} (j \omega) d \omega$$

and

$$\int_ {- \infty} ^ {\infty} | f (t) | ^ {2} d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | F (j \omega) | ^ {2} d \omega .$$

Note that

$$F (j \omega) = \int_ {- \infty} ^ {\infty} f (t) e ^ {- j \omega t} d t, \quad f (t) = \mathcal {F} ^ {- 1} (F (j \omega)) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F (j \omega) e ^ {j \omega t} d \omega .$$

where ${ \mathcal { F } } ^ { - 1 }$ denotes the inverse Fourier transform.

Problem 4.3 Suppose A is stable. Show

$$\int_ {- \infty} ^ {\infty} (j \omega I - A) ^ {- 1} d \omega = \pi I.$$

Suppose $G ( s ) = \left[ \frac { A \textbf { \vert } B } { C } \right] \in \mathcal { R H } _ { \infty }$ and let $Q = Q ^ { * }$ be the observability Gramian. Use the above formula to show that

$$\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} G ^ {\sim} (j \omega) G (j \omega) d \omega = B ^ {*} Q B.$$

[Hint: Use the fact that $G ^ { \sim } ( s ) G ( s ) = F ^ { \sim } ( s ) + F ( s )$ and $F ( s ) = B ^ { * } Q ( s I - A ) ^ { - 1 } B . ]$

Problem 4.4 Compute the 2-norm and ∞-norm of the following systems:

$$
G _ {1} (s) = \left[ \begin{array}{c c} \frac {1}{s + 1} & \frac {s + 3}{(s + 1) (s - 2)} \\ \frac {1 0}{s - 2} & \frac {5}{s + 3} \end{array} \right], G _ {2} (s) = \left[ \begin{array}{c c c} 1 & 0 & 1 \\ 2 & 3 & 1 \\ \hline 1 & 2 & 0 \end{array} \right]

G _ {3} (s) = \left[ \begin{array}{c c c} - 1 & - 2 & 1 \\ 1 & 0 & 0 \\ \hline 2 & 3 & 0 \end{array} \right], G _ {4} (s) = \left[ \begin{array}{c c c c c} - 1 & - 2 & - 3 & 1 & 2 \\ 1 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 & 0 \\ \hline 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 2 \end{array} \right].
$$

Problem 4.5 Let $r ( t )$ = sin ωt be the input signal to a plant

$$G (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \xi \omega_ {n} s + \omega_ {n} ^ {2}}$$

with $0 < \xi < 1 / \sqrt { 2 }$ . Find the steady-state response of the system $y ( t )$ . Also find the frequency ω that gives the largest magnitude steady-state response of $y ( t )$ .

Problem 4.6 Let $G ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ be a $p \times q$ transfer matrix and $y = G ( s ) u$ . Suppose
