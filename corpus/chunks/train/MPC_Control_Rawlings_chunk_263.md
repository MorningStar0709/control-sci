# 2.5.3.1 Linear Systems

The system to be controlled is $x ^ { + } = A x + B u$ where A is not necessarily stable, the control u is subject to the constraint $u \in \mathbb { V }$ where U is compact and contains the origin in its interior, and the state x is subject to the constraint $x \in \mathbb { X }$ where X is closed and contains the origin in its interior. The stage cost is $\ell ( x , u ) = ( 1 / 2 ) ( x ^ { \prime } Q x + u ^ { \prime } R u )$ where Q and R are positive definite. Because of the constraints, it is difficult to obtain a global CLF. Hence we restrict ourselves to the more modest goal of obtaining a local CLF and proceed as follows. If $( A , B )$ is stabilizable, the solution to the infinite horizon unconstrained optimal control problem $\mathbb { P } _ { \infty } ^ { \mathrm { u c } } ( x )$ is known; the value function for this problem is $V _ { \infty } ^ { \mathrm { u c } } ( x ) = ( 1 / 2 ) x ^ { \prime } P x$ where P is the unique (in the class of positive semidefinite matrices) solution to the discrete algebraic Riccati equation

$$P = A _ {K} ^ {\prime} P A _ {K} + Q ^ {*}$$

in which $A _ { K } : = A + B K , Q ^ { * } : = Q + K ^ { \prime } R K$ , and $u = K x$ , in which K is defined by

$$K := - (B ^ {\prime} P B + R) ^ {- 1} B ^ {\prime} P A ^ {\prime}$$

is the optimal controller. The value function $V _ { \infty } ^ { \mathrm { u c } } ( \cdot )$ for the infinite horizon unconstrained optimal control problem $\mathbb { P } _ { \infty } ^ { \mathrm { u c } } ( x )$ satisfies

$$V _ {\infty} ^ {\mathrm{uc}} (x) = \min _ {u} \left\{\ell (x, u) + V _ {\infty} ^ {\mathrm{uc}} (A x + B u) \right\} = \ell (x, K x) + V _ {\infty} ^ {\mathrm{uc}} (A _ {K} x)$$

It is known that P is positive definite. We define the terminal cost $V _ { f } ( \cdot )$ by

$$V _ {f} (x) := V _ {\infty} ^ {\mathrm{uc}} (x) = (1 / 2) x ^ {\prime} P x$$

If X and U are polyhedral, problem $\mathbb { P } _ { N } ( x )$ is a parametric quadratic program that may be solved online using standard software. The terminal cost function $V _ { f } ( \cdot )$ satisfies

$$V _ {f} (A _ {K} x) + (1 / 2) x ^ {\prime} Q ^ {*} x - V _ {f} (x) \leq 0 \forall x \in \mathbb {R} ^ {n}$$
