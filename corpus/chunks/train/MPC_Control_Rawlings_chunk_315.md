# Exercise 2.8: Terminal penalty with and without terminal constraint

Consider the system

$$x ^ {+} = A x + B u$$

subject to the constraints

$$x \in \mathbb {X} \quad u \in \mathbb {U}$$

![](image/050c6a74defa02cf9f11fccb0c8ca1e01558d3688eb16b510467a2900f905f4f.jpg)  
Figure 2.9: The region of attraction for terminal constraint $x ( N ) \in$ $\mathbb { X } _ { f }$ and terminal penalty $V _ { f } ( x ) = ( 1 / 2 ) x ^ { \prime } \Pi x$ and the estimate of $\bar { \mathcal { X } } _ { N }$ for Exercise 2.8.

in which

$$
A = \left[ \begin{array}{c c} 2 & 1 \\ 0 & 2 \end{array} \right] \qquad B = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right]
$$

and

$$\mathbb {X} = \left\{x \in \mathbb {R} ^ {2} \mid - 1 5 \leq x _ {1} \leq 1 5 \right\} \quad \mathbb {U} = \left\{u \in \mathbb {R} ^ {2} \mid - 5 \cdot \mathbf {1} \leq u \leq 5 \cdot \mathbf {1} \right\}$$

The cost is

$$V _ {N} (x, \mathbf {u}) = \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

in which

$$
\ell (x, u) = (1 / 2) (| x | _ {Q} ^ {2} + | u |) ^ {2} \qquad Q = \left[ \begin{array}{c c} \alpha & 0 \\ 0 & \alpha \end{array} \right]
$$

$V _ { f } ( \cdot )$ is the terminal penalty on the final state, and $\mathbf { 1 } \in \mathbb { R } ^ { 2 }$ is a vector of ones.

Use $\alpha = 1 0 ^ { - 5 }$ and $N = 3$ and terminal cost $V _ { f } ( x ) = ( 1 / 2 ) x ^ { \prime } \Pi x$ where $V _ { f } ( \cdot )$ is the infinite horizon optimal cost for the unconstrained problem.

(a) Add a terminal constraint $x ( N ) \in \mathbb { X } _ { f }$ , in which $\mathbb { X } _ { f }$ is the maximal constraint admissible set for the system $x ^ { + } = \overset { \cdot } { ( A + B K ) } x$ and K is the optimal controller gain for the unconstrained problem. Using the code developed in Exercise 2.7, estimate $x _ { N }$ , the region of attraction for the MPC problem with this terminal constraint and terminal cost. Also estimate ${ \bar { X } } _ { N }$ , the region for which the MPC control sequence for horizon N is equal to the the MPC control sequence for infinite horizon. Your results should resemble Figure 2.9   
(b) Remove the terminal constraint and estimate the domain of attraction $\hat { X } _ { N }$ (by simulation). Compare this $\hat { X } _ { N }$ with $x _ { N }$ and ${ \bar { X } } _ { N }$ obtained previously.
