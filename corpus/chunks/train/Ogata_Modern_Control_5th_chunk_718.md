$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \tag {9-114}\mathbf {y} = \mathbf {C x} \tag {9-115}$$

where x = state vector (n-vector)

u = control vector (r-vector)

y = output vector (m-vector) (m - n)

A = n \* n matrix

B = n \* r matrix

C = m \* n matrix

is completely output controllable if and only if the composite $m \times n r$ matrix P, where

$$
\mathbf {P} = \left[ \begin{array}{c c c c c} \mathbf {C B} & \mathbf {C A B} & \mathbf {C A ^ {2} B} & \dots & \mathbf {C A ^ {n - 1} B} \end{array} \right]
$$

is of rank m. (Notice that complete state controllability is neither necessary nor sufficient for complete output controllability.)

Solution. Suppose that the system is output controllable and the output $\mathbf { y } ( t )$ starting from any $\mathbf { y } ( 0 )$ , the initial output, can be transferred to the origin of the output space in a finite time interval $0 \leq t \leq T$ . That is,

$$\mathbf {y} (T) = \mathbf {C x} (T) = \mathbf {0} \tag {9-116}$$

Since the solution of Equation (9–114) is

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \left[ \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {- \mathbf {A} \tau} \mathbf {B u} (\tau) d \tau \right]$$

at $t = T$ , we have

$$\mathbf {x} (T) = e ^ {\mathbf {A} T} \left[ \mathbf {x} (0) + \int_ {0} ^ {T} e ^ {- \mathbf {A} \tau} \mathbf {B u} (\tau) d \tau \right] \tag {9-117}$$

Substituting Equation (9–117) into Equation (9–116), we obtain

$$
\begin{array}{l} \mathbf {y} (T) = \mathbf {C x} (T) \\ = \mathbf {C} e ^ {\mathbf {A} T} \left[ \mathbf {x} (0) + \int_ {0} ^ {T} e ^ {- \mathbf {A} \tau} \mathbf {B u} (\tau) d \tau \right] = \mathbf {0} \tag {9-118} \\ \end{array}
$$

On the other hand, $\mathbf { y } ( 0 ) = \mathbf { C } \mathbf { x } ( 0 )$ . Notice that the complete output controllability means that the vector $\mathbf { C x } ( 0 )$ spans the m-dimensional output space. Since $e ^ { \mathbf { A } T }$ is nonsingular, if $\mathbf { C x } ( 0 )$ spans the m-dimensional output space, so does $\mathbf { C } e ^ { \mathbf { A } T } \mathbf { \bar { x } } ( 0 )$ , and vice versa. From Equation (9–118) we obtain

$$
\begin{array}{l} \mathbf {C} e ^ {\mathbf {A} T} \mathbf {x} (0) = - \mathbf {C} e ^ {\mathbf {A} T} \int_ {0} ^ {T} e ^ {- \mathbf {A} \tau} \mathbf {B u} (\tau) d \tau \\ = - \mathbf {C} \int_ {0} ^ {T} e ^ {\mathbf {A} \tau} \mathbf {B u} (T - \tau) d \tau \\ \end{array}
$$
