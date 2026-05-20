$$
\mathbf {M} ^ {- 1} \mathbf {A M} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - a _ {n} \\ 1 & 0 & \dots & 0 & - a _ {n - 1} \\ 0 & 1 & \dots & 0 & - a _ {n - 2} \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ 0 & 0 & \dots & 1 & - a _ {1} \end{array} \right]
$$

where $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ are the coefficients of the characteristic polynomial

$$\left| s \mathbf {I} - \mathbf {A} \right| = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

Solution. Let us consider the case where n=3. We shall show that

$$
\mathbf {A M} = \mathbf {M} \left[ \begin{array}{l l l} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \tag {10-140}
$$

The left-hand side of Equation (10–140) is

$$\mathbf {A} \mathbf {M} = \mathbf {A} [ \mathbf {B} \mid \mathbf {A B} \mid \mathbf {A} ^ {2} \mathbf {B} ] = [ \mathbf {A B} \mid \mathbf {A} ^ {2} \mathbf {B} \mid \mathbf {A} ^ {3} \mathbf {B} ]$$

The right-hand side of Equation (10–140) is

$$
\left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} \end{array} \right] \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] = \left[ \begin{array}{c c c} \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} & - a _ {3} \mathbf {B} - a _ {2} \mathbf {A B} - a _ {1} \mathbf {A} ^ {2} \mathbf {B} \end{array} \right] \tag {10-141}
$$

The Cayley–Hamilton theorem states that matrix A satisfies its own characteristic equation or, in the case of n=3,

$$\mathbf {A} ^ {3} + a _ {1} \mathbf {A} ^ {2} + a _ {2} \mathbf {A} + a _ {3} \mathbf {I} = \mathbf {0} \tag {10-142}$$

Using Equation (10–142), the third column of the right-hand side of Equation (10–141) becomes

$$- a _ {3} \mathbf {B} - a _ {2} \mathbf {A B} - a _ {1} \mathbf {A} ^ {2} \mathbf {B} = (- a _ {3} \mathbf {I} - a _ {2} \mathbf {A} - a _ {1} \mathbf {A} ^ {2}) \mathbf {B} = \mathbf {A} ^ {3} \mathbf {B}$$

Thus, Equation (10–141) becomes

$$
\left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A ^ {2} B} \end{array} \right] \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] = \left[ \begin{array}{c c c} \mathbf {A B} & \mathbf {A ^ {2} B} & \mathbf {A ^ {3} B} \end{array} \right]
$$

Hence, the left-hand side and the right-hand side of Equation (10–140) are the same. We have thus shown that Equation (10–140) is true. Consequently,
