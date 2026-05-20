# 6.12.2 Controllability Gramian

While the rank of the observability matrix can tell us whether the system is controllable, it won’t tell us which specific states are controllable or how controllable. The controllability Gramian can be used to determine these things.

If A is stable, the controllability Gramian $\mathbf { W } _ { c }$ is the unique solution to the following continuous Lyapunov equation.

$$\mathbf {A} \mathbf {W} _ {c} + \mathbf {W} _ {c} \mathbf {A} ^ {\top} + \mathbf {B} \mathbf {B} ^ {\top} = 0 \tag {6.38}$$

Alternatively,

$$\mathbf {W} _ {c} = \int_ {0} ^ {\infty} e ^ {\mathbf {A} \tau} \mathbf {B} \mathbf {B} ^ {\top} e ^ {\mathbf {A} ^ {\top} \tau} d \tau \tag {6.39}$$

If the solution is positive definite, the system is controllable. The eigenvalues of $\mathbf { W } _ { c }$ represent how controllable their respective states are (larger means more controllable).
