# 5.4 Coprime Factorization over $\mathcal { R } \mathcal { H } _ { \infty }$

Recall that two polynomials $m ( s )$ and $n ( s )$ , with, for example, real coefficients, are said to be coprime if their greatest common divisor is 1 (equivalent, they have no common zeros). It follows from Euclid’s algorithm1 that two polynomials m and n are coprime iff there exist polynomials $x ( s )$ and $y ( s )$ such that $x m + y n = 1 ; $ such an equation is called a Bezout identity. Similarly, two transfer functions $m ( s )$ and $n ( s )$ in $\mathcal { R } \mathcal { H } _ { \infty }$ are said to be coprime over $\mathcal { R H } _ { \infty }$ if there exists $x , y \in \mathcal { R } \mathcal { H } _ { \infty }$ such that

$$x m + y n = 1.$$

The more primitive, but equivalent, definition is that m and n are coprime if every common divisor of m and n is invertible in $\mathcal { R H } _ { \infty } ;$ that ${ \mathrm { i s } } ,$

$$h, m h ^ {- 1}, n h ^ {- 1} \in \mathcal {R H} _ {\infty} \Longrightarrow h ^ {- 1} \in \mathcal {R H} _ {\infty}.$$

More generally, we have the following:

Definition 5.3 Two matrices M and N in $\mathcal { R H } _ { \infty }$ are right coprime over $\mathcal { R } \mathcal { H } _ { \infty }$ if they have the same number of columns and if there exist matrices $X _ { r }$ and $Y _ { r }$ in $\mathcal { R } \mathcal { H } _ { \infty }$ such that

$$
\left[ \begin{array}{l l} X _ {r} & Y _ {r} \end{array} \right] \left[ \begin{array}{l} M \\ N \end{array} \right] = X _ {r} M + Y _ {r} N = I.
$$

Similarly, two matrices $\tilde { M }$ and $\tilde { N }$ in $\mathcal { R H } _ { \infty }$ are left coprime over $\mathcal { R H } _ { \infty }$ if they have the same number of rows and if there exist matrices $X _ { l }$ and $Y _ { l }$ in $\mathcal { R H } _ { \infty }$ such that

$$
\left[ \begin{array}{l l} \tilde {M} & \tilde {N} \end{array} \right] \left[ \begin{array}{l} X _ {l} \\ Y _ {l} \end{array} \right] = \tilde {M} X _ {l} + \tilde {N} Y _ {l} = I.
$$

Note that these definitions are equivalent to saying that the matrix $\left[ \begin{array} { l } { M } \\ { N } \end{array} \right]$ is left invertible in $\mathcal { R H } _ { \infty }$ and the matrix $\begin{array} { r l } { \left\lceil \begin{array} { l l } { \tilde { M } } & { \tilde { N } } \end{array} \right\rceil } \end{array}$ is right invertible in $\mathcal { R H } _ { \infty }$ . These two equations are often called Bezout identities.
