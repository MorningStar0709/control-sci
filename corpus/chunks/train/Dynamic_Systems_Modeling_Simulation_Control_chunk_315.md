# Linear system simulation

The linear hydraulic model was developed in Example 5.10 by linearizing the nonlinear system Eq. (6.24) about a nominal (constant) input flow rate $Q _ { \mathrm { i n } } ^ { \ast }$ and the corresponding nominal (constant) pressure $P ^ { * }$ . The resulting linear hydraulic model is

$$\delta \dot {P} = \left. \frac {\partial f}{\partial P} \right| _ {*} \delta P + \left. \frac {\partial f}{\partial Q _ {\mathrm{in}}} \right| _ {*} \delta Q _ {\mathrm{in}} \tag {6.25}$$

where $\delta P = P - P ^ { * }$ and $\delta Q _ { \mathrm { i n } } = Q _ { \mathrm { i n } } - Q _ { \mathrm { i n } } ^ { * }$ are perturbations from their nominal conditions, and $\dot { P } = f ( P , Q _ { \mathrm { i n } } )$ is in the nonlinear ODE presented by Eq. (6.24). The first-order partial derivatives were determined in Example 5.10 and are repeated below

$$\left. \frac {\partial f}{\partial P} \right| _ {*} = \frac {- K _ {T} ^ {2}}{2 C Q _ {\text { in }} ^ {*}} \quad \left. \frac {\partial f}{\partial Q _ {\text { in }}} \right| _ {*} = \frac {1}{C} \tag {6.26}$$

The nominal pressure $P ^ { * }$ is

$$P ^ {*} = \frac {Q _ {\text { in }} ^ {* 2}}{K _ {T} ^ {2}} + P _ {\text { atm }} \tag {6.27}$$

which produces an equilibrium condition $( C { \dot { P } } = 0 )$ given a nominal volumetric flow $Q _ { \mathrm { i n } } ^ { \ast }$ . Using the numerical value for $K _ { T }$ and the nominal input flow rate $Q _ { \mathrm { i n } } ^ { \ast } = 0 . 0 5 \mathrm { m } ^ { 3 } / \mathrm { s }$ , the nominal pressure is $P ^ { * } = 1 . 1 6 9 5 5 ( 1 0 ^ { 5 } ) \mathrm { N } / \mathrm { m } ^ { 2 }$ . Using the numerical values for $C , K _ { T }$ , and $Q _ { \mathrm { i n } } ^ { \ast }$ we can compute the first-order partial derivatives in Eq. (6.26). Therefore, the linear model is

$$\delta \dot {P} = - 0. 0 0 8 \delta P + 5 0 0 0 \delta Q _ {\text { in }} \tag {6.28}$$
