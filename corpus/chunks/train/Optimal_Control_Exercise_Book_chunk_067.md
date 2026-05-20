# Solution:

The problem can be written as

$$u ^ {*} := \underset {u: [ 0, T ] \rightarrow \mathbb {R}} {\operatorname{argmin}} J (u) = \int_ {0} ^ {T} - e ^ {- \beta t} \sqrt {u (t)} d t \tag {272}$$

subject to (273)

$$\dot {x} (t) = \alpha x (t) - u (t), \quad x (0) = S, \quad x (T) = 0 \tag {274}$$

where minimizing the negative enjoyment is the same as maximizing the positive one.

We first calculate the Hamiltonian as in Equation 311 with the simplified notation $\begin{array} { r } { x = x ( t ) , u = u ( t ) , p = p ( t ) } \end{array}$ , considering that the problem is with scalar variables only:

$$H (t, x, u, p) = p (\alpha x - u) + e ^ {- \beta t} \sqrt {u} \tag {275}$$

Then, the costate equation is as following:

$$\dot {p} = - H _ {x} \left(t, x ^ {*}, u ^ {*}, p\right) = - \alpha p \tag {276}$$

Solving this differential equation we get that $p ( t ) = c _ { 1 } e ^ { - \alpha t }$ . The maximizing $u ^ { * }$ will be:

$$u ^ {*} = \underset {u \in [ 0, T ]} {\operatorname{argmax}} H \left(x ^ {*}, u, p\right) \tag {277}= \underset {u \in [ 0, T ]} {\operatorname{argmax}} \left(p \left(\alpha x ^ {*} - u\right) + e ^ {- \beta t} \sqrt {u}\right) \tag {278}$$

Which is a maximum if the first derivative is equal to zero and the second derivative $\mathrm { i s } \leq 0$ . Thus:

$$\frac {d}{d u} H = e ^ {- \beta t} \frac {1}{2} u ^ {- \frac {1}{2}} - p = 0 \tag {279}\Longrightarrow u ^ {*} (t) = \frac {1}{4 p ^ {2}} e ^ {- 2 \beta t} \tag {280}$$

also

$$\frac {d ^ {2}}{d u ^ {2}} H = - e ^ {- \beta t} \frac {1}{4} u ^ {- \frac {3}{2}} \leq 0 \tag {281}$$

$\mathrm { S o } .$ , we verified that $\begin{array} { r } { u ^ { * } ( t ) = \frac { 1 } { 4 p ^ { 2 } } e ^ { - 2 \beta t } } \end{array}$ is indeed a maximum. Plugging $p$ in we get

$$u ^ {*} (t) = \frac {1}{4 c _ {1} ^ {2}} e ^ {(2 \alpha - 2 \beta) t} \tag {283}$$

In order to obtain the optimal solution, we need to solve the linear ODE given by the state

$$\dot {x} = \alpha x - \frac {1}{4 c _ {1} ^ {2}} e ^ {(2 \alpha - 2 \beta) t} \tag {284}$$

The solution to the ODE will be in the form $x ( t ) = x _ { h } ( t ) + x _ { p } ( t )$ where $x _ { h } ( t )$ is the homogeneous solution and $x _ { p } ( t )$ is a particular solution . The homogeneous solution is:

$$x _ {h} (t) = c _ {2} e ^ {\alpha t}, \quad c _ {2} = \text { constant } \tag {285}$$

The particular solution can be divided in two cases:

1. Case: $\alpha \neq 2 \beta \colon$ Solving the ODE we get the general solution:

$$x (t) = x _ {h} (t) + x _ {p} (t) = c _ {2} e ^ {\alpha t} - \frac {1}{4 c _ {1} ^ {2} (\alpha - 2 \beta)} e ^ {(2 \alpha - 2 \beta) t} \tag {286}$$
