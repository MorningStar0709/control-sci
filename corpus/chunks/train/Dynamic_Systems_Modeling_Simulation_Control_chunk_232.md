# Example 5.9

Derive the linear model of the following nonlinear state-variable equation. Perform the linearization about the static equilibrium state $x ^ { * }$ that results from the nominal input $u ^ { * } = 2$ .

$$\dot {x} = - 2 x - 0. 4 x ^ {3} + 0. 3 u = f (x, u) \tag {5.63}$$

The first step is to obtain the nominal state $x ^ { * }$ given the nominal input $u ^ { * } = 2$ . We assume that a static equilibrium state exists when the nominal input is $u ^ { * } = 2 ;$ ; that is, ẋ = 0 and hence x remains constant. Solving Eq. (5.63) for x with ${ \dot { x } } = 0$ and $u = u ^ { * } = 2$ yields a third-order polynomial in x

$$\dot {x} = - 2 x - 0. 4 x ^ {3} + 0. 6 = 0 \tag {5.64}$$

We can use MATLAB’s roots command to obtain the three roots

$$> > \text { roots } ([ - 0. 4 0 - 2 0. 6 ])$$

where the row vector in the square brackets contains the coefficients of the third-order polynomial in Eq. (5.64) in descending powers of x. The three roots include one real root $( x = 0 . 2 9 4 9 )$ , and two complex conjugate roots $( x = - 0 . 1 4 7 4 \pm j 2 . 2 5 0 6 ;$ ; recall that j is the imaginary number, $j = \sqrt { - 1 } )$ ). Because the equilibrium state must be a real number, the nominal state is $x ^ { * } = 0 . 2 9 4 9$ .

Next, we define the perturbation variables $\delta x = x - x ^ { * }$ and $\delta u = u - u ^ { * }$ and write the linearized equation (5.62) that results from the first-order Taylor-series expansion

$$\delta \dot {x} = \left. \frac {\partial f}{\partial x} \right| _ {*} \delta x + \left. \frac {\partial f}{\partial u} \right| _ {*} \delta u \tag {5.65}$$

The two partial derivatives are easily evaluated using the right-hand-side function $f ( x , u )$ defined in Eq. (5.63). We evaluate the partial derivatives at the nominal state $x ^ { * }$ and nominal input $u ^ { * }$

$$\left. \frac {\partial f}{\partial x} \right| _ {*} = - 2 - 1. 2 x ^ {2} | _ {*} = - 2 - 1. 2 (0. 2 9 4 9 ^ {2}) = - 2. 1 0 4 4\left. \frac {\partial f}{\partial u} \right| _ {*} = 0. 3$$

Note that the value of the nominal input $u ^ { * }$ was not needed for evaluating either of the two partial derivatives. In addition, the partial derivative ??f ∕??u is 0.3, which is the same input coefficient in the nonlinear equation (5.63) because the term involving u is already linear. Finally, substituting the numerical values of the two partial derivatives into the first-order Taylor-series equation (5.65) yields

$$\delta \dot {x} = - 2. 1 0 4 4 \delta x + 0. 3 \delta u \tag {5.66}$$
