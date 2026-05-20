# Exercise 6.6: Why call the Lyapunov stability nonuniform?

Consider the following linear system

$$w ^ {+} = A w \quad w (0) = H x (0)x = C w$$

with solution $w ( k ) = A ^ { k } w ( 0 ) = A ^ { k } H x ( 0 ) , x ( k ) = C A ^ { k } H x ( 0 )$ . Notice that $x ( 0 )$ completely determines both w(k) and x(k), $k \geq 0$ . Also note that zero is a solution, i.e., $x ( k ) = 0 , k \geq 0$ satisfies the model.

(a) Consider the following case

$$
A = \rho \left[ \begin{array}{c c} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{array} \right] \quad H = \left[ \begin{array}{c} 0 \\ - 1 \end{array} \right] \quad C = \left[ \begin{array}{c c} 1 & - 1 \end{array} \right]
\rho = 0. 9 2 5 \quad \theta = \pi / 4 \quad x (0) = 1
$$

Plot the solution $x ( k )$ . Does $x ( k )$ converge to zero? Does $x ( k )$ achieve zero exactly for finite $k > 0 ?$

(b) Is the zero solution x(k) = 0 Lyapunov stable? State your definition of Lyapunov stability, and prove your answer. Discuss how your answer is consistent with the special case considered above.
