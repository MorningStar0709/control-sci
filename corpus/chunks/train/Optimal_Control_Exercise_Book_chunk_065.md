# Solution:

The problem can be rewritten as:

$$u ^ {*} := \underset {u: [ 0, T ] \rightarrow [ 0, 1 ]} {\operatorname{argmin}} J (u) = \int_ {0} ^ {T} - (1 - u (t)) x (t) d t \tag {254}$$

subject to (255)

$$\dot {x} (t) = k u (t) x (t) \tag {256}x (0) = x _ {0} \tag {257}$$

where minimizing the negative cost functional is the same as maximizing the positive one. We consider the Hamiltonian formulation as in the Equation 311 and for simplicity we consider the notation $x = x ( t )$ , $u = u ( t )$ and $p = p ( t )$ ), considering the scalar case. The Hamiltonian will be:

$$H (t, x, p, u) = p k u x + (1 - u) x \tag {258}$$

We can write the costate equation:

$$\dot {p} (t) = - H _ {x} = - p k u - (1 - u) = - 1 - u (p k - 1) \tag {259}$$

Let’s consider the set $\mathcal { U } \ : = \ : [ 0 , 1 ]$ for which $u \in \mathcal { U } .$ . Then, by the Pontryagin’s maximum principle, we have the following

$$
u ^ {*} (t) = \underset {u \in \mathcal {U}} {\operatorname{argmax}} H (t, x ^ {*}, u, p ^ {*}) \tag {260}= \underset {u \in \mathcal {U}} {\operatorname{argmax}} p k u x + (1 - u) x \tag {261}= \underset {u \in \mathcal {U}} {\operatorname{argmax}} (p k - 1) u x + x \tag {262}
= \left\{ \begin{array}{l l} 1 & \text { if } p ^ {*} > \frac {1}{k} \\ 0 & \text { if } p ^ {*} \leq \frac {1}{k} \end{array} \right. \tag {263}
$$

We notice that this is a bang-bang controller with a switching time controlled by the costate equation. By solving the costate equation, we can get the switching time. The terminal condition is

$$p (T) = K _ {x} (x (T)) = 0 \tag {264}$$

Therefore the ODE for the costate becomes:

$$
\left\{ \begin{array}{l} \dot {p} ^ {*} (t) = - 1 - u ^ {*} (t) \left(p ^ {*} (t) k - 1\right) \\ p ^ {*} (T) = 0 \end{array} \right. \tag {265}
$$

Since $p ( T ) = 0$ and $k > 0 .$ , then by continuity for t close to the final time $T$ we have that $\begin{array} { r } { p ( t ) \le \frac { 1 } { k } } \end{array}$ . In this case, $u ^ { * } ( t ) = 0$ and the ODE becomes:

$$
\left\{ \begin{array}{l} \dot {p} ^ {*} (t) = - 1 \\ p ^ {*} (T) = 0 \\ \Longrightarrow p ^ {*} (t) = T - t, \quad p ^ {*} (t) \leq \frac {1}{k} \end{array} \right. \tag {266}
$$

By which we can find the switching time $\hat { t } { : }$

$$T - \hat {t} = \frac {1}{k} \tag {267}\Longrightarrow \hat {t} = T - \frac {1}{k} \tag {268}$$

Therefore, the optimal control we found is:

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 1 & \text { if } t \in [ 0, \hat {t}) \\ 0 & \text { if } t \in [ \hat {t}, T ] \end{array} \right. \quad \text { for } \hat {t} = T - \frac {1}{k} \tag {269}
$$
