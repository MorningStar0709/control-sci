# 15.1.1 Additive Reduction

Consider the class of (reduced-order) controllers that can be represented in the form

$$\hat {K} = K _ {0} + W _ {2} \Delta W _ {1},$$

where $K _ { 0 }$ may be interpreted as a nominal, higher-order controller, and $\Delta$ is a stable perturbation with stable, minimum phase and invertible weighting functions $W _ { 1 }$ and $W _ { 2 }$ . Suppose that $\| \mathcal { F } _ { \ell } ( G , K _ { 0 } ) \| _ { \infty } < \gamma$ . A natural question is whether it is possible to obtain a reduced-order controller $\hat { K }$ in this class such that the $\mathcal { H } _ { \infty }$ performance bound remains valid when $\hat { K }$ is in place of $K _ { 0 }$ . Note that this is somewhat a special case of the preceding general problem: The specific form of $\hat { K }$ means that $\hat { K }$ and $K _ { 0 }$ must possess the same right-half plane poles, thus to a certain degree limiting the set of attainable reduced-order controllers.

Suppose $\hat { K }$ is a suboptimal $\mathcal { H } _ { \infty }$ controller; that is, there is a $Q \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| Q \| _ { \infty } < \gamma$ such that $\hat { K } = \mathcal { F } _ { \ell } ( M _ { \infty } , Q )$ . It follows from simple algebra that

$$Q = \mathcal {F} _ {\ell} (\bar {K} _ {a} ^ {- 1}, \hat {K})$$

where

$$
\bar {K} _ {a} ^ {- 1} := \left[ \begin{array}{c c} 0 & I \\ I & 0 \end{array} \right] M _ {\infty} ^ {- 1} \left[ \begin{array}{c c} 0 & I \\ I & 0 \end{array} \right].
$$

Furthermore, it follows from straightforward manipulations that

$$
\begin{array}{l} \| Q \| _ {\infty} <   \gamma \iff \left\| \mathcal {F} _ {\ell} (\bar {K} _ {a} ^ {- 1}, \hat {K}) \right\| _ {\infty} <   \gamma \\ \Longleftrightarrow \left. \left\| \mathcal {F} _ {\ell} (\bar {K} _ {a} ^ {- 1}, K _ {0} + W _ {2} \Delta W _ {1}) \right\| _ {\infty} <   \gamma \right. \\ \Longleftrightarrow \left\| \mathcal {F} _ {\ell} (\tilde {R}, \Delta) \right\| _ {\infty} <   1 \\ \end{array}
$$

where

$$
\tilde {R} = \left[ \begin{array}{c c} \gamma^ {- 1 / 2} I & 0 \\ 0 & W _ {1} \end{array} \right] \left[ \begin{array}{c c} R _ {1 1} & R _ {1 2} \\ R _ {2 1} & R _ {2 2} \end{array} \right] \left[ \begin{array}{c c} \gamma^ {- 1 / 2} I & 0 \\ 0 & W _ {2} \end{array} \right]
$$

and $R$ is given by the star product

$$
\left[ \begin{array}{c c} R _ {1 1} & R _ {1 2} \\ R _ {2 1} & R _ {2 2} \end{array} \right] = \mathcal {S} (\bar {K} _ {a} ^ {- 1}, \left[ \begin{array}{c c} K _ {o} & I \\ I & 0 \end{array} \right]).
$$
