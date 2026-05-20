B–10–11. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{r r r} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 5 & - 6 & 0 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right]
$$

Design a full-order state observer, assuming that the desired poles for the observer are located at

$$s = - 1 0, \quad s = - 1 0, \quad s = - 1 5$$

B–10–12. Consider the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1. 2 4 4 & 0. 3 9 5 6 & - 3. 1 4 5 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]

+ \left[ \begin{array}{c} 0 \\ 0 \\ 1. 2 4 4 \end{array} \right] u

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

Given the set of desired poles for the observer to be

$$s = - 5 + j 5 \sqrt {3}, \quad s = - 5 - j 5 \sqrt {3}, \quad s = - 1 0$$

design a full-order observer.

B–10–13. Consider the double integrator system defined by

$$\ddot {y} = u$$

If we choose the state variables as

$$x _ {1} = yx _ {2} = \dot {y}$$

then the state-space representation for the system becomes as follows:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

It is desired to design a regulator for this system. Using the pole-placement-with-observer approach, design an observer controller.

Choose the desired closed-loop poles for the poleplacement part to be

$$s = - 0. 7 0 7 1 + j 0. 7 0 7 1, \quad s = - 0. 7 0 7 1 - j 0. 7 0 7 1$$

and assuming that we use a minimum-order observer, choose the desired observer pole at

$$s = - 5$$

B–10–14. Consider the system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where
