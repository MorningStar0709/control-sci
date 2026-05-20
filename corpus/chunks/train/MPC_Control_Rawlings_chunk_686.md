$$
\begin{array}{l} \tilde {\mathbf {u}} _ {1} ^ {+} = \left\{u _ {1} (1), u _ {1} (2), \dots , u _ {1} (N - 1), 0 \right\} \\ \tilde {\mathbf {u}} _ {2} ^ {+} = \left\{u _ {2} (1), u _ {2} (2), \dots , u _ {2} (N - 1), 0 \right\} \\ \end{array}
$$

We define the following linear time-invariant functions $g _ { 1 } ^ { p }$ and $g _ { 2 } ^ { p }$ as the outcome of applying the control iteration procedure $p$ times

$$
\begin{array}{l} \mathbf {u} _ {1} ^ {p} = g _ {1} ^ {p} (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ \mathbf {u} _ {2} ^ {p} = g _ {2} ^ {p} \left(x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) \\ \end{array}
$$

in which $p \geq 0$ is an integer, $x _ { 1 }$ and $x _ { 2 }$ are the states, and $\mathbf { u } _ { 1 } , \mathbf { u } _ { 2 }$ are the input sequences from the previous sample, used to generate the warm start for the iteration. Here we consider p to be constant with time, but Exercise 6.20 considers the case in which the controller iterations may vary with sample time. The system evolution is then given by

$$
\begin{array}{l} x _ {1} ^ {+} = A _ {1} x _ {1} + \overline {{B}} _ {1 1} u _ {1} + \overline {{B}} _ {1 2} u _ {2} \quad x _ {2} ^ {+} = A _ {2} x _ {2} + \overline {{B}} _ {2 1} u _ {1} + \overline {{B}} _ {2 2} u _ {2} \\ \mathbf {u} _ {1} ^ {+} = g _ {1} ^ {p} (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \quad \mathbf {u} _ {2} ^ {+} = g _ {2} ^ {p} (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \tag {6.16} \\ \end{array}
$$

By the construction of the warm start, $\widetilde { \mathbf { u } } _ { 1 } ^ { + } , \widetilde { \mathbf { u } } _ { 2 } ^ { + }$ , we have

$$
\begin{array}{l} V \left(x _ {1} ^ {+}, x _ {2} ^ {+}, \tilde {\mathbf {u}} _ {1} ^ {+}, \tilde {\mathbf {u}} _ {2} ^ {+}\right) = V \left(x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) - \rho_ {1} \ell_ {1} \left(x _ {1}, u _ {1}\right) - \rho_ {2} \ell_ {2} \left(x _ {2}, u _ {2}\right) \\ + (1 / 2) \rho_ {1} x _ {1} (N) ^ {\prime} \left[ A _ {1} ^ {\prime} P _ {1 f} A _ {1} - P _ {1 f} + Q _ {1} \right] x _ {1} (N) \\ + (1 / 2) \rho_ {2} x _ {2} (N) ^ {\prime} \left[ A _ {2} ^ {\prime} P _ {2 f} A _ {2} - P _ {2 f} + Q _ {2} \right] x _ {2} (N) \\ \end{array}
$$

From our choice of terminal penalty satisfying (6.8), the last two terms are zero giving

$$
\begin{array}{l} V (x _ {1} ^ {+}, x _ {2} ^ {+}, \tilde {\mathbf {u}} _ {1} ^ {+}, \tilde {\mathbf {u}} _ {2} ^ {+}) = V (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ - \rho_ {1} \ell_ {1} (x _ {1}, u _ {1}) - \rho_ {2} \ell_ {2} (x _ {2}, u _ {2}) \tag {6.17} \\ \end{array}
$$
