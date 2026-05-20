Hence, to show that $\hat { K } = \hat { U } \hat { V } ^ { - 1 }$ with $\hat { U }$ and $\hat { V }$ satisfying equation (15.2) is also a stabilizing controller such that $\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \| _ { \infty } < \gamma _ { : }$ , we need to show that there is another coprime factorization for ${ \hat { K } } = U { \hat { V } } ^ { - 1 }$ and a $Q \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| Q \| _ { \infty } < \gamma$ such that equation (15.3) is satisfied.

Define

$$
\Delta := \left[ \begin{array}{c c} \gamma^ {- 1} I & 0 \\ 0 & I \end{array} \right] \Theta^ {- 1} \left(\left[ \begin{array}{c} \Theta_ {1 2} \\ \Theta_ {2 2} \end{array} \right] - \left[ \begin{array}{c} \hat {U} \\ \hat {V} \end{array} \right]\right)
$$

and partition $\Delta$ as

$$
\Delta := \left[ \begin{array}{c} \Delta_ {U} \\ \Delta_ {V} \end{array} \right].
$$

Then

$$
\left[ \begin{array}{l} \hat {U} \\ \hat {V} \end{array} \right] = \left[ \begin{array}{l} \Theta_ {1 2} \\ \Theta_ {2 2} \end{array} \right] - \Theta \left[ \begin{array}{l l} \gamma I & 0 \\ 0 & I \end{array} \right] \Delta = \Theta \left[ \begin{array}{l} - \gamma \Delta_ {U} \\ I - \Delta_ {V} \end{array} \right]
$$

and

$$
\left[ \begin{array}{c} \hat {U} (I - \Delta_ {V}) ^ {- 1} \\ \hat {V} (I - \Delta_ {V}) ^ {- 1} \end{array} \right] = \Theta \left[ \begin{array}{c} - \gamma \Delta_ {U} (I - \Delta_ {V}) ^ {- 1} \\ I \end{array} \right].
$$

Define $U : = \hat { U } ( I - \Delta _ { V } ) ^ { - 1 } , V : = \hat { V } ( I - \Delta _ { V } ) ^ { - 1 }$ , and $Q : = - \gamma \Delta _ { U } ( I - \Delta _ { V } ) ^ { - 1 }$ . Then $U V ^ { - 1 }$ is another coprime factorization for $\hat { K }$ . To show that $\hat { K } = U V ^ { - 1 } = \hat { U } \hat { V } ^ { - 1 }$ is a stabilizing controller such that $\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \| _ { \infty } < \gamma$ , we need to show that $\left\| \gamma \Delta _ { U } ( I - \Delta _ { V } ) ^ { - 1 } \right\| _ { \infty } < \bar { \gamma }$ or, equivalently, $\left\| \Delta _ { U } ( I - \Delta _ { V } ) ^ { - 1 } \right\| _ { \infty } < 1$ . Now

$$
\begin{array}{l} \Delta_ {U} (I - \Delta_ {V}) ^ {- 1} = \left[ \begin{array}{c c} I & 0 \end{array} \right] \Delta \left(I - \left[ \begin{array}{c c} 0 & I \end{array} \right] \Delta\right) ^ {- 1} \\ = \mathcal {F} _ {\ell} \left(\left[ \begin{array}{c c} 0 & \left[ \begin{array}{c c} I & 0 \end{array} \right] \\ I / \sqrt {2} & \left[ \begin{array}{c c} 0 & I / \sqrt {2} \end{array} \right] \end{array} \right], \sqrt {2} \Delta\right) \\ \end{array}
$$
