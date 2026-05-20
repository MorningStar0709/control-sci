$$
\begin{array}{l} G (s) = \left[ \begin{array}{c c} 0. 8 & 1 \end{array} \right] \left[ \begin{array}{c c} s & - 1 \\ 0. 4 & s + 1. 3 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ = \frac {1}{s ^ {2} + 1 . 3 s + 0 . 4} \left[ \begin{array}{c c} 0. 8 & 1 \end{array} \right] \left[ \begin{array}{c c} s + 1. 3 & 1 \\ - 0. 4 & s \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ = \frac {s + 0 . 8}{(s + 0 . 8) (s + 0 . 5)} \\ \end{array}
$$

[Note that the same transfer function can be obtained by using Equations (9–122) and (9–123).] Clearly, cancellation occurs in this transfer function.

If a pole-zero cancellation occurs in the transfer function, then the controllability and observability vary, depending on how the state variables are chosen. Remember that, to be completely state controllable and observable, the transfer function must not have any pole-zero cancellations.

A–9–18. Prove that the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}\mathbf {y} = \mathbf {C x}$$

where x = state vector (n-vector)

$$\mathbf {y} = \text { output vector } (m \text {-vector}) \quad (m \leq n)\mathbf {A} = n \times n \text { matrix }\mathbf {C} = m \times n \text { matrix }$$

is completely observable if and only if the composite mn\*n matrix P, where

$$
\mathbf {P} = \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \cdot \\ \cdot \\ \cdot \\ \mathbf {C A} ^ {n - 1} \end{array} \right]
$$

is of rank n.

Solution. We shall first obtain the necessary condition. Suppose that

$$\operatorname{rank} \mathbf {P} < n$$

Then there exists x(0) such that

$$\mathbf {P x} (0) = \mathbf {0}$$

or

$$
\mathbf {P} \mathbf {x} (0) = \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ . \\ . \\ . \\ \mathbf {C A} ^ {n - 1} \end{array} \right] \mathbf {x} (0) = \left[ \begin{array}{c} \mathbf {C x} (0) \\ \mathbf {C A x} (0) \\ . \\ . \\ . \\ \mathbf {C A} ^ {n - 1} \mathbf {x} (0) \end{array} \right] = \mathbf {0}
$$

Hence, we obtain, for a certain x(0),

$$\mathbf {C A} ^ {i} \mathbf {x} (0) = \mathbf {0}, \quad \text { for } i = 0, 1, 2, \dots , n - 1$$

Notice that from Equation (9–48) or (9–50), we have

$$e ^ {\mathbf {A} t} = \alpha_ {0} (t) \mathbf {I} + \alpha_ {1} (t) \mathbf {A} + \alpha_ {2} (t) \mathbf {A} ^ {2} + \dots + \alpha_ {m - 1} (t) \mathbf {A} ^ {m - 1}$$

where $m ( m \leq n )$ is the degree of the minimal polynomial for A. Hence, for a certain x(0), we have
