Furthermore, let F and L be such that $A + B F$ and $A + L C$ are stable. Then a particular set of state-space realizations for these matrices can be given by

$$
\left[ \begin{array}{c c} M & U _ {0} \\ N & V _ {0} \end{array} \right] = \left[ \begin{array}{c c c} A + B F & B & - L \\ \hline F & I & 0 \\ C + D F & D & I \end{array} \right] \tag {5.14}

\left[ \begin{array}{c c} \tilde {V} _ {0} & - \tilde {U} _ {0} \\ - \tilde {N} & \tilde {M} \end{array} \right] = \left[ \begin{array}{c c c} A + L C & - (B + L D) & L \\ \hline F & I & 0 \\ C & - D & I \end{array} \right] \tag {5.15}
$$

Proof. The idea behind the choice of these matrices is as follows. Using the observer theory, find a controller $\hat { K } _ { 0 }$ achieving internal stability; for example

$$
\hat {K} _ {0} := \left[ \begin{array}{c c} A + B F + L C + L D F & - L \\ \hline F & 0 \end{array} \right] \tag {5.16}
$$

Perform factorizations

$$\hat {K} _ {0} = U _ {0} V _ {0} ^ {- 1} = \tilde {V} _ {0} ^ {- 1} \tilde {U} _ {0},$$

which are analogous to the ones performed on P . Then Lemma 5.7 implies that each of the two left-hand side block matrices of equation (5.13) must be invertible in $\mathcal { R H } _ { \infty } .$ In fact, equation (5.13) is satisfied by comparing it with equation (5.7). ✷

Finding a coprime factorization for a scalar transfer function is fairly easy. Let $P ( s ) = \mathrm { n u m } ( s ) / \mathrm { d e n } ( s )$ where num(s) and den(s) are the numerator and the denominator polynomials of $P ( s )$ , and let $\alpha ( s )$ be a stable polynomial of the same order as den(s). Then $P ( s ) = n ( s ) / m ( s )$ with $n ( s ) = \mathrm { n u m } ( s ) / \alpha ( s )$ and $m ( s ) = \mathrm { d e n } ( s ) / \alpha ( s )$ is a coprime factorization. However, finding an $x ( s ) \in \mathcal { H } _ { \infty }$ and a $u ( s ) \in \mathcal { H } _ { \infty }$ such that $x ( s ) n ( s ) + y ( s ) m ( s ) = 1$ needs much more work.

Example 5.2 Let $P ( s ) = { \frac { s - 2 } { s ( s + 3 ) } }$ s − 2 and $\alpha = ( s + 1 ) ( s + 3 )$ . Then $P ( s ) = n ( s ) / m ( s )$ 号 with $n ( s ) = \frac { s - 2 } { ( s + 1 ) ( s + 3 ) }$ s − 2 and $m ( s ) = { \frac { s } { s + 1 } }$ forms a coprime factorization. To find an $x ( s ) \in \mathcal { H } _ { \infty }$ and a $\dot { y } ( s ) \in \mathcal { H } _ { \infty }$ such that $x ( s ) n ( s ) + y ( s ) m ( s ) = 1$ , consider a stabilizing controller for P : $\hat { K } = - \frac { s - 1 } { s + 1 0 } .$ Then $\hat { K } = u / v$ with $u = { \hat { K } }$ and $v = 1$ is a coprime s + 10 factorization and

$$m (s) v (s) - n (s) u (s) = \frac {(s + 1 1 . 7 0 8 5) (s + 2 . 2 1 4) (s + 0 . 0 7 7)}{(s + 1) (s + 3) (s + 1 0)} =: \beta (s)$$

Then we can take
