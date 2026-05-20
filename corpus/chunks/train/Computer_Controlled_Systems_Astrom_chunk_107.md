# Example 2.6 First-order system with time delay

Consider the system

$$\frac {d x (t)}{d t} = \alpha x (t) + \beta u (t - \tau)$$

with $\alpha \neq 0$ . Assume that the system is sampled with period $h$ , where $0 \leq \tau \leq h$ . Equation (2.11) gives

$$
\begin{array}{l} \Phi = a = e ^ {\alpha h} \\ \Gamma_ {0} = b _ {0} = \int_ {0} ^ {h - \tau} e ^ {\alpha s} \beta d s = \frac {\beta}{\alpha} (e ^ {\alpha (h - \tau)} - 1) \\ \Gamma_ {1} = b _ {1} = e ^ {\alpha (h - \tau)} \int_ {0} ^ {\tau} e ^ {\alpha s} \beta d s = \frac {\beta}{\alpha} \left(e ^ {\alpha h} - e ^ {\alpha (h - \tau)}\right) \\ \end{array}
$$

The sampled system is thus

$$x (k h + h) = a x (k h) + b _ {0} u (k h) + b _ {1} u (k h - h)$$
