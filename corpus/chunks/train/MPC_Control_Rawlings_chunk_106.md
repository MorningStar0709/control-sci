This choice is motivated by the works of Davison and Smith (1971, 1974); Qiu and Davison (1993) and the Internal Model Principle of Francis and Wonham (1976). To remove offset, one designs a control system that can remove asymptotically constant, nonzero disturbances (Davison and Smith, 1971), (Kwakernaak and Sivan, 1972, p.278). To accomplish this end, the original system is augmented with a replicate of the constant, nonzero disturbance model, (1.43). Thus the states of the original system are moved onto the manifold that cancels the effect of the disturbance on the controlled variables. The augmented system model used for the state estimator is given by

$$
\left[ \begin{array}{l} x \\ d \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A & B _ {d} \\ 0 & I \end{array} \right] \left[ \begin{array}{l} x \\ d \end{array} \right] + \left[ \begin{array}{l} B \\ 0 \end{array} \right] u + w \tag {1.44a}

y = \left[ \begin{array}{l l} C & C _ {d} \end{array} \right] \left[ \begin{array}{l} x \\ d \end{array} \right] + v \tag {1.44b}
$$

and we are free to choose how the integrating disturbance affects the states and measured outputs through the choice of $B _ { d }$ and $C _ { d }$ . The only restriction is that the augmented system is detectable. That restriction can be easily checked using the following result.

Lemma 1.8 (Detectability of the augmented system). The augmented system (1.44) is detectable if and only if the nonaugmented system (A, C) is detectable, and the following condition holds:

$$
\operatorname{rank} \left[ \begin{array}{c c} I - A & - B _ {d} \\ C & C _ {d} \end{array} \right] = n + n _ {d} \tag {1.45}
$$

Corollary 1.9 (Dimension of the disturbance). The maximal dimension of the disturbance d in (1.44) such that the augmented system is detectable is equal to the number of measurements, that is

$$n _ {d} \leq p$$

A pair of matrices $( B _ { d } , C _ { d } )$ such that (1.45) is satisfied always exists. In fact, since (A, C) is detectable, the submatrix $\left[ \overset { I - A } { C } \right] \in \mathbb { R } ^ { ( p + n ) \times n }$ has rank n. Thus, we can choose any $n _ { d } \leq p$ columns in $\mathbb { R } ^ { \vec { p } + n }$ independent of $\left[ \begin{array} { l } { I - A } \\ { C } \end{array} \right]$ for $\left[ \begin{array} { c } { { - B _ { d } } } \\ { { C _ { d } } } \end{array} \right]$ Cd .
