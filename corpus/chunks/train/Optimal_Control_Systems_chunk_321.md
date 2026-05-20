# 6.2 Pontryagin Minimum Principle

In Chapter 2, for finding the optimal control $\mathbf{u}^{*}(t)$ for the problem described by the plant (6.1.1), performance index (6.1.2), and boundary conditions (6.1.3), we used arbitrary variations in control $\mathbf{u}(t) = \mathbf{u}^{*}(t) + \delta \mathbf{u}(t)$ to define the increment $\Delta J$ and the (first) variation $\delta J$ in $J$ as

$$
\begin{array}{l} \Delta J \left(\mathbf {u} ^ {*} (t), \delta \mathbf {u} (t)\right) = J (\mathbf {u} (t)) - J \left(\mathbf {u} ^ {*} (t)\right) \geq 0 \quad \text {for minimum} \\ = \delta J (\mathbf {u} ^ {*} (t), \delta \mathbf {u} (t)) + \text { higher - order   terms } \tag {6.2.1} \\ \end{array}
$$

where, the first variation

$$\delta J = \frac {\partial J}{\partial \mathbf {u}} \delta \mathbf {u} (t). \tag {6.2.2}$$

Also, in Chapter 2, in order to obtain optimal control of unconstrained systems, we applied the fundamental theorem of calculus of variations
