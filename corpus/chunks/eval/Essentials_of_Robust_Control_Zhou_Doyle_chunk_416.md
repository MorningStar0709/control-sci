$$
H _ {q} = \left[ \begin{array}{c c} A - Y C ^ {*} C & 0 \\ - C ^ {*} C & - (A - Y C ^ {*} C) ^ {*} \end{array} \right].
$$

It is clear that the stable invariant subspace of $H _ { q }$ is given by

$$
\mathcal {X} _ {-} (H _ {q}) = \mathrm{Im} \left[ \begin{array}{l} I \\ Q \end{array} \right]
$$

and the stable invariant subspace of $H _ { \infty }$ is given by

$$
\mathcal {X} _ {-} (H _ {\infty}) = \left[ \begin{array}{c c} I & - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y \\ 0 & \frac {\gamma^ {2}}{\gamma^ {2} - 1} I \end{array} \right] \mathcal {X} _ {-} (H _ {q}) = \mathrm{Im} \left[ \begin{array}{c} I - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y Q \\ \frac {\gamma^ {2}}{\gamma^ {2} - 1} Q \end{array} \right].
$$

Hence there is a nonnegative definite stabilizing solution to the algebraic Riccati equation of $X _ { \infty }$ if and only if

$$I - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y Q > 0$$

or

$$\gamma > \frac {1}{\sqrt {1 - \lambda_ {\max} (Y Q)}}$$

and the solution, if it exists, is given by

$$X _ {\infty} = \frac {\gamma^ {2}}{\gamma^ {2} - 1} Q \left(I - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y Q\right) ^ {- 1}.$$

Note that $Y$ and $Q$ are the controllability Gramian and the observability Gramian of $\left\lceil \begin{array} { l l } { \tilde { N } } & { \tilde { M } } \end{array} \right\rceil$ respectively. Therefore, we also have that the Hankel norm of $\left[ \begin{array} { l l } { \tilde { N } } & { \tilde { M } } \end{array} \right]$ is $\sqrt { \lambda _ { \operatorname* { m a x } } ( Y Q ) }$ . ✷

Corollary 16.3 Let $P = \tilde { M } ^ { - 1 } \tilde { N }$ be a normalized left coprime factorization and

$$P _ {\Delta} = (\tilde {M} + \tilde {\Delta} _ {M}) ^ {- 1} (\tilde {N} + \tilde {\Delta} _ {N})$$

with

$$
\left\| \left[ \begin{array}{c c} \tilde {\Delta} _ {N} & \tilde {\Delta} _ {M} \end{array} \right] \right\| _ {\infty} <   \epsilon .
$$

Then there is a robustly stabilizing controller for $P _ { \Delta }$ if and only $i f$

$$
\epsilon \leq \sqrt {1 - \lambda_ {\max} (Y Q)} = \sqrt {1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}}.
$$

The solutions to the normalized left coprime factorization stabilization problem are also solutions to a related $\mathcal { H } _ { \infty }$ problem, which is shown in the following lemma.

Lemma 16.4 Let $P = \tilde { M } ^ { - 1 } \tilde { N }$ be a normalized $l e f t$ coprime factorization. Then
