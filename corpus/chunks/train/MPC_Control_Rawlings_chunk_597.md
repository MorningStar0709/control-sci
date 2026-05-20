# 5.3.1 Introduction

We consider the following uncertain linear time-invariant system

$$x ^ {+} = A x + B u + wy = C x + \nu \tag {5.9}$$

in which $x \in \mathbb { R } ^ { n }$ is the current state, $u \in \mathbb { R } ^ { m }$ is the current control action, $x ^ { + }$ is the successor state, $\boldsymbol { w } \in \mathbb { R } ^ { n }$ is an unknown state disturbance, $\boldsymbol { y } \in \mathbb { R } ^ { p }$ is the current measured output, $\boldsymbol { \nu } \in \mathbb { R } ^ { p }$ is an unknown output disturbance, the pair (A, B) is assumed to be controllable, and the pair (A, C) observable. The state and additive disturbances w and ν are known only to the extent that they lie, respectively, in the C-$\operatorname { s e t s } ^ { 2 } \mathbb { W } \subseteq \mathbb { R } ^ { n }$ and $\mathbb { N } \subseteq \mathbb { R } ^ { p }$ . Let $\phi ( i ; x ( 0 ) , { \mathbf { u } } , { \mathbf { w } } )$ denote the solution of (5.9) at time i if the initial state at time 0 is x(0), and the control and disturbance sequences are, respectively, $\mathbf { u } : = \{ u ( 0 ) , u ( 1 ) , \ldots \}$ and $\mathbf { w } : = \{ w ( 0 ) , w ( 1 ) , \ldots \}$ . The system (5.9) is subject to the following set of hard state and control constraints

$$x \in \mathbb {X} \quad u \in \mathbb {U} \tag {5.10}$$

where $\mathbb { X } \subseteq \mathbb { R } ^ { n }$ and $\mathbb { U } \subseteq \mathbb { R } ^ { m }$ are polyhedral and polytopic sets respectively; both sets contain the origin as an interior point.
