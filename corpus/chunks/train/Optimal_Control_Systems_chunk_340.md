# 6.3.2 Optimal Control Using Dynamic Programming

Let us first consider the optimal control of a discrete-time system. Or even if there is a continuous-time system, one can easily discretize it to obtain the discrete-time system by using one of the several approaches $[82]$ . Let the plant be described by

$$\mathbf {x} (k + 1) = \mathbf {f} (\mathbf {x} (k), \mathbf {u} (k), k) \tag {6.3.2}$$

and the cost function be

$$J _ {i} (\mathbf {x} (k _ {i})) = J = S (\mathbf {x} (k _ {f}), k _ {f}) + \sum_ {k = i} ^ {k _ {f} - 1} V (\mathbf {x} (k), \mathbf {u} (k)) \tag {6.3.3}$$

where, $\mathbf{x}(k), \mathbf{u}(k)$ are the $n$ and $r$ state and control vectors, respectively. Note, we showed the dependence of $J$ on the initial time $(k)$ and state $(x(k))$ .

We are interested in using the principle of optimality to find the optimal control $\mathbf{u}^{*}(k)$ which applied to the plant (6.3.2) gives optimal state $\mathbf{x}^{*}(k)$ . Let us assume that we evaluated the optimal control, state and cost for all values starting from $k+1$ to $k_{f}$ . Then, at any time or stage k, we use the principle of optimality to write as

$$J _ {k} ^ {*} (\mathbf {x} (k)) = \min _ {\mathbf {u} (k)} \left[ V [ \mathbf {x} (k), \mathbf {u} (k) ] + J _ {k + 1} ^ {*} (\mathbf {x} ^ {*} (k + 1)) \right]. \tag {6.3.4}$$

The previous relation is the mathematical form of the principle of optimality as applied to optimal control system. It is also called functional equation of dynamic programming. Thus, it means that if one had found the optimal control, state and cost from any stage $k + 1$ to the final stage $k_{f}$ , then one can find the optimal values for a single stage from k to $k + 1$ .
