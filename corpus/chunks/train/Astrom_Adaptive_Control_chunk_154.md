# EXAMPLE 3.1 Model-following with zero cancellation

Consider a continuous-time process described by the transfer function

$$G (s) = \frac {1}{s (s + 1)} \tag {3.16}$$

This can be regarded as a normalized model for a motor. The pulse transfer operator for the sampling period h = 0.5 s is

$$H (q) = \frac {B (q)}{A (q)} = \frac {b _ {0} q + b _ {1}}{q ^ {2} + a _ {1} q + a _ {2}} = \frac {0 . 1 0 6 5 q + 0 . 0 9 0 2}{q ^ {2} - 1 . 6 0 6 5 q + 0 . 6 0 6 5} \tag {3.17}$$

We have $\deg A = 2$ and $\deg B = 1$ . The design procedure thus gives a first-order controller, and the closed-loop system will be of third order. The sampled data system has a zero in -0.84 and poles in 1 and 0.61. Let the desired closed-loop system be

$$\frac {B _ {m} (q)}{A _ {m} (q)} = \frac {b _ {m 0} q}{q ^ {2} + a _ {m 1} q + a _ {m 2}} = \frac {0 . 1 7 6 1 q}{q ^ {2} - 1 . 3 2 0 5 q + 0 . 4 9 6 6} \tag {3.18}$$

This corresponds to a natural frequency of 1 rad/s and a relative damping of 0.7. Parameter $b_{m0}$ is chosen so that the static gain is unity. This model satisfies the compatibility conditions because it has the same pole excess as the process and the process zero is stable although poorly damped. To apply the design procedure in Algorithm 3.1, we first factor the polynomial B, and we obtain

$$
\begin{array}{l} B ^ {+} (q) = q + b _ {1} / b _ {0} \\ B ^ {-} (q) = b _ {0} \\ B _ {m} ^ {\prime} (q) = b _ {m 0} q / b _ {0} \\ \end{array}
$$

Since the process is of second order, the polynomials $R, S$ , and $T$ will all be of first order. Polynomial $R'$ is thus of degree zero. Since the polynomial is monic, we have $R' = 1$ . Since $\deg B^{+} = 1$ , it follows from the compatibility conditions that $\deg A_{\omega} = 0$ . Choose

$$A _ {o} (q) = 1$$

The Diophantine equation (3.11) then becomes

$$\left(q ^ {2} + a _ {1} q + a _ {2}\right) \cdot 1 + b _ {0} (s _ {0} q + s _ {1}) = q ^ {2} + a _ {m 1} q + a _ {m 2}$$

Equating coefficients of equal power of q gives

$$a _ {1} + b _ {0} s _ {0} = a _ {m 1}a _ {2} + b _ {0} s _ {1} = a _ {m 2}$$

These equations can be solved if $b_{0} \neq 0$ . The solution is

$$s _ {0} = \frac {a _ {m 1} \cdot a _ {1}}{b _ {0}}s _ {1} = \frac {a _ {m 2} - a _ {2}}{b _ {0}}$$

The controller is thus characterized by the polynomials

$$R (q) = B ^ {+} = q + \frac {b _ {1}}{b _ {0}}S (q) = s _ {0} q + s _ {1}T (q) = A _ {o} B _ {m} ^ {\prime} = \frac {b _ {m 0} q}{b _ {0}}$$

The process in Example 3.1 has a zero that is stable but poorly damped. The continuous-time equivalent corresponds to a zero with relative damping $\zeta = 0.06$ . We will therefore also determine a controller that does not cancel the zero. This is done in the next example.
