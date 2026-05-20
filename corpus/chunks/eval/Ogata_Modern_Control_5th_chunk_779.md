To present the basic idea of the minimum-order observer, without undue mathematical complications, we shall present the case where the output is a scalar (that is, m=1) and derive the state equation for the minimum-order observer. Consider the system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-79}y = \mathbf {C x} \tag {10-80}$$

where the state vector x can be partitioned into two parts $x _ { a }$ (a scalar) and $\mathbf { x } _ { b }$ C an $\left( n - 1 \right) \mathbf { - v e c t o r } \mathbf { ] }$ . Here the state variable $x _ { a }$ is equal to the output y and thus can be directly measured, and $\mathbf { x } _ { b }$ is the unmeasurable portion of the state vector. Then the partitioned state and output equations become

$$
\left[ \begin{array}{c} \dot {x} _ {a} \\ \hline \dot {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c c} A _ {a a} & \mathbf {A} _ {a b} \\ \hline \mathbf {A} _ {b a} & \mathbf {A} _ {b b} \end{array} \right] \left[ \begin{array}{c} x _ {a} \\ \hline \mathbf {x} _ {b} \end{array} \right] + \left[ \begin{array}{c} B _ {a} \\ \hline \mathbf {B} _ {b} \end{array} \right] u \tag {10-81}

y = \left[ \begin{array}{l l} 1 & \mathbf {0} \end{array} \right] \left[ \begin{array}{c} x _ {a} \\ \dots \\ \mathbf {x} _ {b} \end{array} \right] \tag {10-82}
$$

where $A _ { a a }$ = scalar

$$\mathbf {A} _ {a b} = 1 \times (n - 1) \text { matrix }\mathbf {A} _ {b a} = (n - 1) \times 1 \text { matrix }\mathbf {A} _ {b b} = (n - 1) \times (n - 1) \text { matrix }B _ {a} = \text { scalar }\mathbf {B} _ {b} = (n - 1) \times 1 \text { matrix }$$

From Equation (10–81), the equation for the measured portion of the state becomes

$$\dot {x} _ {a} = A _ {a a} x _ {a} + \mathbf {A} _ {a b} \mathbf {x} _ {b} + B _ {a} u$$

or

$$\dot {x} _ {a} - A _ {a a} x _ {a} - B _ {a} u = \mathbf {A} _ {a b} \mathbf {x} _ {b} \tag {10-83}$$

The terms on the left-hand side of Equation (10–83) can be measured. Equation (10–83) acts as the output equation. In designing the minimum-order observer, we consider the left-hand side of Equation (10–83) to be known quantities.Thus, Equation (10–83) relates the measurable quantities and unmeasurable quantities of the state.

From Equation (10–81), the equation for the unmeasured portion of the state becomes

$$\dot {\mathbf {x}} _ {b} = \mathbf {A} _ {b a} x _ {a} + \mathbf {A} _ {b b} \mathbf {x} _ {b} + \mathbf {B} _ {b} u \tag {10-84}$$
