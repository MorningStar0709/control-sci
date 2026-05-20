Noting that $\boldsymbol { r } ( t )$ is a step input, we have $r ( \infty ) = r ( t ) = r ( \mathrm { c o n s t a n t } )$ for $t > 0 ,$ . By subtracting Equation (10–23) from Equation (10–22), we obtain

$$\dot {\mathbf {x}} (t) - \dot {\mathbf {x}} (\infty) = (\mathbf {A} - \mathbf {B K}) [ \mathbf {x} (t) - \mathbf {x} (\infty) ] \tag {10-24}$$

Define

$$\mathbf {x} (t) - \mathbf {x} (\infty) = \mathbf {e} (t)$$

Then Equation (10–24) becomes

$$\dot {\mathbf {e}} = (\mathbf {A} - \mathbf {B K}) \mathbf {e} \tag {10-25}$$

Equation (10–25) describes the error dynamics.

The design of the type 1 servo system here is converted to the design of an asymptotically stable regulator system such that $\mathbf { e } ( t )$ approaches zero, given any initial condition ${ \bf e } ( 0 )$ . If the system defined by Equation (10–19) is completely state controllable, then, by specifying the desired eigenvalues $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ for the matrix $\mathbf { A } - \mathbf { B } \mathbf { K }$ , matrix K can be determined by the pole-placement technique presented in Section 10–2.

The steady-state values of ${ \bf x } ( t )$ and $u ( t )$ can be found as follows: At steady state $( t = \infty )$ , we have, from Equation (10–22),

$$\dot {\mathbf {x}} (\infty) = \mathbf {0} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} (\infty) + \mathbf {B} k _ {1} r$$

Since the desired eigenvalues of A-BK are all in the left-half s plane, the inverse of matrix A-BK exists. Consequently, x(q) can be determined as

$$\mathbf {x} (\infty) = - (\mathbf {A} - \mathbf {B K}) ^ {- 1} \mathbf {B} k _ {1} r$$

Also, u(q) can be obtained as

$$u (\infty) = - \mathbf {K x} (\infty) + k _ {1} r = 0$$

(See Example 10–4 to verify this last equation.)
