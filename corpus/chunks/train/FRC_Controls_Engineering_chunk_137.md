# 6.5 Closed-loop controller

With the control law $\mathbf { u } = \mathbf { K } ( \mathbf { r } - \mathbf { x } )$ , we can derive the closed-loop state-space equations. We’ll discuss where this control law comes from in subsection 7.7.

First is the state update equation. Substitute the control law into equation (6.1).

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {K} (\mathbf {r} - \mathbf {x})\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {K r} - \mathbf {B} \mathbf {K x}\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B K r} \tag {6.3}$$

Now for the output equation. Substitute the control law into equation (6.2).

$$\mathbf {y} = \mathbf {C x} + \mathbf {D} (\mathbf {K} (\mathbf {r} - \mathbf {x}))\mathbf {y} = \mathbf {C x} + \mathbf {D K r} - \mathbf {D K x}\mathbf {y} = (\mathbf {C} - \mathbf {D K}) \mathbf {x} + \mathbf {D K r} \tag {6.4}$$

Instead of commanding the system to a state using the vector u directly, we can now specify a vector of desired states through r and the controller will choose values of u for us over time that drive the system toward the reference.

The eigenvalues of A − BK are the poles of the closed-loop system. Therefore, the rate of convergence and stability of the closed-loop system can be changed by moving the poles via the eigenvalues of A − BK. A and B are inherent to the system, but K can be chosen arbitrarily by the controller designer. For equation (6.3) to reach steady-state, the eigenvalues of A − BK must be in the left-half plane. There will be steady-state error if $\mathbf { A r } \neq \mathbf { 0 }$ .

<table><tr><td>Symbol</td><td>Name</td><td>Rows × Columns</td></tr><tr><td>A</td><td>system matrix</td><td>states × states</td></tr><tr><td>B</td><td>input matrix</td><td>states × inputs</td></tr><tr><td>C</td><td>output matrix</td><td>outputs × states</td></tr><tr><td>D</td><td>feedthrough matrix</td><td>outputs × inputs</td></tr><tr><td>K</td><td>controller gain matrix</td><td>inputs × states</td></tr><tr><td>r</td><td>reference vector</td><td>states × 1</td></tr><tr><td>x</td><td>state vector</td><td>states × 1</td></tr><tr><td>u</td><td>input vector</td><td>inputs × 1</td></tr><tr><td>y</td><td>output vector</td><td>outputs × 1</td></tr></table>

Table 6.2: Controller matrix dimensions
