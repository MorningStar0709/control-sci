# Definition 6.3.1 — Continuous state-space notation.

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \tag {6.1}\mathbf {y} = \mathbf {C x} + \mathbf {D u} \tag {6.2}$$

A system matrix x state vector   
B input matrix u input vector   
C output matrix y output vector   
D feedthrough matrix

<table><tr><td>Matrix</td><td>Rows × Columns</td><td>Matrix</td><td>Rows × Columns</td></tr><tr><td>A</td><td>states × states</td><td>x</td><td>states × 1</td></tr><tr><td>B</td><td>states × inputs</td><td>u</td><td>inputs × 1</td></tr><tr><td>C</td><td>outputs × states</td><td>y</td><td>outputs × 1</td></tr><tr><td>D</td><td>outputs × inputs</td><td></td><td></td></tr></table>

Table 6.1: State-space matrix dimensions

The change in state and the output are linear combinations of the state vector and the input vector. The A and B matrices are used to map the state vector x and the input vector u to a change in the state vector x˙ . The C and D matrices are used to map the state vector x and the input vector u to an output vector y.
