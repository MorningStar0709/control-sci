# 4.4 LQR with a Specified Degree of Stability

In this section, we examine the state regulator system with infinite time interval and with a specified degree of stability for a time-invariant system $[3, 2]$ . Let us consider a linear time-invariant plant as

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t); \quad \mathbf {x} (t = t _ {0}) = \mathbf {x} (0), \tag {4.4.1}$$

and the cost functional as

$$J = \frac {1}{2} \int_ {t _ {0}} ^ {\infty} e ^ {2 \alpha t} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) \right] d t \tag {4.4.2}$$

where, $\alpha$ is a positive parameter. Here, we first assume that the pair $[A + \alpha \mathbf{I}, B]$ is completely stabilizable and $\mathbf{R}$ and $\mathbf{Q}$ are constant, symmetric, positive definite and positive semidefinite matrices, respectively. The problem is to find the optimal control which minimizes the performance index (4.4.2) under the dynamical constraint (4.4.1).

This can be solved by modifying the previous system to fit into the standard infinite-time regulator system discussed earlier in Chapter 3. Thus, we make the following transformations

$$\hat {\mathbf {x}} (t) = e ^ {\alpha t} \mathbf {x} (t); \quad \hat {\mathbf {u}} (t) = e ^ {\alpha t} \mathbf {u} (t). \tag {4.4.3}$$

Then, using the transformations (4.4.3), it is easy to see that the modified system becomes

$$
\begin{array}{l} \dot {\hat {\mathbf {x}}} (t) = \frac {d}{d t} \left\{e ^ {\alpha t} \mathbf {x} (t) \right\} = \alpha e ^ {\alpha t} \mathbf {x} (t) + e ^ {\alpha t} \dot {\mathbf {x}} (t) \\ = \alpha \hat {\mathbf {x}} (t) + e ^ {\alpha t} [ \mathbf {A x} (t) + \mathbf {B u} (t) ] \\ \dot {\hat {\mathbf {x}}} (t) = (\mathbf {A} + \alpha \mathbf {I}) \hat {\mathbf {x}} (t) + \mathbf {B} \hat {\mathbf {u}} (t). \tag {4.4.4} \\ \end{array}
$$

We note that the initial conditions for the original system (4.4.1) and the modified system (4.4.4) are simply related as $\hat{\mathbf{x}}(t_{0}) = e^{\alpha t_{0}}\mathbf{x}(t_{0})$ and in particular, if $t_{0} = 0$ the initial conditions are the same for the original and modified systems. Also, using the transformations (4.4.3), the original performance measure (4.4.2) can be modified to
