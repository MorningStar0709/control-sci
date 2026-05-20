# Example 6.2

Consider a simple scalar example to illustrate the procedure underlying the dynamic programming method [79, 89].

$$x (k + 1) = x (k) + u (k) \tag {6.3.5}$$

and the performance criterion to be optimized as

$$J = \frac {1}{2} x ^ {2} (k _ {f}) + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} [ x ^ {2} (k) + u ^ {2} (k) ] \tag {6.3.6}$$

where, for simplicity of calculations, we take $k_{f} = 2$ . Let the constraints and the quantization values on the control be

$$- 1. 0 \leq u (k) \leq + 1. 0, \quad k = 0, 1, 2 \quad \text { or }u (k) = - 1. 0, \quad - 0. 5, \quad 0, \quad + 0. 5, \quad + 1. 0 \tag {6.3.7}$$

and on the state be

$$0 \leq x (k) \leq + 2. 0, \quad k = 0, 1 \quad \text { or }x (k) = 0, \quad 0. 5, \quad 1. 0 \quad 1. 5 \quad 2. 0. \tag {6.3.8}$$

Find the optimal control sequence $u^{*}(k)$ and the state $x^{*}(k)$ which minimize the performance criterion (6.3.6).

Solution: To use the principle of optimality, to solve the previous system, we first set up a grid between $x(k)$ and k, omitting all the arrows, arrow heads, etc. We divide the stages into two sets: one for k = 2 and the other for k = 1, 0. We start with k = 2 and first find the optimal values and work backward for k = 1, 0 using the state (6.3.5), the cost function (6.3.6) and the optimal control (6.3.7).

Stage: $k = 2$

First calculate the state $x(2)$ using the state relation (6.3.5) for all admissible values of $x(k)$ and $u(k)$ given by (6.3.7) and (6.3.8). Thus, for example, for the admissible value of $x(1)=2.0$ and $u(1)=-1,-0.5,0,0.5,1$ , we have

$$x (2) = x (1) + u (1)x (2) = 2. 0 + (- 1) = 1. 0x (2) = 2. 0 + (- 0. 5) = 1. 5x (2) = 2. 0 + 0 = 2. 0x (2) = 2. 0 + 0. 5 = 2. 5 \ggx (2) = 1. 5 + 1 = 3. \theta \rangle . \tag {6.3.9}$$

Note the values 2.5 and 3.0 (shown by a striking arrow) of state $x(2)$ are not allowed due to exceeding the state constraint (6.3.8).

Also, corresponding to the functional equation (6.3.4), we have for this example,

$$J _ {k} (x (k)) = \min _ {u (k)} \left[ \frac {1}{2} u ^ {2} (k) + x ^ {2} (k) + J _ {k + 1} ^ {*} \right] \tag {6.3.10}$$

from which we have for the optimal cost at $k = 2$

$$J _ {k _ {f}} ^ {*} = \frac {1}{2} x ^ {2} (2) \tag {6.3.11}$$

which is evaluated for all admissible values of $x(2)$ as

$$
\begin{array}{l} J _ {k _ {f}} ^ {*} = 2. 0 0 0 \quad \text { for } \quad x (2) = 2. 0 \\ = 1. 1 2 5 \quad \text { for } \quad x (2) = 1. 5 \\ = 0. 5 0 0 \quad \text {for} \quad x (2) = 1. 0 \\ = 0. 1 2 5 \quad \text {for} \quad x (2) = 0. 5 \\ = 0. 0 0 0 \quad \text { for } \quad x (2) = 0. \tag {6.3.12} \\ \end{array}
$$
