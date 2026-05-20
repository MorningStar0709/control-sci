$$
\delta \dot {\mathbf {x}} = \left[ \begin{array}{c c c} - R / L & 0 & 0 \\ 0 & 0 & 1 \\ 2 K _ {F} x _ {1} / m (d - x _ {2}) ^ {2} & 2 K _ {F} x _ {1} ^ {2} / m (d - x _ {2}) ^ {3} & 0 \end{array} \right] \Bigg | _ {*} \delta \mathbf {x} + \left[ \begin{array}{c c} 1 / L & 0 \\ 0 & 0 \\ 0 & - 1 \end{array} \right] \Bigg | _ {*} \delta \mathbf {u} \tag {11.73}
$$

Next, we evaluate the two matrices using $x _ { 1 } ^ { * } = 0 . 8 \mathrm { A }$ (nominal current), $x _ { 2 } ^ { * } = 0$ (nominal position), and the numerical parameters for $R , L , K _ { F } , m$ , and d. The linearized state equation (11.73) becomes

$$
\delta \dot {\mathbf {x}} = \left[ \begin{array}{c c c} - 2 7 7. 7 7 7 8 & 0 & 0 \\ 0 & 0 & 1 \\ 2 4. 5 2 5 & 8 1 7. 5 & 0 \end{array} \right] \delta \mathbf {x} + \left[ \begin{array}{c c} 5 5. 5 5 5 6 & 0 \\ 0 & 0 \\ 0 & - 1 \end{array} \right] \delta \mathbf {u} \tag {11.74}
$$

The $3 \times 3$ square matrix in $\operatorname { E q . }$ (11.74) is the system matrix A and the $3 \times 2$ matrix is the input matrix B. We can check the eigenvalues of the open-loop system by computing the determinant

$$
\det [ \lambda \mathbf {I} - \mathbf {A} ] = \det {\left[ \begin{array}{c c c} \lambda + 2 7 7. 7 7 7 8 & 0 & 0 \\ 0 & \lambda & - 1 \\ - 2 4. 5 2 5 & - 8 1 7. 5 & \lambda \end{array} \right]} = 0
$$

Using MATLAB we determine that the three eigenvalues are $\lambda _ { 1 } = - 2 7 7 . 7 7 7 8$ , and $\lambda _ { 2 , 3 } = \pm 2 8 . 5 9 2 0$ . Hence, the linearized maglev system is unstable owing to the positive eigenvalue (root) at $\lambda _ { 2 } = + 2 8 . 5 9 2 0$ . This result is not surprising because the maglev system has no natural feedback mechanism (such as stiffness or damping) that will return the ball back to its original equilibrium position if it is disturbed.

Although we have derived the linearized maglev system using state-space methods, it is advantageous to construct the linear system in terms of transfer functions so that we can use root-locus methods. To do this, let us rewrite the first and third linearized state equations in Eq. (11.74) with the substitutions $\delta x _ { 1 } = \delta I$ , $\delta x _ { 2 } = \delta z , \delta x _ { 3 } = \delta \dot { z } .$ , and $\delta u _ { 1 } = \delta e _ { \mathrm { i n } }$

${ \mathrm { F i r s t ~ s t a t e ~ e q u a t i o n } } ; \quad \delta { \dot { I } } = - 2 7 7 . 7 7 8 \delta { I } + 5 5 . 5 5 5 6 \delta { e _ { \mathrm { i n } } }$ (11.75)

$\mathrm { T h i r d ~ s t a t e ~ e q u a t i o n : ~ } \delta \ddot { z } = 2 4 . 5 2 5 \delta I + 8 1 7 . 5 \delta z - \delta g$ (11.76)
