$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 0 \end{array} \right] u

y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + 0 u
$$

Hence,

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 0 \end{array} \right]

\mathbf {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right], \qquad \qquad D = [ 0 ]
$$

(Note that, for the pole placement, matrices C and D do not affect the state-feedback gain matrix K.)

Two MATLAB programs for obtaining state-feedback gain matrix K are given in MATLAB Programs 10–24 and 10–25.
