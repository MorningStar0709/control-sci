# Solution:

For simplicity, let us consider the simplified notation $x = x ( t ) , u = u ( t )$ and $p = p ( t )$ . We first calculate the Hamiltonian as

$$H (t, x, u, p, p _ {0}) = \langle p, f (t, x, u) \rangle + p _ {0} L (t, x, u) \tag {296}$$

Given that the problem is with scalar variables only, we can write the Hamiltonian as:

$$H (t, x, u, p) = p u - \sqrt {1 + u ^ {2}} \tag {297}$$

Since the function is concave, we can find the maximal for the Hamiltonian by setting the derivative with respect to u equal to zero and considering the positive value for u:

$$\frac {\partial H}{\partial u} = p - \frac {u}{\sqrt {1 + u ^ {2}}} = 0 \tag {298}\Longrightarrow p ^ {2} + p ^ {2} u ^ {2} = u ^ {2} \tag {299}u ^ {2} = \left(\frac {p ^ {2}}{1 - p ^ {2}}\right) \tag {300}\Longrightarrow u = \sqrt {\frac {p ^ {2}}{1 - p ^ {2}}} \tag {301}$$

If we apply the optimality condition for $p ^ { * }$ , we get:

$$\dot {p} ^ {*} = - H _ {x} = - \frac {\partial}{\partial x} \left[ p u - \sqrt {1 + u ^ {2}} \right] = 0 \tag {303}\Longrightarrow p ^ {*} (t) = K, \quad \text { where } K \in \mathbb {R} \tag {304}$$

Moreover, given that this is a fixed-time, free-endpoint problem, we can also apply the boundary condition:

$$p ^ {*} (T) = p _ {0} ^ {*} K _ {x} (x ^ {*} (T)) = 0 \tag {305}$$

since the final cost K is 0. Therefore, since the optimal $p ^ { * } ( t )$ is constant, then $K = 0$ and we can write $p ^ { * } ( t ) = 0 , \forall t \in [ 0 , T ]$ ]. The optimal control then is:

$$u ^ {*} (t) = \sqrt {\frac {p ^ {*} (t) ^ {2}}{1 - p ^ {*} (t) ^ {2}}} \tag {306}\Longrightarrow u ^ {*} (t) = 0, \forall t \in [ 0, T ] \tag {307}$$

In this case, given that ${ \dot { x } } ( t ) = u ( t ) = 0$ , we will have that the state variable is constant; thus ${ \boldsymbol { x } } ( t ) = { \boldsymbol { x } } ( 0 ) = { \boldsymbol { x } } _ { 0 } , \forall t \in [ 0 , T ]$ .
