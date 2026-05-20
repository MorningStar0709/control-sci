in which the control u is constrained to lie in the set $\mathbb { U } = [ - 1 , 1 ]$ . Suppose we choose a horizon length $N = 2$ and choose $\mathbb { X } _ { f }$ to be the origin. If $x _ { 1 } ~ \neq ~ 0$ , the only feasible control sequence steering x to 0 in two steps is $\mathbf { u } = \left\{ 1 , 0 \right\}$ ; the resulting state sequence is $\{ x , ( 0 , | x | ) , ( 0 , 0 ) \}$ . Since there is only one feasible control sequence, it is also optimal, and $\kappa _ { 2 } ( x ) = 1$ for all x such that $x _ { 1 } \neq 0$ . If $x _ { 1 } = 0$ , then the only optimal control sequence is $\mathbf { u } = \{ 0 , 0 \}$ and $\kappa _ { 2 } ( x ) = 0$ . The resultant closed-loop system satisfies

$$
x ^ {+} = f (x) := \left[ \begin{array}{c} x _ {1} (1 - \kappa_ {2} (x)) \\ | x |   \kappa_ {2} (x) \end{array} \right]
$$

in which $\kappa _ { 2 } ( x ) = 1 \mathrm { i f } x _ { 1 } \neq 0 .$ , and $\kappa _ { 2 } ( x ) = 0$ otherwise. Thus

$$
f (x) = \left\{ \begin{array}{l l} (0, | x |) & x _ {1} \neq 0 \\ (0, 0) & \text { otherwise } \end{array} \right. \tag {3.4}
$$

The system $x ^ { + } ~ = ~ f ( x )$ is the discontinuous system analyzed previously. Thus, receding horizon optimal control of a continuous system has resulted in a discontinuous system that is globally asymptotically stable but has no robustness.
