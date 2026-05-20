and, by Lemma 15.1, $\left\| \Delta _ { U } ( I - \Delta _ { V } ) ^ { - 1 } \right\| _ { \infty } < 1$ since

$$
\left[ \begin{array}{c c} 0 & \left[ \begin{array}{c c} I & 0 \end{array} \right] \\ I / \sqrt {2} & \left[ \begin{array}{c c} 0 & I / \sqrt {2} \end{array} \right] \end{array} \right]
$$

is a contraction and $\| \sqrt { 2 } \Delta \| _ { \infty } < 1$ .

Similarly, we have the following theorem:

Theorem 15.6 Let $\begin{array} { r l r } { K _ { 0 } } & { { } = } & { \tilde { \Theta } _ { 2 2 } ^ { - 1 } \tilde { \Theta } _ { 2 1 } } \end{array}$ be the central $\mathcal { H } _ { \infty }$ controller such that $\| \mathcal { F } _ { \ell } ( G , K _ { 0 } ) \| _ { \infty } < \gamma$ and let $\hat { \tilde { U } } , \hat { \tilde { V } } \in \mathcal { R } \mathcal { H } _ { \infty }$ with det $\hat { \tilde { V } } ( \infty ) \not = 0$ be such that

$$
\left\| \left(\left[ \begin{array}{c c} \tilde {\Theta} _ {2 1} & \tilde {\Theta} _ {2 2} \end{array} \right] - \left[ \begin{array}{c c} \hat {\tilde {U}} & \hat {\tilde {V}} \end{array} \right]\right) \tilde {\Theta} ^ {- 1} \left[ \begin{array}{c c} \gamma^ {- 1} I & 0 \\ 0 & I \end{array} \right] \right\| _ {\infty} <   1 / \sqrt {2}.
$$

Then $\hat { K } = \hat { \tilde { V } } ^ { - 1 } \hat { \tilde { U } }$ is also a stabilizing controller such that $\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \| _ { \infty } < \gamma .$ .

The preceding two theorems show that the sufficient conditions for $\mathcal { H } _ { \infty }$ controller reduction problem are equivalent to frequency-weighted $\mathcal { H } _ { \infty }$ model reduction problems.
