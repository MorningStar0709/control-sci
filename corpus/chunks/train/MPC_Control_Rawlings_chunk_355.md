# 3.2.1 Introduction

Because feedback MPC is complex, it is natural to inquire if nominal MPC, i.e., MPC based on the nominal system ignoring uncertainty, is sufficiently robust to uncertainty. Before proceeding with a detailed analysis, a few comments may be helpful.

MPC uses, as a Lyapunov function, the value function of a parametric optimal control problem. Often the value function is continuous, but this is not necessarily the case, especially if state and/or terminal constraints are present. It is also possible for the value function to be continuous but the associated control law to be discontinuous; this can happen, for example, if the minimizing control is not unique.

It is important to realize that a control law may be stabilizing but not robustly stabilizing; arbitrary perturbations, no matter how small, can destabilize the system. Teel (2004) illustrates this point with the following discontinuous autonomous system $( n = 2 , x = ( x _ { 1 } , x _ { 2 } ) )$

$$
x ^ {+} = f (x) \qquad f (x) = \left\{ \begin{array}{l l} (0, | x |) & x _ {1} \neq 0 \\ (0, 0) & \text { otherwise } \end{array} \right.
$$

If the initial state is $x = ( 1 , 1 )$ , then $\phi ( 1 ; x ) = ( 0 , \sqrt { 2 } )$ and $\phi ( 2 ; x ) =$ (0, 0), with similar behavior for other initial states. In fact, all solutions satisfy

$$\phi (k; x) \leq \beta (| x |, k)$$

in which $\beta ,$ defined by

$$\beta (| x |, k) := | x | \max \{2 - k, 0 \}$$

is a KL function, so that the origin is globally asymptotically stable. Consider now a perturbed system satisfying

$$
x ^ {+} = \left[ \begin{array}{c} \delta \\ | x | + \delta \end{array} \right]
$$

in which $\delta > 0$ is a constant perturbation that causes $x _ { 1 }$ to remain strictly positive. If the initial state is $x = \varepsilon ( 1 , 1 )$ , then $x _ { 1 } ( k ) = \delta$ for $k \geq 1$ , and $x _ { 2 } ( k ) > \varepsilon \sqrt { 2 } + k \delta  \infty$ as $k  \infty$ , no matter how small δ and ε are. Hence the origin is unstable in the presence of an arbitrarily small perturbation; global asymptotic stability is not a robust property of this system.

This example may appear contrived but, as Teel (2004) points out, it can arise in receding horizon optimal control of a continuous system. Consider the following system

$$
x ^ {+} = \left[ \begin{array}{c} x _ {1} (1 - u) \\ | x |   u \end{array} \right]
$$
