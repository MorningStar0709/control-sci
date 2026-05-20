Complete Observability of Continuous-Time Systems. Consider the system described by Equations (9–63) and (9–64). The output vector y(t) is

$$\mathbf {y} (t) = \mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} (0)$$

Referring to Equation (9–48) or (9–50), we have

$$e ^ {\mathbf {A} t} = \sum_ {k = 0} ^ {n - 1} \alpha_ {k} (t) \mathbf {A} ^ {k}$$

where n is the degree of the characteristic polynomial. [Note that Equations (9–48) and (9–50) with m replaced by n can be derived using the characteristic polynomial.]

Hence, we obtain

$$\mathbf {y} (t) = \sum_ {k = 0} ^ {n - 1} \alpha_ {k} (t) \mathbf {C A} ^ {k} \mathbf {x} (0)$$

or

$$\mathbf {y} (t) = \alpha_ {0} (t) \mathbf {C x} (0) + \alpha_ {1} (t) \mathbf {C A x} (0) + \dots + \alpha_ {n - 1} (t) \mathbf {C A} ^ {n - 1} \mathbf {x} (0) \tag {9-65}$$

If the system is completely observable, then, given the output y(t) over a time interval $0 \le t \le t _ { 1 } , { \bf x } ( 0 )$ is uniquely determined from Equation (9–65). It can be shown that this requires the rank of the nm\*n matrix

$$
\left[ \begin{array}{c} \mathbf {C} \\ \hline \mathbf {C A} \\ \hline \cdot \\ \cdot \\ \cdot \\ \mathbf {C A} ^ {n - 1} \end{array} \right]
$$

to be n. (See Problem A–9–19 for the derivation of this condition.)

From this analysis, we can state the condition for complete observability as follows: The system described by Equations (9–63) and (9–64) is completely observable if and only if the n\*nm matrix

$$
\left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right]
$$

is of rank n or has n linearly independent column vectors. This matrix is called the observability matrix.

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ - 2 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

Is this system controllable and observable?

Since the rank of the matrix

$$
\left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 1 & - 1 \end{array} \right]
$$

is 2, the system is completely state controllable.

For output controllability, let us find the rank of the matrix $[ \mathbf { C B } \vdots \mathbf { C A B } ] .$ Since.
