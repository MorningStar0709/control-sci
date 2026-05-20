$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B} u (\tau) d \tau$$

Applying the definition of complete state controllability just given, we have

$$\mathbf {x} \left(t _ {1}\right) = \mathbf {0} = e ^ {\mathbf {A} t _ {1}} \mathbf {x} (0) + \int_ {0} ^ {t _ {1}} e ^ {\mathbf {A} \left(t _ {1} - \tau\right)} \mathbf {B} u (\tau) d \tau$$

or

$$\mathbf {x} (0) = - \int_ {0} ^ {t _ {1}} e ^ {- \mathbf {A} \tau} \mathbf {B} u (\tau) d \tau \tag {9-52}$$

Referring to Equation (9–48) or (9–50), $e ^ { - \mathbf { A } \tau }$ can be written

$$e ^ {- \mathbf {A} \tau} = \sum_ {k = 0} ^ {n - 1} \alpha_ {k} (\tau) \mathbf {A} ^ {k} \tag {9-53}$$

Substituting Equation (9–53) into Equation (9–52) gives

$$\mathbf {x} (0) = - \sum_ {k = 0} ^ {n - 1} \mathbf {A} ^ {k} \mathbf {B} \int_ {0} ^ {t _ {1}} \alpha_ {k} (\tau) u (\tau) d \tau \tag {9-54}$$

Let us put

$$\int_ {0} ^ {t _ {1}} \alpha_ {k} (\tau) u (\tau) d \tau = \beta_ {k}$$

Then Equation (9–54) becomes

$$
\mathbf {x} (0) = - \sum_ {k = 0} ^ {n - 1} \mathbf {A} ^ {k} \mathbf {B} \beta_ {k}
= - \left[ \begin{array}{c c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] \left[ \begin{array}{c} \beta_ {0} \\ \hline \beta_ {1} \\ \hline \cdot \\ \cdot \\ \cdot \\ \hline \beta_ {n - 1} \end{array} \right] \tag {9-55}
$$

If the system is completely state controllable, then, given any initial state x(0), Equation (9–55) must be satisfied. This requires that the rank of the n\*n matrix

$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

be n.

From this analysis, we can state the condition for complete state controllability as follows: The system given by Equation (9–51) is completely state controllable if and only if the vectors $\mathbf { B } , \bar { \mathbf { A } } \mathbf { B } , \dots , \mathbf { \bar { A } } ^ { n - 1 } \mathbf { B }$ are linearly independent, or the n\*n matrix

$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

is of rank n.

The result just obtained can be extended to the case where the control vector u is r-dimensional. If the system is described by

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}$$

where u is an r-vector, then it can be proved that the condition for complete state controllability is that the n\*nr matrix
