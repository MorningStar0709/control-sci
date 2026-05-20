As before in the case of finite final-time interval, we can proceed and obtain the closed-loop optimal control and the associated Riccati equation. Still $\mathbf{P}(t)$ must be the solution of the matrix differential Riccati equation (3.2.34) with boundary condition $\mathbf{P}(t_{f}) = 0$ . It was shown that the assumptions of [70]

1. controllability and

2. $F(t_{f}) = 0$

imply that

$$\lim _ {t _ {f} \to \infty} \{\mathbf {P} (t _ {f}) \} = \bar {\mathbf {P}} \tag {3.5.4}$$

where, $\bar{P}$ is the nxn positive definite, symmetric, constant matrix. If $\bar{P}$ is constant, then $\bar{P}$ is the solution of the nonlinear, matrix, algebraic Riccati equation (ARE),

$$\frac {d \bar {\mathbf {P}}}{d t} = 0 = - \bar {\mathbf {P}} \mathbf {A} - \mathbf {A} ^ {\prime} \bar {\mathbf {P}} + \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} - \mathbf {Q}. \tag {3.5.5}$$

Alternatively, we can write (3.5.5) as

$$\bar {\mathbf {P}} \mathbf {A} + \mathbf {A} ^ {\prime} \bar {\mathbf {P}} + \mathbf {Q} - \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} = 0. \tag {3.5.6}$$

Note, for a time-varying system with finite-time interval, we have the differential Riccati equation (3.2.34), whereas for a linear time-invariant system with infinite-time horizon, we have the algebraic Riccati equation (3.5.6).

A historical note on R.E. Kalman is appropriate (from SIAM News, 6/94 - article about R.E. Kalman).
