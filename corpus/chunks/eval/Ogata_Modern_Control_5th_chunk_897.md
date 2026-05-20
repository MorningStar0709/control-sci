$$
\mathbf {A} ^ {- 1} = \frac {\operatorname{adj} \mathbf {A}}{| \mathbf {A} |} = \left[ \begin{array}{c c c} \frac {3}{1 7} & \frac {6}{1 7} & - \frac {4}{1 7} \\ \frac {7}{1 7} & - \frac {3}{1 7} & \frac {2}{1 7} \\ \frac {1}{1 7} & \frac {2}{1 7} & - \frac {7}{1 7} \end{array} \right]
$$

In what follows, we give formulas for finding inverse matrices for the $2 \times 2$ matrix and the $3 \times 3$ matrix. For the $2 \times 2$ matrix

$$
\mathbf {A} = \left[ \begin{array}{l l} a & b \\ c & d \end{array} \right] \quad \text { where } a d - b c \neq 0
$$

the inverse matrix is given by

$$
\mathbf {A} ^ {- 1} = \frac {1}{a d - b c} \left[ \begin{array}{c c} d & - b \\ - c & a \end{array} \right]
$$

For the $3 \times 3$ matrix

$$
\mathbf {A} = \left[ \begin{array}{c c c} a & b & c \\ d & e & f \\ g & h & i \end{array} \right] \quad \text { where } | \mathbf {A} | \neq 0
$$

the inverse matrix is given by

$$
\mathbf {A} ^ {- 1} = \frac {1}{| \mathbf {A} |} \left[ \begin{array}{c c c c c} \left| \begin{array}{c c} e & f \\ h & i \end{array} \right| & - \left| \begin{array}{c c} b & c \\ h & i \end{array} \right| & \left| \begin{array}{c c} b & c \\ e & f \end{array} \right| \\ - \left| \begin{array}{c c} d & f \\ g & i \end{array} \right| & \left| \begin{array}{c c} a & c \\ g & i \end{array} \right| & - \left| \begin{array}{c c} a & c \\ d & f \end{array} \right| \\ \left| \begin{array}{c c} d & e \\ g & h \end{array} \right| & - \left| \begin{array}{c c} a & b \\ g & h \end{array} \right| & \left| \begin{array}{c c} a & b \\ d & e \end{array} \right| \end{array} \right]
$$

Note that

$$(\mathbf {A} ^ {- 1}) ^ {- 1} = \mathbf {A}(\mathbf {A} ^ {- 1}) ^ {\prime} = (\mathbf {A} ^ {\prime}) ^ {- 1}(\mathbf {A} ^ {- 1}) ^ {*} = (\mathbf {A} ^ {*}) ^ {- 1}$$

There are several more useful formulas available. Assume that $\mathbf { A } = n \times n$ matrix, $\mathbf { B } = n \times$ m matrix, $\mathbf { C } = m \times n$ matrix, and $\mathbf { D } = m \times m$ matrix. Then

$$[ \mathbf {A} + \mathbf {B C} ] ^ {- 1} = \mathbf {A} ^ {- 1} - \mathbf {A} ^ {- 1} \mathbf {B} [ \mathbf {I} _ {m} + \mathbf {C A} ^ {- 1} \mathbf {B} ] ^ {- 1} \mathbf {C A} ^ {- 1}$$

$\operatorname { I f } \left| \mathbf { A } \right| \neq 0 \operatorname { a n d } \left| \mathbf { D } \right| \neq 0 , \operatorname { t h e n }$
