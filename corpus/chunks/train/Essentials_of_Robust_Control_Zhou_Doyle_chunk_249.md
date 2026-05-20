# 9.5 Problems

Problem 9.1 Find M and N matrices such that $\tilde { \Delta } = M \Delta N$ , where $\Delta$ is block diagonal.

$\mathrm { 1 . } \ \tilde { \Delta } = \left[ \begin{array} { l l } { \Delta _ { 1 } } & { \Delta _ { 2 } } \end{array} \right]$   
$\tilde { \Delta } = \left( \begin{array} { c c c } { { \Delta _ { 1 } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \Delta _ { 2 } } } \end{array} \right)$   
$\begin{array} { r } { \mathrm { 3 . ~ } \tilde { \Delta } = \left( \begin{array} { c } { \Delta _ { 1 } } \\ { \left[ \begin{array} { c } { \Delta _ { 2 } } \\ { 0 } \end{array} \right] } \end{array} \begin{array} { c } { \left[ \begin{array} { c c } { 0 } & { 0 } \end{array} \right] } \\ { \Delta _ { 3 } } \end{array} \right) } \end{array}$   
$4 . \ \tilde { \Delta } = \left( \begin{array} { c c c } { { \Delta _ { 1 } } } & { { 0 } } & { { 0 } } \\ { { \Delta _ { 2 } } } & { { \Delta _ { 3 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \Delta _ { 4 } } } \end{array} \right)$   
$5 . \ \tilde { \Delta } = \left( \begin{array} { c c c } { { \Delta _ { 1 } } } & { { \Delta _ { 3 } } } & { { 0 } } \\ { { \Delta _ { 2 } } } & { { \Delta _ { 4 } } } & { { \Delta _ { 6 } } } \\ { { 0 } } & { { \Delta _ { 5 } } } & { { 0 } } \end{array} \right)$

Problem 9.2 Let $G = ( I - P ( s ) \Delta ) ^ { - 1 }$ . Find a matrix $M ( s )$ such that $G = \mathcal { F } _ { u } ( M , \Delta )$ .

Problem 9.3 Consider the unity feedback system with $G ( s )$ of size $2 \times 2$ . Suppose $G ( s )$ has an uncertainty model of the form

$$
G (s) = \left[ \begin{array}{l l} [ 1 + \Delta_ {1 1} (s) ] g _ {1 1} (s) & [ 1 + \Delta_ {1 2} (s) ] g _ {1 2} (s) \\ [ 1 + \Delta_ {2 1} (s) ] g _ {2 1} (s) & [ 1 + \Delta_ {2 2} (s) ] g _ {2 2} (s) \end{array} \right].
$$

Suppose also that we wish to study robust stability of the feedback system. Pull out the $\Delta \mathrm { s }$ and draw the appropriate block diagram in the form of a structured perturbation of a nominal system.

Problem 9.4 Let

$$
P (s) = \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & D _ {1 1} & D _ {1 2} \\ C _ {2} & D _ {2 1} & D _ {2 2} \end{array} \right], \qquad K (s) = \left[ \begin{array}{c c} \hat {A} & \hat {B} \\ \hline \hat {C} & \hat {D} \end{array} \right].
$$

Find state-space realizations for $\mathcal { F } _ { \ell } ( P , K )$ and $\mathcal { F } _ { \ell } ( P , \hat { D } )$ .

Problem 9.5 Suppose $D _ { 2 1 }$ is nonsingular and

$$
M (s) = \left[ \begin{array}{c c c} A & B _ {1} & B _ {2} \\ \hline C _ {1} & D _ {1 1} & D _ {1 2} \\ C _ {2} & D _ {2 1} & D _ {2 2} \end{array} \right].
$$

Find a state-space realization for

$$
\hat {M} (s) = \left[ \begin{array}{l l} {\left[ \begin{array}{c c} 0 & M _ {1 2} \\ 0 & 0 \end{array} \right]} & {\left[ \begin{array}{c} M _ {1 1} \\ I \end{array} \right]} \\ {\left[ \begin{array}{c c} - I & M _ {2 2} \end{array} \right]} & {M _ {2 1} + E} \end{array} \right]
$$

where E is a constant matrix. Find the state-space realization for $\mathcal { F } _ { \ell } ( \hat { M } , E ^ { - 1 } )$ when $E = I$
