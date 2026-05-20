$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{r r r} 0 & 1 & 0 \\ - 1 & - 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \\ 0 \end{array} \right] u \tag {5-47}

z = \left[ \begin{array}{l l l} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] \tag {5-48}
$$

where u appearing in Equation (5–47) is the unit-step function.These equations can be written as

$$\dot {\mathbf {x}} = \mathbf {A A x} + \mathbf {B B u}z = \mathbf {C C x} + D D u$$

where

$$
\begin{array}{l} \mathbf {A} \mathbf {A} = \left[ \begin{array}{r r r} 0 & 1 & 0 \\ - 1 & - 1 & 0 \\ 1 & 0 & 0 \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & 0 \\ & 0 \\ \hline \mathbf {C} & 0 \end{array} \right] \\ \mathbf {B} \mathbf {B} = \left[ \begin{array}{l} 0 \\ 1 \\ 0 \end{array} \right] = \left[ \begin{array}{l} \mathbf {B} \\ 0 \end{array} \right], \quad \mathbf {C C} = [ 0 \quad 0 \quad 1 ], \quad D D = [ 0 ] \\ \end{array}
$$

Note that $x _ { 3 }$ is the third element of x. A plot of the unit-ramp response curve $z ( t )$ can be obtained by entering MATLAB Program 5–11 into the computer.A plot of the unitramp response curve obtained from this MATLAB program is shown in Figure 5–27.
