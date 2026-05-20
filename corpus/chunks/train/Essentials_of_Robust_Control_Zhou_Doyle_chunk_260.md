Proof. The only $\Delta \mathrm { s }$ in $\pmb { \Delta }$ that satisfy the det $\left( I - M \Delta \right) = 0$ constraint are reciprocals of nonzero eigenvalues of M. The smallest one of these is associated with the largest (magnitude) eigenvalue, so, $\mu _ { \pmb { \Delta } } ( M ) = \rho \left( M \right)$ . ✷

• If ∆ = Cn×n (S = 0, F = 1, m1 = n), then µ∆(M ) = σ(M ).

Obviously, for a general $\pmb { \Delta }$ , as in equation (10.1), we must have

$$\{\delta I _ {n}: \delta \in \mathbb {C} \} \subset \boldsymbol {\Delta} \subset \mathbb {C} ^ {n \times n}. \tag {10.5}$$

Hence directly from the definition of $\mu$ and from the two preceding special cases, we conclude that

$$\rho (M) \leq \mu_ {\Delta} (M) \leq \overline {{{{\sigma}}}} (M). \tag {10.6}$$

These bounds alone are not sufficient for our purposes because the gap between $\rho$ and $\overline { { \sigma } }$ can be arbitrarily large.

Example 10.1 Suppose

$$
\Delta = \left[ \begin{array}{c c} \delta_ {1} & 0 \\ 0 & \delta_ {2} \end{array} \right]
$$

and consider

$M = { \left\lceil \begin{array} { l l } { 0 } & { \beta } \\ { 0 } & { 0 } \end{array} \right\rceil }$ $\beta > 0$ . Then $\rho ( M ) = 0 \mathrm { ~ a n d ~ } \overline { { { \sigma } } } ( M ) = \beta .$ . But $\mu ( M ) = 0$   
since $\bar { \mathrm { d e t } } ( I - \bar { M } \Delta ) = 1$ for all admissible $\Delta .$

$( 2 ) ~ M = \left[ \begin{array} { c c } { { - 1 / 2 } } & { { 1 / 2 } } \\ { { - 1 / 2 } } & { { 1 / 2 } } \end{array} \right] . \mathrm { T h e n } \rho ( M ) = 0 \mathrm { a n d } \overline { { \sigma } } ( M ) = 1 . \mathrm { S i n c e }$

$$\det (I - M \Delta) = 1 + \frac {\delta_ {1} - \delta_ {2}}{2},$$

it is easy to see that min $\begin{array} { r } { \left\{ \operatorname* { m a x } _ { i } \left| \delta _ { i } \right| : 1 + \frac { \delta _ { 1 } - \delta _ { 2 } } { 2 } = 0 \right\} = 1 , \mathrm { { s o } } \ \mu ( M ) = 1 } \end{array}$ .

Thus neither $\rho$ nor $\overline { { \sigma } }$ provide useful bounds even in simple cases. The only time they do provide reliable bounds is when $\rho \approx \overline { { \sigma } } .$

However, the bounds can be refined by considering transformations on M that do not $a f f e c t \mu _ { \Delta } ( M )$ , but do affect $\rho$ and ${ \overline { { \sigma } } } .$ . To do this, define the following two subsets of $\mathbb { C } ^ { n \times n }$ :
