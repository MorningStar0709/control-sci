# 6.1.1 Least Squares Solution

In comparing various forms of linear distributed MPC it proves convenient to see the MPC quadratic program for the sequence of states and inputs as a single large linear algebra problem. To develop this linear algebra problem, we consider first the unconstrained LQ problem of Chapter 1, which we solved efficiently with dynamic programming (DP) in Section 1.3.3

$$V (x (0), \mathbf {u}) = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k)\right) + (1 / 2) x (N) ^ {\prime} P _ {f} x (N)$$

subject to

$$x ^ {+} = A x + B u$$

In this section, we first take the direct but brute-force approach to finding the optimal control law. We write the model solution as

$$
\left[ \begin{array}{c} x (1) \\ x (2) \\ \vdots \\ x (N) \end{array} \right] = \underbrace {\left[ \begin{array}{c} A \\ A ^ {2} \\ \vdots \\ A ^ {N} \end{array} \right]} _ {\mathcal {A}} x (0) + \underbrace {\left[ \begin{array}{c c c c} B & 0 & \cdots & 0 \\ A B & B & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ A ^ {N - 1} B & A ^ {N - 2} B & \cdots & B \end{array} \right]} _ {\mathcal {B}} \left[ \begin{array}{c} u (0) \\ u (1) \\ \vdots \\ u (N - 1) \end{array} \right] \tag {6.1}
$$

or using the input and state sequences

$$\mathbf {x} = \mathcal {A} x (0) + \mathcal {B} \mathbf {u}$$

The objective function can be expressed as

$$V (x (0), \mathbf {u}) = (1 / 2) \left(x ^ {\prime} (0) Q x (0) + \mathbf {x} ^ {\prime} Q \mathbf {x} + \mathbf {u} ^ {\prime} R \mathbf {u}\right)$$

in which

$$
\mathcal {Q} = \operatorname{diag} \left(\left[ \begin{array}{c c c c} Q & Q & \dots & P _ {f} \end{array} \right]\right) \in \mathbb {R} ^ {N n \times N n}

\mathcal {R} = \operatorname{diag} \left(\left[ \begin{array}{c c c c} R & R & \dots & R \end{array} \right]\right) \quad \in \mathbb {R} ^ {N m \times N m} \tag {6.2}
$$

Eliminating the state sequence. Substituting the model into the objective function and eliminating the state sequence gives a quadratic function of u

$$V (x (0), \mathbf {u}) = (1 / 2) x ^ {\prime} (0) \left(Q + \mathcal {A} ^ {\prime} \mathcal {Q} \mathcal {A}\right) x (0) + \mathbf {u} ^ {\prime} \left(\mathcal {B} ^ {\prime} \mathcal {Q} \mathcal {A}\right) x (0) +(1 / 2) \mathbf {u} ^ {\prime} (\mathcal {B} ^ {\prime} \mathcal {Q} \mathcal {B} + \mathcal {R}) \mathbf {u} \tag {6.3}$$

and the optimal solution for the entire set of inputs is obtained in one shot
