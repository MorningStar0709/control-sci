Given the initial condition of $x ( 0 ) = S$ and $x ( T ) = 0$ we get the unknown coefficients:

$$\frac {1}{4 c _ {1} ^ {2}} = \frac {- S (\alpha - 2 \beta)}{1 - e ^ {(\alpha - 2 \beta) T}} \tag {287}c _ {2} = \frac {- S e ^ {\alpha - 2 \beta) T}}{1 - e ^ {(\alpha - 2 \beta) T}} \tag {288}$$

2. Case $\alpha = 2 \beta$ : Solving the ODE we get the general solution:

$$x (t) = x _ {h} (t) + x _ {p} (t) = c _ {2} e ^ {\alpha t} - \frac {1}{4 c _ {1} ^ {2}} t e ^ {\alpha t} \tag {289}$$

Given the initial condition of $x ( 0 ) = S$ and $x ( T ) = 0$ we get the unknown coefficients:

$$\frac {1}{4 c _ {1} ^ {2}} = \frac {S}{T} \tag {290}c _ {2} = S \tag {291}$$

Therefore, the optimal control $u ^ { * }$ will be:

$$
u ^ {*} (t) = \left\{ \begin{array}{c l} \frac {S (2 \beta - \alpha)}{1 - e ^ {(\alpha - 2 \beta) T}} e ^ {(2 \alpha - 2 \beta) t}, & \text { for } \alpha \neq 2 \beta \\ \frac {S}{T} e ^ {(2 \alpha - 2 \beta) t} = \frac {S}{T} e ^ {\alpha t}, & \text { for } \alpha = 2 \beta \end{array} \right. \tag {292}
$$
