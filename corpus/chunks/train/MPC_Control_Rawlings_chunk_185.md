# Exercise 1.58: Existence and uniqueness of the unconstrained target

Assume a system having p controlled variables $z \ = \ H x$ , with setpoints $r _ { \mathrm { s p } }$ , and m manipulated variables u, with setpoints $u _ { \mathrm { s p } }$ . Consider the steady-state target problem

$$\min _ {x, u} (1 / 2) \left(u - u _ {\mathrm{sp}}\right) ^ {\prime} R \left(u - u _ {\mathrm{sp}}\right) \quad R > 0$$

subject to

$$
\left[ \begin{array}{c c} I - A & - B \\ H & 0 \end{array} \right] \left[ \begin{array}{c} x \\ u \end{array} \right] = \left[ \begin{array}{c} 0 \\ r _ {\mathrm{sp}} \end{array} \right]
$$

Show that the steady-state solution $( x , u )$ exists for any $( r _ { \mathrm { s p } } , u _ { \mathrm { s p } } )$ and is unique if

$$
\operatorname{rank} \left[ \begin{array}{c c} I - A & - B \\ H & 0 \end{array} \right] = n + p \quad \operatorname{rank} \left[ \begin{array}{c} I - A \\ H \end{array} \right] = n
$$
