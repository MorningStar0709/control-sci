# 5.5.1 Estimation

Given the numerous sets that are required to specify the output feedback case we are about to develop, Table 5.1 may serve as a reference for the sets defined in the chapter and the variables that are members of these sets.

Since both x and d are unknown, it is necessary to estimate them. For estimation purposes, it is convenient to work with the composite system whose state is $\phi : = ( x , d )$ . This system may be described more compactly by

$$\phi^ {+} = \tilde {A} \phi + \tilde {B} u + wy = \tilde {C} \phi + v$$

in which

$$
\widetilde {A} := \left[ \begin{array}{c c} A & B _ {d} \\ 0 & I \end{array} \right] \qquad \widetilde {B} := \left[ \begin{array}{c} B \\ 0 \end{array} \right] \qquad \widetilde {C} := \left[ \begin{array}{c c} C & C _ {d} \end{array} \right]
$$

and $\boldsymbol { w } : = ( w _ { x } , w _ { d } )$ takes values in $\mathbb { W } = \mathbb { W } _ { x } \times \mathbb { W } _ { d }$ . A necessary and sufficient condition for the detectability of $( \tilde { \cal A } , \tilde { \cal C } )$ is given in Lemma 1.8 in Chapter 1; a sufficient condition is detectability of $( A , C )$ coupled with invertibility of $C _ { d }$ . If $( \tilde { \cal A } , \tilde { \cal C } )$ is detectable, the state may be estimated using the time-invariant observer or filter described by

$$\hat {\phi} ^ {+} = \tilde {A} \hat {\phi} + \tilde {B} u + \delta \quad \delta := L (y - \tilde {C} \hat {\phi})$$

in which L is such that $\rho (  { \tilde { { A } } } _ { L } ) < 1$ where $\tilde { \cal A } _ { L } : = \tilde { \cal A } - L \tilde { \cal C }$ . Clearly $\delta = L \tilde { \mathcal { y } }$ where $\tilde { \boldsymbol { y } } = \tilde { \boldsymbol { C } } \tilde { \boldsymbol { \phi } } + \boldsymbol { \nu }$ . The estimation error $\tilde { \phi } : = \phi - \hat { \phi }$ satisfies

$$\tilde {\phi} ^ {+} = \tilde {A} \tilde {\phi} + w - L (\tilde {C} \tilde {\phi} + \nu)$$

or, in simpler form

$$\tilde {\phi} ^ {+} = \tilde {A} _ {L} \tilde {\phi} + \tilde {w} \quad \tilde {w} := w - L v$$

Clearly $\tilde { w } = w - L \nu$ takes values in the compact set $\tilde { \mathbb { W } }$ defined by

$$\widetilde {\mathbb {W}} := \mathbb {W} \oplus (- L \mathbb {N})$$
