# Controller Design

The controller design is now straightforward. The Diophantine equation (5.4) becomes

$$(z - 1) ^ {2} R (z) + \frac {h ^ {2}}{2} (z + 1) S (z) = A _ {o} (z) A _ {c} (z) = A _ {c l} (z)$$

where it is required that R have a zero at z = 1. The minimum-degree solution with no controller delay is such that both R and S are second-order polynomials, that is,

$$
\begin{array}{l} S (z) = s _ {0} z ^ {2} + s _ {1} z + s _ {2} \\ R (z) = z ^ {2} + r _ {1} z + r _ {2} = (z + r) (z - 1) \\ \end{array}
$$

Straightforward calculations give

$$
\begin{array}{l} s _ {0} = \frac {A _ {c l} (1) - 2 A _ {c l} ^ {\prime} (1) + 2 A _ {c l} ^ {\prime \prime} (1)}{4 h ^ {2}} \\ s _ {1} = \frac {- A _ {c l} (1) + 2 A _ {c l} ^ {\prime} (1) - A _ {c l} ^ {\prime \prime} (1)}{h ^ {2}} \\ s _ {2} = \frac {7 A _ {c l} (1) - 6 A _ {c l} ^ {\prime} (1) + 2 A _ {c l} ^ {\prime \prime} (1)}{4 h ^ {2}} \\ r _ {1} = \frac {A _ {c l} (- 1)}{8} \\ r _ {2} = 1 - \frac {A _ {c l} (- 1)}{8} \\ \end{array}
$$

where $A_{cl}^{\prime}(z)$ and $A_{cl}^{\prime\prime}(z)$ are the first and second derivative of $A_{cl}$ with respect to z. The polynomial T is given by

$$T (z) = \frac {A _ {c} (1) A _ {o} (z)}{B (1)} = \frac {(1 + a _ {c 1} + a _ {c 2}) A _ {o} (z)}{h ^ {2}}$$
