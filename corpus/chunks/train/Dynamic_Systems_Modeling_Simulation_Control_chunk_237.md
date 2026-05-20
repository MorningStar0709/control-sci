# Example 5.11

Consider again the nonlinear system from Example 5.1 and the corresponding state-variables equations. Derive the linear state equation for a nominal constant input $u ^ { * } = 0 . 1 5$ .

$$\dot {x} _ {1} = f _ {1} (\mathbf {x}, u) = x _ {2} \tag {5.77}\dot {x} _ {2} = f _ {2} (\mathbf {x}, u) = - 0. 4 x _ {1} + 0. 2 x _ {3} - 0. 1 x _ {2} x _ {3} \tag {5.78}\dot {x} _ {3} = f _ {3} (\mathbf {x}, u) = - 0. 7 5 x _ {3} - 0. 0 2 5 x _ {3} ^ {3} + 1. 5 x _ {1} + 2 u \tag {5.79}$$

The linearization is performed about the nominal state vector. We must determine the equilibrium state vector $\mathbf { x } ^ { * }$ given constant input $u ^ { * }$ . The first state-variable equation (5.77) shows that setting $\dot { x } _ { 1 } = 0$ for equilibrium requires that state $x _ { 2 } = 0$ . Using $x _ { 2 } = 0$ in Eq. (5.78) with $\dot { x } _ { 2 } = 0$ results in the equilibrium condition $- 0 . 4 x _ { 1 } + 0 . 2 x _ { 3 } = 0 , \mathrm { o r } x _ { 1 } = 0 . 5 x _ { 3 }$ . The final state-variable equation (5.79) with condition $x _ { 1 } = 0 . 5 x _ { 3 }$ and nominal input $u = u ^ { * } = 0 . 1 5$ yields the third-order polynomial in $x _ { 3 }$

$$\dot {x} _ {3} = - 0. 7 5 x _ {3} - 0. 0 2 5 x _ {3} ^ {3} + 1. 5 (0. 5 x _ {3}) + 2 (0. 1 5) = 0 \tag {5.80}$$

or

$$- 0. 0 2 5 x _ {3} ^ {3} + 0. 3 = 0 \tag {5.81}$$

We can use MATLAB’s roots command to obtain the three roots

$$> > \text { roots } ([ - 0. 0 2 5 0 0 0. 3 ])$$

The three roots include one real root $( x _ { 3 } = 2 . 2 8 9 4 )$ and two complex conjugate roots $( x _ { 3 } = - 1 . 1 4 4 7 \pm j 1 . 9 8 2 7 )$ . Because the equilibrium state must be a real number, the nominal value of the third state is $x _ { 3 } ^ { * } = 2 . 2 8 9 4$ . Hence the nominal value of the first state is $x _ { 1 } ^ { * } = 1 . 1 4 4 7$ and the nominal state vector is

$$
\mathbf {x} ^ {*} = \left[ \begin{array}{c} x _ {1} ^ {*} \\ x _ {2} ^ {*} \\ x _ {3} ^ {*} \end{array} \right] = \left[ \begin{array}{c} 1. 1 4 4 7 \\ 0 \\ 2. 2 8 9 4 \end{array} \right] \tag {5.82}
$$

Equations (5.75) and (5.76) show that the system matrix A is composed of the first-order partial derivatives of the three right-hand side functions $f _ { i } ( { \bf x } , u )$ in Eqs. (5.77) – (5.79). The first-order partial derivatives are
