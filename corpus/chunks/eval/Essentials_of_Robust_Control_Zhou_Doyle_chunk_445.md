where F is chosen such that $N M ^ { - 1 }$ is a normalized right coprime factorization. Let $\left[ \begin{array} { l } { \hat { N } } \\ { \hat { M } } \end{array} \right]$ be an rth order balanced truncation of $\left[ \begin{array} { l } { N } \\ { M } \end{array} \right]$ Show that $\left[ \begin{array} { l } { \hat { N } } \\ { \hat { M } } \end{array} \right]$ is also a normalized right coprime factorization.

Problem 16.11 (Reduced-Order Controllers by Controller Model Reduction; see Mc-Farlane and Glover [1990], Zhou and Chen [1995].) Let $G ( s ) = [ \frac { A \ : | \ : B \ : ] } { C \ : | \ : 0 \ : ] } = \tilde { M } ^ { - 1 } \tilde { N }$ be a normalized left coprime factorization and let $K ( s )$ be a suboptimal controller given in Corollary 18.2 (with performance γ). Let $K = U V ^ { - 1 }$ be a right coprime factorization

$$
\left[ \begin{array}{c} U \\ V \end{array} \right] = \left[ \begin{array}{c c} A - B B ^ {*} X _ {\infty} & - Y C ^ {*} \\ \hline - C & I \\ - B ^ {*} X _ {\infty} & 0 \end{array} \right]
$$

and $\hat { U } , \hat { V } \in \mathcal { R } \mathcal { H } _ { \infty }$ be approximations of U and V . Define

$$
\epsilon := \left\| \left[ \begin{array}{c} U \\ V \end{array} \right] - \left[ \begin{array}{c} \hat {U} \\ \hat {V} \end{array} \right] \right\| _ {\infty}
$$

and $K _ { r } = \hat { U } \hat { V } ^ { - 1 }$ . Show that $K _ { r }$ is a stabilizing controller for G if $\epsilon < 1$ and

$$
\left\| \left[ \begin{array}{c} K _ {r} \\ I \end{array} \right] (I + G K _ {r}) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} = \left\| \left[ \begin{array}{c} K _ {r} \\ I \end{array} \right] (I + G K _ {r}) ^ {- 1} \left[ \begin{array}{c c} I & G \end{array} \right] \right\| _ {\infty} <   \frac {\gamma}{1 - \epsilon}.
$$

Problem 16.12 (Reduced Order Controllers by Plant Model Reduction; see McFarlane and Glover [1990].) Let $G = \tilde { M } ^ { - 1 } \tilde { N }$ be a normalized left coprime factorization and let K be a stabilizing controller such that

$$
\left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + G K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} \leq \delta^ {- 1}.
$$

Let $G _ { r } : = \tilde { M } _ { r } ^ { - 1 } \tilde { N } _ { \eta }$ be an approximation of G and

$$
\epsilon := \left\| \left[ \begin{array}{c c} \tilde {M} - \tilde {M} _ {r} & \tilde {N} - \tilde {N} _ {r} \end{array} \right] \right\| _ {\infty} <   \delta .
$$

(a) Show that K stabilizes $G _ { r }$ and
