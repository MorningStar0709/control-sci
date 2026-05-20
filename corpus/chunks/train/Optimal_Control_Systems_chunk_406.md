# 7.4.1 Problem Statement

Let us consider a linear, time-invariant system

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {7.4.1}$$

where, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are n- and r-dimensional state and control vectors, respectively. Let us assume that the control $\mathbf{u}(t)$ is constrained as

$$- 1 \leq \mathbf {u} (t) \leq + 1 \quad \text { or } \quad | \mathbf {u} (t) | \leq 1 \tag {7.4.2}$$

or component wise,

$$| u _ {j} (t) | \leq 1 \quad j = 1, 2, \dots , r. \tag {7.4.3}$$

Our problem is to find the optimal control $\mathbf{u}^{*}(t)$ which transfers the system (7.4.1) from any initial condition $\mathbf{x}(0)$ to a given final state (usually the origin) and minimizes the performance measure

$$J (\mathbf {u}) = \int_ {0} ^ {t _ {f}} \sum_ {j = 1} ^ {r} | u _ {j} (t) | d t. \tag {7.4.4}$$
