# 11.3.1 Discrete and Continuous Comparison Table

In the following table, we list the analogous concepts between discrete time and continuous time.

<table><tr><td>Sampled World</td><td>Continuous World</td></tr><tr><td> $x(n) \quad n = 0,1,2\ldots$ </td><td> $x(t)$ </td></tr><tr><td>Digital Filter</td><td>Differential Equation</td></tr><tr><td> $x(n) = 4.2x(n-1) - 2.7x(n-2)$ </td><td> $\ddot{x}(t) = 6.7\dot{x} - 3.2x + 10$ </td></tr><tr><td>Digital Convolution:</td><td>Continuous Convolution:</td></tr><tr><td> $f(n) = \sum_{k=-\infty}^{k=\infty} h(k)x(k-n)$ </td><td> $f(t) = \int_{\tau=-\infty}^{\tau=\infty} h(\tau)x(t-\tau)d\tau$ </td></tr><tr><td>Z-Transform</td><td>Laplace Transform</td></tr><tr><td>Discrete Transfer Function</td><td>Continuous Transfer function</td></tr><tr><td> $G(z) = \frac{Y(z)}{X(z)}$ </td><td> $G(s) = \frac{Y(s)}{X(s)}$ </td></tr><tr><td>Stability: Outside Unit Circle</td><td>Stability: Left Half Plane</td></tr></table>
