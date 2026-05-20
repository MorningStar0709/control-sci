Finally, note that if the performance index is given in terms of the output vector rather than the state vector, that is,

$$J = \int_ {0} ^ {\infty} (\mathbf {y} ^ {*} \mathbf {Q y} + \mathbf {u} ^ {*} \mathbf {R u}) d t$$

then the index can be modified by using the output equation

$$\mathbf {y} = \mathbf {C x}$$

to

$$J = \int_ {0} ^ {\infty} (\mathbf {x} ^ {*} \mathbf {C} ^ {*} \mathbf {Q C x} + \mathbf {u} ^ {*} \mathbf {R u}) d t \tag {10-119}$$

and the design steps presented in this section can be applied to obtain the optimal matrix K.

$$u (t) = - \mathbf {K x} (t)$$

determine the optimal feedback gain matrix K such that the following performance index is minimized:

$$J = \int_ {0} ^ {\infty} \left(\mathbf {x} ^ {T} \mathbf {Q x} + u ^ {2}\right) d t$$

where

$$
\mathbf {Q} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & \mu \end{array} \right] \quad (\mu \geq 0)
$$

From Figure 10–36, we find that the state equation for the plant is

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

We shall demonstrate the use of the reduced-matrix Riccati equation in the design of the optimal control system. Let us solve Equation (10–118), rewritten as

$$\mathbf {A} ^ {*} \mathbf {P} + \mathbf {P A} - \mathbf {P B R} ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} + \mathbf {Q} = \mathbf {0}$$

Noting that matrix A is real and matrix Q is real symmetric, we see that matrix P is a real symmetric matrix. Hence, this last equation can be written as

$$
\begin{array}{l} \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] \\ - \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ 1 ] [ 0 \quad 1 ] \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 0 \\ 0 & \mu \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \\ \end{array}
$$

This equation can be simplified to
