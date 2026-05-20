$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 6 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right]
$$

The eigenvalues of matrix A are

$$\lambda_ {1} = - 1, \quad \lambda_ {2} = - 2, \quad \lambda_ {3} = - 3$$

Thus, three eigenvalues are distinct. If we define a set of new state variables $z _ { 1 } , z _ { 2 } ,$ , and $z _ { 3 }$ by the transformation

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] = \left[ \begin{array}{r r r} 1 & 1 & 1 \\ - 1 & - 2 & - 3 \\ 1 & 4 & 9 \end{array} \right] \left[ \begin{array}{c} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right]
$$

or

$$\mathbf {x} = \mathbf {P z} \tag {9-17}$$

where

$$
\mathbf {P} = \left[ \begin{array}{l l l} 1 & 1 & 1 \\ \lambda_ {1} & \lambda_ {2} & \lambda_ {3} \\ \lambda_ {1} ^ {2} & \lambda_ {2} ^ {2} & \lambda_ {3} ^ {2} \end{array} \right] = \left[ \begin{array}{r r r} 1 & 1 & 1 \\ - 1 & - 2 & - 3 \\ 1 & 4 & 9 \end{array} \right] \tag {9-18}
$$

then, by substituting Equation (9–17) into Equation (9–15), we obtain

$$\mathbf {P} \dot {\mathbf {z}} = \mathbf {A P z} + \mathbf {B u}$$

By premultiplying both sides of this last equation by $\mathbf { P } ^ { - 1 } .$ , we get

$$\dot {\mathbf {z}} = \mathbf {P} ^ {- 1} \mathbf {A} \mathbf {P} \mathbf {z} + \mathbf {P} ^ {- 1} \mathbf {B} u \tag {9-19}$$

or

$$
\left[ \begin{array}{c} \dot {z} _ {1} \\ \dot {z} _ {2} \\ \dot {z} _ {3} \end{array} \right] = \left[ \begin{array}{r r r} 3 & 2. 5 & 0. 5 \\ - 3 & - 4 & - 1 \\ 1 & 1. 5 & 0. 5 \end{array} \right] \left[ \begin{array}{r r r} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right] \left[ \begin{array}{r r r} 1 & 1 & 1 \\ - 1 & - 2 & - 3 \\ 1 & 4 & 9 \end{array} \right] \left[ \begin{array}{c} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right]

+ \left[ \begin{array}{r r r} 3 & 2. 5 & 0. 5 \\ - 3 & - 4 & - 1 \\ 1 & 1. 5 & 0. 5 \end{array} \right] \left[ \begin{array}{c} 0 \\ 0 \\ 6 \end{array} \right] u
$$

Simplifying gives

$$
\left[ \begin{array}{c} \dot {z} _ {1} \\ \dot {z} _ {2} \\ \dot {z} _ {3} \end{array} \right] = \left[ \begin{array}{r r r} - 1 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & - 3 \end{array} \right] \left[ \begin{array}{c} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right] + \left[ \begin{array}{c} 3 \\ - 6 \\ 3 \end{array} \right] u \tag {9-20}
$$

Equation (9–20) is also a state equation that describes the same system as defined by Equation (9–13).

The output equation, Equation (9–16), is modified to

$$y = \mathbf {C P z}$$

or
