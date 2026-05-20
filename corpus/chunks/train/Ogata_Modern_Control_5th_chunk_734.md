Notice that the eigenvalues of $\mathbf { A } _ { 2 2 }$ do not depend on K. Thus, if the system is not completely state controllable, then there are eigenvalues of matrix A that cannot be arbitrarily placed.Therefore, to place the eigenvalues of matrix A-BK arbitrarily, the system must be completely state controllable (necessary condition).

Next we shall prove a sufficient condition: that is, if the system is completely state controllable, then all eigenvalues of matrix A can be arbitrarily placed.

In proving a sufficient condition, it is convenient to transform the state equation given by Equation (10–1) into the controllable canonical form.

Define a transformation matrix T by

$$\mathbf {T} = \mathbf {M W} \tag {10-4}$$

where M is the controllability matrix

$$
\mathbf {M} = \left[ \begin{array}{c c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] \tag {10-5}
$$

and

$$
\mathbf {W} = \left[ \begin{array}{c c c c c} a _ {n - 1} & a _ {n - 2} & \dots & a _ {1} & 1 \\ a _ {n - 2} & a _ {n - 3} & \dots & 1 & 0 \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ a _ {1} & 1 & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0 \end{array} \right] \tag {10-6}
$$

where the $\boldsymbol { a } _ { i } ^ { \prime } \mathbf { s }$ are coefficients of the characteristic polynomial

$$| s \mathbf {I} - \mathbf {A} | = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

Define a new state vector $\hat { \mathbf { x } }$ by

$$\mathbf {x} = \mathbf {T} \hat {\mathbf {x}}$$

If the rank of the controllability matrix M is n (meaning that the system is completely state controllable), then the inverse of matrix T exists, and Equation (10–1) can be modified to

$$\dot {\hat {\mathbf {x}}} = \mathbf {T} ^ {- 1} \mathbf {A} \mathbf {T} \hat {x} + \mathbf {T} ^ {- 1} \mathbf {B} u \tag {10-7}$$

where

$$
\mathbf {T} ^ {- 1} \mathbf {A T} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \tag {10-8}

\mathbf {T} ^ {- 1} \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ \cdot \\ \cdot \\ \cdot \\ 0 \\ 1 \end{array} \right] \tag {10-9}
$$
