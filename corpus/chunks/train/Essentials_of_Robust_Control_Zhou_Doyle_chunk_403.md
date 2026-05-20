\Theta^ {- 1} = \left[ \begin{array}{c c c} \hat {A} - \hat {B} _ {2} \hat {D} _ {1 2} ^ {- 1} \hat {C} _ {1} & \hat {B} _ {2} \hat {D} _ {1 2} ^ {- 1} & \hat {B} _ {1} - \hat {B} _ {2} \hat {D} _ {1 2} ^ {- 1} \hat {D} _ {1 1} \\ \hline - \hat {D} _ {1 2} ^ {- 1} \hat {C} _ {1} & \hat {D} _ {1 2} ^ {- 1} & - \hat {D} _ {1 2} ^ {- 1} \hat {D} _ {1 1} \\ \hat {C} _ {2} - \hat {D} _ {2 2} \hat {D} _ {1 2} ^ {- 1} \hat {C} _ {1} & \hat {D} _ {2 2} \hat {D} _ {1 2} ^ {- 1} & \hat {D} _ {2 1} - \hat {D} _ {2 2} \hat {D} _ {1 2} ^ {- 1} \hat {D} _ {1 1} \end{array} \right]

\tilde {\Theta} ^ {- 1} = \left[ \begin{array}{c c c} \hat {A} - \hat {B} _ {1} \hat {D} _ {2 1} ^ {- 1} \hat {C} _ {2} & - \hat {B} _ {1} \hat {D} _ {2 1} ^ {- 1} & \hat {B} _ {2} - \hat {B} _ {1} \hat {D} _ {2 1} ^ {- 1} \hat {D} _ {2 2} \\ \hline \hat {D} _ {2 1} ^ {- 1} \hat {C} _ {2} & \hat {D} _ {2 1} ^ {- 1} & \hat {D} _ {2 1} ^ {- 1} \hat {D} _ {2 2} \\ \hat {C} _ {1} - \hat {D} _ {1 1} \hat {D} _ {2 1} ^ {- 1} \hat {C} _ {2} & - \hat {D} _ {1 1} \hat {D} _ {2 1} ^ {- 1} & \hat {D} _ {1 2} - \hat {D} _ {1 1} \hat {D} _ {2 1} ^ {- 1} \hat {D} _ {2 2} \end{array} \right].
$$

Proof. The results follow immediately from Lemma 9.2.

Theorem 15.5 Let $\begin{array} { r l r } { K _ { 0 } } & { { } = } & { \Theta _ { 1 2 } \Theta _ { 2 2 } ^ { - 1 } } \end{array}$ be the central $\mathcal { H } _ { \infty }$ controller such that $\| \mathcal { F } _ { \ell } ( G , K _ { 0 } ) \| _ { \infty } < \gamma$ and let $\hat { U } , \hat { V } \in \mathcal { R } \mathcal { H } _ { \infty }$ with det $\hat { V } ( \infty ) \neq 0$ be such that

$$
\left\| \left[ \begin{array}{c c} \gamma^ {- 1} I & 0 \\ 0 & I \end{array} \right] \Theta^ {- 1} \left(\left[ \begin{array}{l} \Theta_ {1 2} \\ \Theta_ {2 2} \end{array} \right] - \left[ \begin{array}{l} \hat {U} \\ \hat {V} \end{array} \right]\right) \right\| _ {\infty} <   1 / \sqrt {2}. \tag {15.2}
$$

Then $\hat { K } = \hat { U } \hat { V } ^ { - 1 }$ is also a stabilizing controller such that $\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \| _ { \infty } < \gamma$ .

Proof. Note that by Lemma 15.4, K is an admissible controller such that $\| T _ { z w } \| _ { \infty } < \gamma$ if and only if there exists a $Q \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| Q \| _ { \infty } < \gamma$ such that

$$
\left[ \begin{array}{l} U \\ V \end{array} \right] := \left[ \begin{array}{l} \Theta_ {1 1} Q + \Theta_ {1 2} \\ \Theta_ {2 1} Q + \Theta_ {2 2} \end{array} \right] = \Theta \left[ \begin{array}{l} Q \\ I \end{array} \right] \tag {15.3}
$$

and

$$K = U V ^ {- 1}.$$
