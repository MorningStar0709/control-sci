# Example 2.1 First-order system

Consider the system

$$\frac {d x}{d t} = \alpha x + \beta u$$

with $\alpha \neq 0$ . Applying Eqs. (2.5) we get

$$
\begin{array}{l} \Phi = e ^ {\alpha h} \\ \Gamma = \int_ {0} ^ {h} e ^ {\alpha s} d s \beta = \frac {\beta}{\alpha} (e ^ {\alpha h} - 1) \\ \end{array}
$$

The sampled system thus becomes

$$x (k h + h) = e ^ {\alpha h} x (k h) + \frac {\beta}{\alpha} (e ^ {\alpha h} - 1) u (k h)$$
