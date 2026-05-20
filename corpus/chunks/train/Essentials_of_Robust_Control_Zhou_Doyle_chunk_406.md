# $\mathcal { H } _ { \infty }$ Controller Reduction Procedures

(i) Let $K _ { 0 } = \Theta _ { 1 2 } \Theta _ { 2 2 } ^ { - 1 } ( = \tilde { \Theta } _ { 2 2 } ^ { - 1 } \tilde { \Theta } _ { 2 1 } )$ be a suboptimal $\mathcal { H } _ { \infty }$ central controller $( Q = 0 )$ such that $\| T _ { z w } \| _ { \infty } < \gamma$ .   
(ii) Find a reduced-order controller $\hat { K } = \hat { U } \hat { V } ^ { - 1 } ( \mathrm { o r } \hat { \tilde { V } } ^ { - 1 } \hat { \tilde { U } } )$ 1 such that

$$
\left\| \left[ \begin{array}{c c} \gamma^ {- 1} I & 0 \\ 0 & I \end{array} \right] \Theta^ {- 1} \left(\left[ \begin{array}{c} \Theta_ {1 2} \\ \Theta_ {2 2} \end{array} \right] - \left[ \begin{array}{c} \hat {U} \\ \hat {V} \end{array} \right]\right) \right\| _ {\infty} <   1 / \sqrt {2}
$$

or

$$
\left\| \left(\left[ \begin{array}{c c} \tilde {\Theta} _ {2 1} & \tilde {\Theta} _ {2 2} \end{array} \right] - \left[ \begin{array}{c c} \hat {\tilde {U}} & \hat {\tilde {V}} \end{array} \right]\right) \tilde {\Theta} ^ {- 1} \left[ \begin{array}{c c} \gamma^ {- 1} I & 0 \\ 0 & I \end{array} \right] \right\| _ {\infty} <   1 / \sqrt {2}.
$$

Then the closed-loop system with the reduced-order controller $\hat { K }$ is stable and the performance is maintained with the reduced-order controller; that is,

$$\left\| T _ {z w} \right\| _ {\infty} = \left\| \mathcal {F} _ {\ell} (G, \hat {K}) \right\| _ {\infty} < \gamma .$$
