# THEOREM 2.2

Consider the extrema of a continuous, real-valued function $f(\mathbf{x}) = f(x_{1}, x_{2}, \cdots, x_{n})$ subject to the conditions

$$g _ {1} (\mathbf {x}) = g _ {1} (x _ {1}, x _ {2}, \dots , x _ {n}) = 0g _ {2} (\mathbf {x}) = g _ {2} (x _ {1}, x _ {2}, \dots , x _ {n}) = 0$$

...

$$g _ {m} (\mathbf {x}) = g _ {m} (x _ {1}, x _ {2}, \dots , x _ {n}) = 0 \tag {2.5.38}$$

where, f and g have continuous partial derivatives, and m < n. Let $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$ be the Lagrange multipliers corresponding to m conditions, such that the augmented Lagrangian function is formed as

$$\mathcal {L} (\mathbf {x}, \boldsymbol {\lambda}) = f (\mathbf {x}) + \boldsymbol {\lambda} ^ {\prime} \mathbf {g} (\mathbf {x}), \tag {2.5.39}$$

where, $\lambda'$ is the transpose of $\lambda$ . Then, the optimal values $x^{*}$ and $\lambda^{*}$ are the solutions of the following $n + m$ equations

$$\frac {\partial \mathcal {L}}{\partial \mathbf {x}} = \frac {\partial f}{\partial \mathbf {x}} + \lambda^ {\prime} \frac {\partial \mathbf {g}}{\partial \mathbf {x}} = 0 \tag {2.5.40}\frac {\partial \mathcal {L}}{\partial \boldsymbol {\lambda}} = \mathbf {g} (\mathbf {x}) = 0. \tag {2.5.41}$$

Features of Lagrange Multiplier: The Lagrange multiplier method is a powerful one in finding the extrema of functions subject to conditions. It has the following attractive features:

1. The importance of the Lagrange multiplier technique lies on the fact that the problem of determining the extrema of the function $f(\mathbf{x})$ subject to the conditions $\mathbf{g}(\mathbf{x}) = 0$ is embedded within the simple problem of determining the extrema of the simple augmented function $\mathcal{L}(\mathbf{x},\boldsymbol{\lambda}) = f(\mathbf{x}) + \boldsymbol{\lambda}'\mathbf{g}(\mathbf{x})$ .

2. Introduction of Lagrange multiplier allows us to treat all the variables x and $\lambda$ in the augmented function $\mathcal{L}(\mathbf{x},\boldsymbol{\lambda})$ as though each were independent.

3. The multiplier $\lambda$ acts like a catalyst in the sense that it is introduced to perform a certain duty as given by item 2.

4. The increased dimensionality $(n + m)$ which is characteristic of the Lagrange multiplier method, is generally more than compensated by the relative simplicity and systematic procedure of the technique.

The multiplier method was given by Lagrange in 1788.
