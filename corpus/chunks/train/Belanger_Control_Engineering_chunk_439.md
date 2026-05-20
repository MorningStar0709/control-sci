If we use the differentiation-free Equation 7.85,

$$
\dot {\psi} = (0 - 4) \psi + \left[ \begin{array}{l l l} 0 & 0 & 1 9. 6 \end{array} \right] - \left[ \begin{array}{l l l} 0 & 0 & 4 \end{array} \right] \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] \left[ \begin{array}{l l l} 0 & 0 & 4 \end{array} \right] \left[ \begin{array}{l} x \\ v \\ \theta \end{array} \right] + (- 1) u
$$

or

$$\dot {\psi} = - 4 \psi + 3. 6 \theta - u$$

and, from Equation 7.86,

$$\widehat {\omega} = \psi + 4 \theta .$$

The reduced-order observer is also used when the outputs are not state variables, by transforming them into states. To do this, we start from

$$\mathbf {y} = C \mathbf {x}$$

and find an $(n - m) \times n$ matrix $M$ such that

$$
T = \left[ \begin{array}{c} C \\ - - \\ M \end{array} \right]
$$

is nonsingular. If $C$ has its maximal rank $m$ ( $m$ independent rows), that is always possible. We then use the linear transformation

$$
\mathbf {z} = \left[ \begin{array}{c} C \\ - - \\ M \end{array} \right] \mathbf {x} = T \mathbf {x}
$$

and calculate the state equations for the transformed state, $\mathbf{z}$ (see Chapter 3). The first $m$ components of $\mathbf{z}$ are $C\mathbf{x} = \mathbf{y}$ , as desired, and we go on as before.
