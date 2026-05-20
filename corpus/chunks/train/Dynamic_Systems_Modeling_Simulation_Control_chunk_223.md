The reader should be able to multiply each row of state matrix A and input matrix B by column vectors x and u, respectively, and reproduce the three state equations (5.35)– (5.37).

The system has two measurements, angular velocity and current, and therefore the output variables are $y _ { 1 } = \dot { \theta }$ and $y _ { 2 } = I .$ Both outputs are state variables: $y _ { 1 } = \dot { \theta } = x _ { 3 }$ and $y _ { 2 } = I = x _ { 1 }$ . Thus, the output equation is

$$
\mathbf {y} = \left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{l l l} 0 & 0 & 1 \\ 1 & 0 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \mathbf {u} \tag {5.39}
$$

The complete SSR is

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

where the state and input matrices are

$$
\mathbf {A} = \left[ \begin{array}{c c c} - R / L & 0 & - K _ {b} / L \\ 0 & 0 & 1 \\ K _ {m} / J & 0 & - b / J \end{array} \right] \quad \mathbf {B} = \left[ \begin{array}{c c} 1 / L & 0 \\ 0 & 0 \\ 0 & - 1 / J \end{array} \right]
$$

and the output and direct-link matrices are

$$
\mathbf {C} = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 1 & 0 & 0 \end{array} \right] \quad \mathbf {D} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right]
$$

In summary, we have a third-order system (n = 3) with two inputs and two outputs. Consequently, the state matrix A is $3 \times 3$ , the input matrix B is $3 \times 2 .$ , the output matrix C is $2 \times 3$ , and the direct-link matrix D is a $2 \times 2$ null matrix.
