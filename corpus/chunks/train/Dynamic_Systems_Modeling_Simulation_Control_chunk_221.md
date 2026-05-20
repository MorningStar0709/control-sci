$$
y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + [ 0 ] u \tag {5.29}
$$

The complete SSR is

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x} + D u$$

where the state and input matrices are

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - k / m & - b / m \end{array} \right] \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 / m \end{array} \right]
$$

and the output and direct-link matrices are

$$
\mathbf {C} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \qquad D = 0
$$

In summary, we have a second-order system $( n = 2 )$ ) with one input and one output. Hence, the state matrix A is $2 \times 2$ , the input matrix B is $2 \times 1$ (a column vector), the output matrix C is $1 \times 2$ (a row vector), and the direct-link matrix D is a scalar (it is zero in this case).
