# EXAMPLE PROBLEMS AND SOLUTIONS

A–10–1. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

Suppose that this system is not completely state controllable. Then the rank of the controllability matrix is less than n, or

$$
\operatorname{rank} \left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] = q <   n \tag {10-136}
$$

This means that there are q linearly independent column vectors in the controllability matrix. Let us define such q linearly independent column vectors as $\mathbf { f } _ { 1 } , \mathbf { f } _ { 2 } , \ldots , \mathbf { f } _ { q }$ . Also, let us choose $n \mathrm { ~ - ~ } q$ additional n-vectors $\mathbf { v } _ { q { \mathrm { ~ + ~ } } 1 } , \mathbf { v } _ { q { \mathrm { ~ + ~ } } 2 } , \ldots , \mathbf { v } _ { n }$ such that

$$
\mathbf {P} = \left[ \begin{array}{c c c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \mathbf {v} _ {q + 2} & \dots & \mathbf {v} _ {n} \end{array} \right]
$$

is of rank n. By using matrix P as the transformation matrix, define

$$\mathbf {P} ^ {- 1} \mathbf {A} \mathbf {P} = \hat {\mathbf {A}}, \quad \mathbf {P} ^ {- 1} \mathbf {B} = \hat {\mathbf {B}}$$

Show that $\hat { \bf A }$ can be given by

$$
\hat {\mathbf {A}} = \left[ \begin{array}{c c} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \hline \mathbf {0} & \mathbf {A} _ {2 2} \end{array} \right]
$$

where ${ \bf A } _ { 1 1 }$ 1 is a $q \times q$ matrix, ${ \bf A } _ { 1 2 }$ is a $q \times ( n - q )$ matrix, ${ \bf A } _ { 2 2 }$ is an $( n - q ) \times ( n - q )$ matrix, and 0 is an $( n - q ) \times q$ matrix. Show also that matrix can be given byBˆ

$$
\hat {\mathbf {B}} = \left[ \begin{array}{c} \mathbf {B} _ {1 1} \\ \hdashline \mathbf {0} \end{array} \right]
$$

where $\mathbf { B } _ { 1 1 }$ is ${ \mathrm { a ~ } } q \times 1$ matrix and 0 is an $( n - q ) \times 1$ matrix.

Solution. Notice that

$$\mathbf {A} \mathbf {P} = \mathbf {P} \hat {\mathbf {A}}$$

or

$$
\begin{array}{l} \left[ \begin{array}{c c c c c c c c} \mathbf {A f} _ {1} & \mathbf {A f} _ {2} & \dots & \mathbf {A f} _ {q} & \mathbf {A v} _ {q + 1} & \dots & \mathbf {A v} _ {n} \end{array} \right] \\ = \left[ \begin{array}{c c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \dots & \mathbf {v} _ {n} \end{array} \right] \hat {\mathbf {A}} \tag {10-137} \\ \end{array}
$$

Also,

$$\mathbf {B} = \mathbf {P} \hat {\mathbf {B}} \tag {10-138}$$
