# Example 5.4

Given the state-variable equations of a third-order system, obtain the SSR matrices if the two output variables are $y _ { 1 } = x _ { 1 }$ and $y _ { 2 } = x _ { 2 } - x _ { 3 }$ .

$$\dot {x} _ {1} = - 6. 2 x _ {1} - 2. 3 x _ {2} + 8. 4 x _ {3}\dot {x} _ {2} = - x _ {2} + 2. 7 x _ {3} + 3 u _ {1}\dot {x} _ {3} = - 4. 1 x _ {1} - 1. 5 x _ {2} + 3. 9 x _ {3} + 4 u _ {2} \tag {5.23}$$

We can develop the complete SSR equations and matrices only if the system is linear, and we see that the three state-variable equations (5.23) are indeed linear combinations of the states $x _ { i }$ and inputs $u _ { j } .$ Let us develop the state equation first: Eq. (5.21) presents the general format of the state equation. In this case, the state vector x is a $3 \times 1$ column vector, and the input vector u is $\mathbf { a } \ 2 \times 1$ column vector (note that Eq. (5.23) includes two inputs $u _ { 1 }$ and $u _ { 2 } )$ . The rows of the state matrix A and input matrix B contain the state and input coefficients from the three respective state-variable equations. The state equation is

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 6. 2 & - 2. 3 & 8. 4 \\ 0 & - 1 & 2. 7 \\ - 4. 1 & - 1. 5 & 3. 9 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 3 & 0 \\ 0 & 4 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \tag {5.24}
$$

The reader should be able to perform the matrix-vector multiplication in Eq. (5.24) and reproduce the three individual state-variable equations in Eq. (5.23).

The system has two output variables, $y _ { 1 } = x _ { 1 }$ and $y _ { 2 } = x _ { 2 } - x _ { 3 }$ . Therefore the output vector $\mathbf { y }$ is a $2 \times 1$ column vector. Equation (5.22) presents the general format of the output equation, which, takes the form

$$
\mathbf {y} = \left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & - 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] \tag {5.25}
$$

Again, the reader should be able to carry out the matrix-vector multiplication in Eq. (5.25) and reproduce the desired output variables, $y _ { 1 } = x _ { 1 }$ and $y _ { 2 } = x _ { 2 } - x _ { 3 }$ . The complete SSR is
