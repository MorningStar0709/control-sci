# 8.8 Problems

Problem 8.1 This problem shows that the stability margin is critically dependent on the type of perturbation. The setup is a unity-feedback loop with controller $K ( s ) = 1$ and plant $P _ { \mathrm { n o m } } ( s ) + \Delta ( s )$ , where

$$P _ {\mathrm{nom}} (s) = \frac {1 0}{s ^ {2} + 0 . 2 s + 1}.$$

1. Assume $\Delta ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ . Compute the largest $\beta$ such that the feedback system is internally stable for all $\| \Delta \| _ { \infty } < \beta$ .   
2. Repeat but with $\Delta \in \mathbb { R }$

Problem 8.2 Let $M \in \mathbb { C } ^ { p \times q }$ be a given complex matrix. Then it is shown in Qiu et al [1995] that $I - \Delta M$ is invertible for all $\Delta \in \mathbb { R } ^ { q \times p }$ such that $\overline { { \sigma } } ( \Delta ) \leq \gamma$ if and only if $\mu _ { \Delta } ( M ) < 1 / \gamma$ , where

$$
\mu_ {\Delta} (M) = \inf _ {\alpha \in (0, 1 ]} \sigma_ {2} \left(\left[ \begin{array}{c c} \operatorname{Re} M & - \alpha \Im M \\ \alpha^ {- 1} \Im M & \operatorname{Re} M \end{array} \right]\right).
$$

It follows that $( I - \Delta M ( s ) ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ for a given $M ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ and all $\Delta \in \mathbb { R } ^ { q \times p }$ with $\overline { { \sigma } } ( \Delta ) \leq \gamma$ if and only if $\mathrm { s u p } _ { \omega } \mu _ { \Delta } ( M ( j \omega ) ) < 1 / \gamma$ . Write a Matlab program to compute $\mu _ { \Delta } ( M )$ and apply it to the preceding problem.

Problem 8.3 Let $G ( s ) = { \frac { K e ^ { - \tau s } } { T s + 1 } }$ and $K \in [ 1 0 , 1 2 ] , \tau \in [ 0 , 0 . 5 ] , T = 1$ . Find a nominal model $G _ { o } ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ and a weighting function $W ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ such that

$$G (s) \in \left\{G _ {o} (s) (1 + W (s) \Delta (s)): \quad \Delta \in \mathcal {H} _ {\infty}, \quad \| \Delta \| \leq 1 \right\}.$$

Problem 8.4 Think of an example of a physical system with the property that the number of unstable poles changes when the system undergoes a small change, for example, when a mass is perturbed slightly or the geometry is deformed slightly.

Problem 8.5 Let X be a space of scalar-valued transfer functions. A function $f ( s )$ in X is a unit if $1 / f ( s )$ is in $\mathcal { X }$ .

1. Prove that the set of units in $\mathcal { R } \mathcal { H } _ { \infty }$ is an open set, that is, if f is a unit, then

$$(\exists \epsilon > 0) (\forall g \in \mathcal {R H} _ {\infty}) \| g \| _ {\infty} < \epsilon \implies f + g \text { is a unit. } \tag {8.11}$$
