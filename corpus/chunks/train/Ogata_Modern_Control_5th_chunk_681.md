Output Controllability. In the practical design of a control system, we may want to control the output rather than the state of the system. Complete state controllability is neither necessary nor sufficient for controlling the output of the system. For this reason, it is desirable to define separately complete output controllability.

Consider the system described by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \tag {9-61}\mathbf {y} = \mathbf {C x} + \mathbf {D u} \tag {9-62}$$

where x = state vector (n-vector)

u = control vector (r-vector)

y = output vector (m-vector)

A = n \* n matrix

B = n \* r matrix

C = m \* n matrix

D = m \* r matrix

The system described by Equations (9–61) and (9–62) is said to be completely output controllable if it is possible to construct an unconstrained control vector u(t) that will transfer any given initial output $\mathbf { y } \big ( t _ { 0 } \big )$ to any final output $\mathbf { y } ( t _ { 1 } )$ in a finite time interval $t _ { 0 } \leq t \leq t _ { 1 }$ .

It can be proved that the condition for complete output controllability is as follows: The system described by Equations (9–61) and (9–62) is completely output controllable if and only if the $m \times ( n + 1 )$ r matrix

$$
\left[ \begin{array}{c c c c c c} \mathbf {C B} & \mathbf {C A B} & \mathbf {C A ^ {2} B} & \dots & \mathbf {C A ^ {n - 1} B} & \mathbf {D} \end{array} \right]
$$

is of rank m. (For a proof, see Problem A–9–16.) Note that the presence of the Du term in Equation (9–62) always helps to establish output controllability.

Uncontrollable System. An uncontrollable system has a subsystem that is physically disconnected from the input.

Stabilizability. For a partially controllable system, if the uncontrollable modes are stable and the unstable modes are controllable, the system is said to be stabilizable. For example, the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] u
$$

is not state controllable.The stable mode that corresponds to the eigenvalue of –1 is not controllable.The unstable mode that corresponds to the eigenvalue of 1 is controllable. Such a system can be made stable by the use of a suitable feedback. Thus this system is stabilizable.
