$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {k}{m} & - \frac {b}{m} \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ \frac {1}{m} \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right], \quad D = 0
$$

Figure 2–16 is a block diagram for the system. Notice that the outputs of the integrators are state variables.

Correlation Between Transfer Functions and State-Space Equations. In what follows we shall show how to derive the transfer function of a single-input, single-output system from the state-space equations.

Let us consider the system whose transfer function is given by

$$\frac {Y (s)}{U (s)} = G (s) \tag {2-22}$$

This system may be represented in state space by the following equations:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {2-23}y = \mathbf {C} \mathbf {x} + D u \tag {2-24}$$

where x is the state vector, u is the input, and y is the output. The Laplace transforms of Equations (2–23) and (2–24) are given by

$$s \mathbf {X} (s) - \mathbf {x} (0) = \mathbf {A X} (s) + \mathbf {B U} (s) \tag {2-25}Y (s) = \mathbf {C X} (s) + D U (s) \tag {2-26}$$

Since the transfer function was previously defined as the ratio of the Laplace transform of the output to the Laplace transform of the input when the initial conditions were zero, we set $\mathbf { x } ( 0 )$ in Equation (2–25) to be zero. Then we have

$$s \mathbf {X} (s) - \mathbf {A X} (s) = \mathbf {B U} (s)$$

or

$$(s \mathbf {I} - \mathbf {A}) \mathbf {X} (s) = \mathbf {B} U (s)$$

By premultiplying $( s \mathbf { I } - \mathbf { A } ) ^ { - 1 }$ to both sides of this last equation, we obtain

$$\mathbf {X} (s) = (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} U (s) \tag {2-27}$$

By substituting Equation (2–27) into Equation (2–26), we get

$$Y (s) = \left[ \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + D \right] U (s) \tag {2-28}$$

Upon comparing Equation (2–28) with Equation (2–22), we see that

$$G (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + D \tag {2-29}$$

This is the transfer-function expression of the system in terms of A, B, C, and D.

Note that the right-hand side of Equation (2–29) involves $( s \mathbf { I } - \mathbf { A } ) ^ { - 1 }$ Hence. $G ( s )$ can be written as

$$G (s) = \frac {Q (s)}{| s \mathbf {I} - \mathbf {A} |}$$

where $Q ( s )$ is a polynomial in s. Notice that is equal to the characteristic poly-∑sI - A∑ nomial of G(s). In other words, the eigenvalues of A are identical to the poles of $G ( s )$ .
