$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right], \qquad y = \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \\ \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right], \qquad \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 3 \\ 0 & 2 & 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] \\ \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \\ \dot {x} _ {5} \end{array} \right] = \left[ \begin{array}{c c c c c c} 2 & 1 & 0 & & & 0 \\ 0 & 2 & 1 & & \\ 0 & 0 & 2 & & \\ \hline & & & - 3 & 1 \\ 0 & & & 0 & - 3 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right], \qquad \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c c c c c} \framebox {1} & 1 & 1 & \framebox {0} & 0 \\ \framebox {0} & 1 & 1 & \framebox {0} & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ x _ {5} \end{array} \right] \\ \end{array}
$$

Principle of Duality. We shall now discuss the relationship between controllability and observability. We shall introduce the principle of duality, due to Kalman, to clarify apparent analogies between controllability and observability.

Consider the system $S _ { 1 }$ described by

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}\mathbf {y} = \mathbf {C x}$$

where x = state vector (n-vector)

u = control vector (r-vector)

y = output vector (m-vector)

A = n \* n matrix

B = n \* r matrix

C = m \* n matrix

and the dual system $S _ { 2 }$ defined by

$$\dot {\mathbf {z}} = \mathbf {A} ^ {*} \mathbf {z} + \mathbf {C} ^ {*} \mathbf {v}\mathbf {n} = \mathbf {B} ^ {*} \mathbf {z}$$

where z = state vector (n-vector)

v = control vector (m-vector)

n = output vector (r-vector)

A\* = conjugate transpose of A

B\* = conjugate transpose of B

C\* = conjugate transpose of C
