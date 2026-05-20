# 15.1.2 Coprime Factor Reduction

The $\mathcal { H } _ { \infty }$ controller reduction problem can also be considered in the coprime factor framework. For that purpose, we need the following alternative representation of all admissible $\mathcal { H } _ { \infty }$ controllers:

Lemma 15.4 The family of all admissible controllers such that $\| T _ { z w } \| _ { \infty } < \gamma$ can also be written as

$$K (s) = \mathcal {F} _ {\ell} (M _ {\infty}, Q) = (\Theta_ {1 1} Q + \Theta_ {1 2}) (\Theta_ {2 1} Q + \Theta_ {2 2}) ^ {- 1} := U V ^ {- 1}= (Q \tilde {\Theta} _ {1 2} + \tilde {\Theta} _ {2 2}) ^ {- 1} (Q \tilde {\Theta} _ {1 1} + \tilde {\Theta} _ {2 1}) := \tilde {V} ^ {- 1} \tilde {U}$$

where $Q \in \mathcal { R H } _ { \infty } , \| Q \| _ { \infty } < \gamma$ , and $U V ^ { - 1 }$ and $\tilde { V } ^ { - 1 } \tilde { U }$ are, respectively, right and $l e f t$ coprime factorizations over $\mathcal { R H } _ { \infty }$ , and

$$
\Theta = \left[ \begin{array}{c c} \Theta_ {1 1} & \Theta_ {1 2} \\ \Theta_ {2 1} & \Theta_ {2 2} \end{array} \right] = \left[ \begin{array}{c c c} \hat {A} - \hat {B} _ {1} \hat {D} _ {2 1} ^ {- 1} \hat {C} _ {2} & \hat {B} _ {2} - \hat {B} _ {1} \hat {D} _ {2 1} ^ {- 1} \hat {D} _ {2 2} & \hat {B} _ {1} \hat {D} _ {2 1} ^ {- 1} \\ \hline \hat {C} _ {1} - \hat {D} _ {1 1} \hat {D} _ {2 1} ^ {- 1} \hat {C} _ {2} & \hat {D} _ {1 2} - \hat {D} _ {1 1} \hat {D} _ {2 1} ^ {- 1} \hat {D} _ {2 2} & \hat {D} _ {1 1} \hat {D} _ {2 1} ^ {- 1} \\ - \hat {D} _ {2 1} ^ {- 1} \hat {C} _ {2} & - \hat {D} _ {2 1} ^ {- 1} \hat {D} _ {2 2} & \hat {D} _ {2 1} ^ {- 1} \end{array} \right]

\tilde {\Theta} = \left[ \begin{array}{c c} \tilde {\Theta} _ {1 1} & \tilde {\Theta} _ {1 2} \\ \tilde {\Theta} _ {2 1} & \tilde {\Theta} _ {2 2} \end{array} \right] = \left[ \begin{array}{c c c} \hat {A} - \hat {B} _ {2} \hat {D} _ {1 2} ^ {- 1} \hat {C} _ {1} & \hat {B} _ {1} - \hat {B} _ {2} \hat {D} _ {1 2} ^ {- 1} \hat {D} _ {1 1} & - \hat {B} _ {2} \hat {D} _ {1 2} ^ {- 1} \\ \hline \hat {C} _ {2} - \hat {D} _ {2 2} \hat {D} _ {1 2} ^ {- 1} \hat {C} _ {1} & \hat {D} _ {2 1} - \hat {D} _ {2 2} \hat {D} _ {1 2} ^ {- 1} \hat {D} _ {1 1} & - \hat {D} _ {2 2} \hat {D} _ {1 2} ^ {- 1} \\ \hat {D} _ {1 2} ^ {- 1} \hat {C} _ {1} & \hat {D} _ {1 2} ^ {- 1} \hat {D} _ {1 1} & \hat {D} _ {1 2} ^ {- 1} \end{array} \right]
