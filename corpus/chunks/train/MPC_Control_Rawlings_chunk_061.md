# 1.2.1 Linear Dynamic Models

Time-varying model. The most general linear state space model is the time-varying model

$$\frac {d x}{d t} = A (t) x + B (t) uy = C (t) x + D (t) ux (0) = x _ {0}$$

in which $A ( t ) \in \mathbb { R } ^ { n \times n }$ is the state transition matrix, $B ( t ) \in \mathbb { R } ^ { n \times m }$ is the input matrix, $C ( t ) \in \mathbb { R } ^ { p \times n }$ is the output matrix, and $D ( t ) \in \mathbb { R } ^ { p \times m }$ allows a direct coupling between u and $y .$ . In many applications $D = 0$ .

Time-invariant model. If A, B, C, and D are time invariant, the linear model reduces to

$$\frac {d x}{d t} = A x + B uy = C x + D u \tag {1.1}x (0) = x _ {0}$$

One of the main motivations for using linear models to approximate physical systems is the ease of solution and analysis of linear models.

Equation (1.1) can be solved to yield

$$x (t) = e ^ {A t} x _ {0} + \int_ {0} ^ {t} e ^ {A (t - \tau)} B u (\tau) d \tau \tag {1.2}$$

in which $e ^ { \boldsymbol { A } t } \in \mathbb { R } ^ { n \times n }$ is the matrix exponential.1 Notice the solution is a convolution integral of the entire u(t) behavior weighted by the matrix exponential of At. We will see later that the eigenvalues of A determine whether the past u(t) has more effect or less effect on the current x(t) as time increases.
