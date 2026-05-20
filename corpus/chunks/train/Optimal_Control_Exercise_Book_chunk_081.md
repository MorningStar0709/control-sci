# Solution:

We first find the Hamilton-Jacobi-Bellman equation which can be written as following with the simplified notation (implicit time-dependence of $u = u ( t )$ and $x = x ( t ) )$ :

$$- \frac {\partial \hat {V} (t , x)}{\partial t} = \inf _ {u \in \mathbb {R} ^ {m}} \left[ L (t, x, u) + \left\langle \frac {\partial}{\partial x} \hat {V} (t, x, u), f (t, x, u) \right\rangle \right] \tag {362}$$

where in this case, $u \in \mathbb { R }$ . We can then rewrite the equation as following:

$$- \hat {V} _ {t} (t, x) = \min _ {u \in R} \left[ x (t) ^ {2} u (t) ^ {2} + \hat {V} _ {x} (t, x) x (t) u (t) \right] \tag {363}$$

where we have substituted the infimum with the minimum; this is due to the problem’s convexity. We can then find the $u ( t )$ minimizing the equation by setting the first derivative with respect to u equal to 0 (we use the simplified notation here too):

$$\frac {\partial}{\partial u} \left(x ^ {2} u ^ {2} + \hat {V} _ {x} x u\right) = 0 \tag {364}\Longrightarrow 2 u x ^ {2} + \hat {V} _ {x} x = 0 \tag {365}\Longrightarrow u ^ {*} (t) = - \frac {\hat {V} _ {x} (t , x)}{2 x} \tag {366}$$

We can consider a candidate for the value function that is as quadratic in x:

$$\hat {V} (t, x) = s (t) x ^ {2} \tag {368}$$

Its derivatives then can be written as:

$$\hat {V} _ {t} (t, x) = \frac {\partial}{\partial t} s (t) x ^ {2} = \dot {s} (t) x ^ {2} \tag {369}\hat {V} _ {x} (t, x) = \frac {\partial}{\partial x} s (t) x ^ {2} = 2 s (t) x \tag {370}$$

The optimal control can thus be rewritten as $\begin{array} { r } { u ^ { * } ( t ) = - \frac { \hat { V } _ { x } ( t , x ) } { 2 x } = - s ( t ) } \end{array}$ − Vˆx(t,x) = −s(t). Substituting 2x the value function in the HJB equation we get:

$$\hat {V} _ {t} (t, x) = L \left(t, x, u ^ {*}\right) + \hat {V} _ {x} (t, x) \cdot f (t, x, u ^ {*}) \tag {372}\Longrightarrow \dot {s} (t) x ^ {2} = x ^ {2} u ^ {* 2} + 2 s (t) x ^ {2} u ^ {*} \tag {373}$$

substituting $u ^ { * }$ we obtain (374)

$$\dot {s} (t) x ^ {2} = x ^ {2} s ^ {2} (t) + 2 s (t) x ^ {2} (- s (t)) \tag {375}\dot {s} (t) = - s ^ {2} (t) \tag {376}$$

This first-order nonlinear ordinary differential equation yields the following solution:

$$s (t) = \frac {1}{c _ {1} + t} \tag {377}$$

In order to find the value of $s ( t )$ , we can apply the boundary condition for optimality for the final time $t _ { f i n a l } = 1$ , which is

$$\hat {V} (t _ {\text { final }}, x) = K (t _ {\text { final }}, x) \tag {378}$$

Since the final cost is 0, we have $\hat { V } ( t _ { 1 } , x ) = 0$ , yielding

$$s (1) = 0 \tag {379}$$
