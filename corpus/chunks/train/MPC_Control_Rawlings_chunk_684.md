$$
\mathbf {u} _ {1} ^ {0} (x (0), \mathbf {u} _ {2}) = \left[ \begin{array}{c c} K _ {1 1} & K _ {1 2} \end{array} \right] \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + L _ {1} \mathbf {u} _ {2}
$$

Combining the optimal control laws for each player gives

$$
\left[ \begin{array}{c} \mathbf {u} _ {1} ^ {0} \\ \mathbf {u} _ {2} ^ {0} \end{array} \right] = \left[ \begin{array}{c c} K _ {1 1} & K _ {1 2} \\ K _ {2 1} & K _ {2 2} \end{array} \right] \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + \left[ \begin{array}{c c} 0 & L _ {1} \\ L _ {2} & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p}
$$

in which the gain matrix multiplying the state is a full matrix for the cooperative game. Substituting the optimal control into the iteration gives

$$
\left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p + 1} = \underbrace {\left[ \begin{array}{c c} w _ {1} K _ {1 1} & w _ {1} K _ {1 2} \\ w _ {2} K _ {2 1} & w _ {2} K _ {2 2} \end{array} \right]} _ {\overline {{K}}} \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + \underbrace {\left[ \begin{array}{c c} (1 - w _ {1}) I & w _ {1} L _ {1} \\ w _ {2} L _ {2} & (1 - w _ {2}) I \end{array} \right]} _ {L} \left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p}
$$

Finally writing this equation in the plantwide notation, we express the iteration as

$$\mathbf {u} ^ {p + 1} = \overline {{K}} x (0) + L \mathbf {u} ^ {p}$$

Exponential stability of the closed-loop system. In the case of cooperative control, we consider the closed-loop system with a finite number of iterations, p. With finite iterations, distributed MPC becomes a form of suboptimal MPC as discussed in Sections 6.1.2 and 2.8. To analyze the behavior of the cooperative controller with a finite number of iterations, we require the cost decrease achieved by a single iteration, which we derive next. First we write the complete system evolution as in (6.10)

$$x ^ {+} = A x + B u$$

in which A and B are defined in (6.11). We can then use (6.3) to express the overall cost function

$$
\begin{array}{l} V (x (0), \mathbf {u}) = (1 / 2) x ^ {\prime} (0) (Q + \mathcal {A} ^ {\prime} \mathcal {Q A}) x (0) + \mathbf {u} ^ {\prime} (\mathcal {B} ^ {\prime} \mathcal {Q A}) x (0) + \\ (1 / 2) \mathbf {u} ^ {\prime} H _ {\mathbf {u}} \mathbf {u} \\ \end{array}
$$
