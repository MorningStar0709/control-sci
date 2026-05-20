$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| = s ^ {2} + \sqrt {\mu + 2} s + 1 = 0$$

if $\mu = 1$ , the two closed-loop poles are located at

$$s = - 0. 8 6 6 + j 0. 5, \quad s = - 0. 8 6 6 - j 0. 5$$

These correspond to the desired closed-loop poles when $\mu = 1$ .

Solving Quadratic Optimal Regulator Problems with MATLAB. In MATLAB, the command

$$\operatorname{lqr} (A, B, Q, R)$$

solves the continuous-time, linear, quadratic regulator problem and the associated Riccati equation. This command calculates the optimal feedback gain matrix K such that the feedback control law

$$u = - \mathbf {K x}$$

minimizes the performance index

$$J = \int_ {0} ^ {\infty} (\mathbf {x} ^ {*} \mathbf {Q x} + \mathbf {u} ^ {*} \mathbf {R u}) d t$$

subject to the constraint equation

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}$$

Another command

$$[ K, P, E ] = \operatorname{lqr} (A, B, Q, R)$$

returns the gain matrix K, eigenvalue vector E, and matrix P, the unique positive-definite solution to the associated matrix Riccati equation:

$$\mathbf {P} \mathbf {A} + \mathbf {A} ^ {*} \mathbf {P} - \mathbf {P B R} ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} + \mathbf {Q} = \mathbf {0}$$

If matrix A-BK is a stable matrix, such a positive-definite solution P always exists.The eigenvalue vector E gives the closed-loop poles of A-BK.

It is important to note that for certain systems matrix A-BK cannot be made a stable matrix, whatever K is chosen. In such a case, there does not exist a positive-definite matrix P for the matrix Riccati equation. For such a case, the commands

$$K = \operatorname{lqr} (A, B, Q, R)[ K, P, E ] = \operatorname{lqr} (A, B, Q, R)$$

do not give the solution. See MATLAB Program 10–18.
