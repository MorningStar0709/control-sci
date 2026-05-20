# 6.12.6 Observability Gramian

While the rank of the observability matrix can tell us whether the system is observable, it won’t tell us which specific states are observable or how observable. The observability Gramian can be used to determine these things.

If A is stable, the observability Gramian $\mathbf { W } _ { o }$ is the unique solution to the following continuous Lyapunov equation.

$$\mathbf {A} ^ {\top} \mathbf {W} _ {o} + \mathbf {W} _ {o} \mathbf {A} + \mathbf {C} ^ {\top} \mathbf {C} = 0 \tag {6.42}$$

Alternatively,

$$\mathbf {W} _ {o} = \int_ {0} ^ {\infty} e ^ {\mathbf {A} ^ {\top} \tau} \mathbf {C} ^ {\top} \mathbf {C} e ^ {\mathbf {A} \tau} d \tau \tag {6.43}$$

If the solution is positive definite, the system is observable. The eigenvalues of $\mathbf { W } _ { o }$ represent how observable their respective states are (larger means more observable).
