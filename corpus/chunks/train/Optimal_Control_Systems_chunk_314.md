# 5.7 Problems

3. the closed-loop optimal control to track the speed along a ramp function 0.5t.

Problem 5.11 For the liquid-level control system described in Problem 1.2, obtain

1. the discrete-time model based on zero-order hold,   
2. the closed-loop optimal control to keep the liquid level constant at a particular value, and   
3. the closed-loop optimal control to track the liquid level along a ramp function $0.25t$ .

Problem 5.12 For the mechanical control system described in Problem 1.4, find the discrete-time model based on zero-order hold and then find the closed-loop optimal control to track the system along (i) a constant value and (ii) a ramp function.

Problem 5.13 [105] The discretized model using zero-order hold of the longitudinal motion of an aircraft is given by

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (k) + \mathbf {B} \mathbf {u} (t)$$

where,

$$
\mathbf {A} = \left[ \begin{array}{r r r r r} 0. 9 2 3 7 & - 0. 3 0 8 1 & 0. 0 & 0. 0 5 3 0 & - 0. 0 9 0 4 \\ 0. 0 3 9 7 & 0. 9 9 5 5 & 0. 0 & - 0. 1 0 7 5 & 0. 5 8 8 9 \\ 0. 0 8 7 1 & 1. 9 0 0 & 1. 0 & - 0. 6 3 5 3 & 0. 3 9 4 0 \\ - 0. 0 3 5 6 & 0. 0 1 0 1 & 0. 0 & 0. 0 0 7 8 & 0. 1 3 7 4 \\ 0. 0 6 9 6 & - 0. 0 1 2 7 & 0. 0 & - 0. 0 9 7 1 & 0. 2 8 7 4 \end{array} \right]

\mathbf {B} = \left[ \begin{array}{r r r} 0. 0 4 2 8 & - 0. 0 0 0 4 & - 0. 1 5 4 0 \\ - 0. 4 8 4 6 & - 0. 5 1 5 4 & - 0. 0 0 2 3 \\ - 0. 1 6 1 5 & - 0. 0 6 7 5 & - 0. 0 0 5 3 \\ - 0. 2 0 2 0 & - 0. 2 8 9 3 & 0. 0 0 5 1 \\ - 0. 8 0 6 8 & - 0. 8 5 2 2 & - 0. 0 0 6 4 \end{array} \right]

\begin{array}{l} x _ {1} (k) = \text { velocity,   ft / sec } \\ x _ {2} (k) = \text { pitch   angle,   deg } \\ x _ {3} (k) = \text { altitude,   ft } \\ x _ {4} (k) = \text { angle   of   attack,   deg } \\ x _ {5} (k) = \text { pitch   angular   velocity,   deg / sec } \\ u _ {1} (k) = \text { elevator   deflection,   deg } \\ u _ {2} (k) = \text { flap   deflection,   deg } \\ u _ {3} (k) = \text { throttle   position,   deg } \\ \end{array}
$$

Formulate a performance index to minimize the errors in states and to minimize the control effort. Obtain optimal controls and states for the system.

@@@@@@
