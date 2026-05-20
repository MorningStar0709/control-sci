# 1.5.1 Tracking

It is a standard objective in applications to use a feedback controller to move the measured outputs of a system to a specified and constant setpoint. This problem is known as setpoint tracking. In Section 2.9 we consider the case in which the system is nonlinear and constrained, but for simplicity here we consider the linear unconstrained system in which $y _ { \mathrm { s p } }$ is an arbitrary constant. In the regulation problem of Section 1.3 we assumed that the goal was to take the state of the system to the origin. Such a regulator can be used to treat the setpoint tracking problem with a coordinate transformation. Denote the desired output setpoint as $y _ { \mathrm { s p } }$ . Denote a steady state of the system model as $( x _ { s } , u _ { s } )$ . From (1.5), the steady state satisfies

$$
\left[ \begin{array}{c c} I - A & - B \end{array} \right] \left[ \begin{array}{c} x _ {s} \\ u _ {s} \end{array} \right] = 0
$$

For unconstrained systems, we also impose the requirement that the steady state satisfies $C x _ { s } = y _ { \mathrm { s p } }$ for the tracking problem, giving the set of equations

$$
\left[ \begin{array}{c c} I - A & - B \\ C & 0 \end{array} \right] \left[ \begin{array}{l} x _ {s} \\ u _ {s} \end{array} \right] = \left[ \begin{array}{l} 0 \\ y _ {\mathrm{sp}} \end{array} \right] \tag {1.41}
$$

If this set of equations has a solution, we can then define deviation variables

$$\tilde {x} (k) = x (k) - x _ {s}\tilde {u} (k) = u (k) - u _ {s}$$

that satisfy the dynamic model

$$
\begin{array}{l} \tilde {x} (k + 1) = x (k + 1) - x _ {s} \\ = A x (k) + B u (k) - \left(A x _ {s} + B u _ {s}\right) \\ \tilde {x} (k + 1) = A \tilde {x} (k) + B \tilde {u} (k) \\ \end{array}
$$

so that the deviation variables satisfy the same model equation as the original variables. The zero regulation problem applied to the system in deviation variables finds $\widetilde u ( k )$ that takes $\widetilde { \boldsymbol { x } } ( \boldsymbol { k } )$ to zero, or, equivalently, which takes $x ( k )$ to $x _ { s }$ e e, so that at steady state, $C x ( k ) = C x _ { s } = y _ { \mathrm { s p } }$ , which is the goal of the setpoint tracking problem. After solving the regulation problem in deviation variables, the input applied to the system is u $( k ) = \widetilde { u } ( k ) + u _ { s }$ .
