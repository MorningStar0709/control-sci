$$
\mathbf {u} = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \\ \vdots \\ u _ {r} \end{array} \right] \qquad \qquad \mathbf {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {m} \end{array} \right]
$$

Therefore, all three vectors x, u, and y are column vectors. We note that the first time derivative of the state vector is still an n × 1 vector:

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \vdots \\ \dot {x} _ {n} \end{array} \right]
$$

We can assemble the a, b, c, and d coefficients of the state and output equations into four matrices:

$$
\mathbf {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & \ddots & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right]

\mathbf {B} = \left[ \begin{array}{c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 r} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 r} \\ \vdots & \vdots & \ddots & \vdots \\ b _ {n 1} & b _ {n 2} & \dots & b _ {n r} \end{array} \right]

\mathbf {C} = \left[ \begin{array}{c c c c} c _ {1 1} & c _ {1 2} & \dots & c _ {1 n} \\ c _ {2 1} & c _ {2 2} & \dots & c _ {2 n} \\ \vdots & \vdots & \ddots & \vdots \\ c _ {m 1} & c _ {m 2} & \dots & c _ {m n} \end{array} \right]

\mathbf {D} = \left[ \begin{array}{c c c c} d _ {1 1} & d _ {1 2} & \dots & d _ {1 r} \\ d _ {2 1} & d _ {2 2} & \dots & d _ {2 r} \\ \vdots & \vdots & \ddots & \vdots \\ d _ {m 1} & d _ {m 2} & \dots & d _ {m r} \end{array} \right]
$$

The n × n (square) matrix A is the state or system matrix; the n × r matrix B is the input matrix; the m × n matrix C is the output matrix; and the m × r matrix D is the direct-link matrix. Finally, we can use these matrix and vector definitions to present a compact matrix-vector representation of the state and output equations

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \tag {5.21}\mathbf {y} = \mathbf {C x} + \mathbf {D u} \tag {5.22}$$

Equation (5.21) is the state equation, and Eq. (5.22) is the output equation, and together they constitute a complete SSR. The reader should note that the state equation (5.21) represents the system dynamics; that is, the linear coefficients from the differential equations that comprise the mathematical model are contained in matrices A and B. The output equation (5.22) is an algebraic linear mapping between the state and input variables and the outputs or measurements.
