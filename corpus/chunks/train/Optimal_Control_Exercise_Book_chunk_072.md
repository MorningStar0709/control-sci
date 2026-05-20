# Solution:

Similarly to the previous exercise, let us consider the simplified notation $x = x ( t )$ , $u = u ( t )$ and $p = p ( t )$ . We first calculate the Hamiltonian as

$$H (t, x, u, p, p _ {0}) = \langle p, f (t, x, u) \rangle + p _ {0} L (t, x, u) \tag {311}$$

Given that the problem is with scalar variables only, we can write the Hamiltonian as:

$$H (t, x, u, p) = p u - \sqrt {1 + u ^ {2}} \tag {312}$$

Since the function is concave, we can find the maximal for the Hamiltonian by setting the derivative with respect to u equal to zero:

$$\frac {\partial H}{\partial u} = p - \frac {u}{\sqrt {1 + u ^ {2}}} = 0 \tag {313}\Longrightarrow p ^ {2} + p ^ {2} u ^ {2} = u ^ {2} \tag {314}u ^ {2} = \left(\frac {p ^ {2}}{1 - p ^ {2}}\right) \tag {315}\Longrightarrow u = \sqrt {\frac {p ^ {2}}{1 - p ^ {2}}} \tag {316}$$

If we apply the optimality condition for $p ^ { * }$ , we get:

$$\dot {p} ^ {*} = - H _ {x} = - \frac {\partial}{\partial x} \left(p u - \sqrt {1 + u ^ {2}}\right) = 0 \tag {318}\Longrightarrow p ^ {*} (t) = K, \quad \text { where } K \in \mathbb {R} \tag {319}$$

We now need to consider the condition on $x ( T ) = x _ { 1 }$ . Hence, given that $x ( 0 ) = x _ { 0 }$ （20号

$$\dot {x} = u \tag {320}\Longrightarrow x (T) - x (0) = \int_ {0} ^ {T} u d t = \int_ {0} ^ {T} \sqrt {\frac {p (t) ^ {2}}{1 - p (t) ^ {2}}} d t \tag {321}$$

since $p ( t ) = K \in \mathbb { R } , p$ does not depend on time t (322)

$$= \int_ {0} ^ {T} \sqrt {\frac {p ^ {2}}{1 - p ^ {2}}} d t = \sqrt {\frac {p ^ {2}}{1 - p ^ {2}}} T \tag {323}$$

By which we can obtain the value of $p \colon$

$$\left(\frac {x _ {1} - x _ {0}}{t}\right) ^ {2} = \frac {p ^ {2}}{1 - p ^ {2}} \tag {325}$$

For simplicity, we can substitute

$$\left(\frac {x _ {1} - x _ {0}}{T}\right) ^ {2} = \mathcal {V} \tag {326}$$

which has the physical meaning of the velocity of the system. from which we get:

$$\mathcal {V} ^ {2} = \frac {p ^ {2}}{1 - p ^ {2}} \tag {327}\Longrightarrow p = \sqrt {\frac {\mathcal {V}}{1 + \mathcal {V}}} \tag {328}$$

Then, plugging this $p ^ { * }$ back into the equation for the optimal control, we get:

$$u ^ {*} (t) = \sqrt {\frac {p ^ {2}}{1 - p ^ {2}}} = \sqrt {\frac {\frac {\nu}{1 + \nu}}{1 - \frac {\nu}{1 + \nu}}} = \sqrt {\frac {\frac {\nu}{1 + \nu}}{\frac {1 + \nu - \nu}{1 + \nu}}} = \sqrt {\mathcal {V}} \tag {329}$$

By substituting back the value of V, we get the optimal control as:

$$u ^ {*} (t) = \frac {x _ {1} - x _ {0}}{T}, \quad \forall t \in [ 0, T ] \tag {330}$$

Which means that the optimal control will be a constant velocity moving the system from $x _ { 0 }$ to $x _ { 1 }$ .
