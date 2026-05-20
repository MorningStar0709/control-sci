# 5.6.1 Introduction

For simplicity, we consider here the following uncertain, discrete time, nonlinear system

$$x ^ {+} = f (x, u) + w \quad y = h (x) + v \tag {5.33}$$

where $\boldsymbol { x } \in \mathbb { R } ^ { n }$ is the current state, $u \in \mathbb { R } ^ { m }$ is the current control action, $x ^ { + }$ is the successor state, $\boldsymbol { w } \in \mathbb { R } ^ { n }$ is an unknown state disturbance, $y \in$ $\mathbb { R } ^ { p }$ is the current measured output, and $\boldsymbol { \nu } \in \mathbb { R } ^ { p }$ is an unknown output disturbance. The state and additive disturbances w and ν are known only to the extent that they lie, respectively, in the C sets $\mathbb { W } \subseteq \mathbb { R } ^ { n }$ and $\mathbb { N } \subseteq \mathbb { R } ^ { p }$ . Let $\phi ( i ; x ( 0 ) , { \mathbf { u } } , { \mathbf { w } } )$ denote the solution of (5.9) at time i if the initial state at time 0 is $x ( 0 )$ , and the control and disturbance sequences are, respectively, $\mathbf { u } : = \{ u ( 0 ) , u ( 1 ) , \ldots \}$ and $\mathbf { w } : = \{ w ( 0 ) , w ( 1 ) , \ldots \}$ . The system (5.33) is subject to the following set of hard state and control constraints

$$(x, u) \in \mathbb {X} \times \mathbb {U}$$

in which $\mathbb { X } \subseteq \mathbb { R } ^ { n }$ and $\mathbb { U } \subseteq \mathbb { R } ^ { m }$ are polyhedral and polytopic sets, respectively, with each set containing the origin in its interior. Output MPC of nonlinear systems remains an active area of research; the proposals to follow are speculative.
