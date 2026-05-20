$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

where the state and input matrices are

$$
\mathbf {A} = \left[ \begin{array}{c c c} - 6. 2 & - 2. 3 & 8. 4 \\ 0 & - 1 & 2. 7 \\ - 4. 1 & - 1. 5 & 3. 9 \end{array} \right] \quad \mathbf {B} = \left[ \begin{array}{c c} 0 & 0 \\ 3 & 0 \\ 0 & 4 \end{array} \right]
$$

and the output and direct-link matrices are

$$
\mathbf {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \end{array} \right] \quad \mathbf {D} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right]
$$

In summary, we have a third-order system $( n = 3 )$ with two inputs and two outputs. Hence, the state matrix A is $3 \times 3$ , the input matrix B is $3 \times 2 .$ , the output matrix C is $2 \times 3 .$ , and the direct-link matrix D is a $2 \times 2$ null matrix. Even though the direct-link matrix D contains all zeros, it must be defined in order to perform numerical simulations with MATLAB and Simulink, as we see in Chapter 6.
