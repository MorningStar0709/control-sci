# 6.2 Pontryagin Minimum Principle

subject to the constraint relation

$$| u | \leq 2, \longrightarrow - 2 \leq u \leq + 2. \tag {6.2.24}$$

Solution: First let us use a relation similar to (6.1.5) for unconstrained control as

$$\frac {\partial H}{\partial u} = 0 \longrightarrow 2 u ^ {*} - 6 = 0 \longrightarrow u ^ {*} = 3 \tag {6.2.25}$$

and the corresponding optimal $H^{*}$ from (6.2.23) becomes

$$H ^ {*} = 3 ^ {2} - 6 \mathrm{x} 3 + 7 = - 2. \tag {6.2.26}$$

This value of $u^{*} = 3$ is certainly outside the constraint (admissible) region specified by (6.2.24). But, using the relation (6.2.18) for the constrained control, we have

$$H (u ^ {*}) \leq H (u),H (u ^ {* ^ {2}} - 6 u ^ {*} + 7) \leq H (u ^ {2} - 6 u + 7). \tag {6.2.27}$$

The complete situation is depicted in Figure 6.2 which shows that the admissible optimal value is $u^{*} = +2$ and the corresponding optimal $H^{*}$ is

$$H ^ {*} = 2 ^ {2} - 6 \mathrm{x} 2 + 7 = - 1. \tag {6.2.28}$$

However, let us note if our constraint relation (6.2.24) had been

$$| u | \leq 3, \longrightarrow - 3 \leq u \leq + 3 \tag {6.2.29}$$

then, we are lucky to use the relation similar to (6.1.5) or (6.2.25) and obtain the optimal value as $u^{*} = 3$ . But, in general this is not true.
