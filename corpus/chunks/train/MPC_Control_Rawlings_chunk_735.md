# Exercise 6.13: Padding matrices

Given a vector z and subvector u

$$
\mathbf {z} = \left[ \begin{array}{c} u (0) \\ x (1) \\ u (1) \\ x (2) \\ \vdots \\ u (N - 1) \\ x (N) \end{array} \right] \qquad \mathbf {u} = \left[ \begin{array}{c} u (0) \\ u (1) \\ \vdots \\ u (N - 1) \end{array} \right] \qquad x \in \mathbb {R} ^ {n} \qquad u \in \mathbb {R} ^ {m}
$$

and quadratic function of u

$$(1 / 2) \mathbf {u} ^ {\prime} H \mathbf {u} + h ^ {\prime} \mathbf {u}$$

Find the corresponding quadratic function of z so that

$$(1 / 2) \mathbf {z} ^ {\prime} H _ {z} \mathbf {z} + h _ {z} ^ {\prime} \mathbf {z} = (1 / 2) \mathbf {u} ^ {\prime} H \mathbf {u} + h ^ {\prime} \mathbf {u} \quad \forall \mathbf {z}, \mathbf {u}$$

Hint: first find the padding matrix E such that $\mathbf { u } = E \mathbf { z } .$ .
