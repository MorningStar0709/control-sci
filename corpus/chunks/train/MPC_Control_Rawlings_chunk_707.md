# 6.3.4 Disturbance Models and Zero Offset

Integrating disturbance model. As discussed in Chapter 1, we model the disturbance with an integrator to remove steady offset. The augmented models for the local systems are

$$
\begin{array}{l} \left[ \begin{array}{c} x _ {i} \\ d _ {i} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {i} & B _ {d i} \\ 0 & I \end{array} \right] \left[ \begin{array}{c} x _ {i} \\ d _ {i} \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} _ {i 1} \\ 0 \end{array} \right] u _ {1} + \left[ \begin{array}{c} \overline {{B}} _ {i 2} \\ 0 \end{array} \right] u _ {2} \\ y _ {i} = \left[ \begin{array}{c c} C _ {i} & C _ {d i} \end{array} \right] \left[ \begin{array}{c} x _ {i} \\ d _ {i} \end{array} \right] \qquad i = 1, 2 \\ \end{array}
$$

We wish to estimate both $x _ { i }$ and $d _ { i }$ from measurements $y _ { i }$ . To ensure this goal is possible, we make the following restriction on the disturbance models

Assumption 6.14 (Disturbance models).

$$
\operatorname{rank} \left[ \begin{array}{c c} I - A _ {i} & - B _ {d i} \\ C _ {i} & C _ {d i} \end{array} \right] = n _ {i} + p _ {i} \qquad i = 1, 2
$$

It is always possible to satisfy this assumption by proper choice of $B _ { d i } , C _ { d i }$ . From Assumption 6.12 (b), $( A _ { i } , C _ { i } )$ is detectable, which implies that the first $n _ { i }$ columns of the square $( n _ { i } + p _ { i } ) \times ( n _ { i } + p _ { i } )$ matrix in Assumption 6.14 are linearly independent. Therefore the columns of $\left[ \begin{array} { l } { - B _ { d i } } \\ { C _ { d i } } \end{array} \right]$ can be chosen so that the entire matrix has rank $n _ { i } + p _ { i }$ . Assumption 6.14 is equivalent to detectability of the following augmented system.

Lemma 6.15 (Detectability of distributed disturbance model). Consider the augmented systems

$$
\widetilde {A} _ {i} = \left[ \begin{array}{c c} A _ {i} & B _ {d i} \\ 0 & I \end{array} \right] \qquad \widetilde {C} _ {i} = \left[ \begin{array}{c c} C _ {i} & C _ {d i} \end{array} \right] \qquad i = 1, 2
$$

The augmented systems $( \tilde { \cal A } _ { i } , \tilde { \cal C } _ { i } ) , i = 1 , 2$ are detectable if and only if Assumption 6.14 is satisfied.

Proving this lemma is discussed in Exercise 6.29. The detectability assumption then establishes the existence of $\widetilde { L } _ { i }$ such that $( \tilde { \boldsymbol { A } } _ { i } \mathrm { ~ - ~ }$ $\tilde { L _ { i } } \tilde { C _ { i } } ) , i = \mathrm { \dot { 1 } } , 2$ are stable and the local integrating disturbances can be estimated from the local measurements.
