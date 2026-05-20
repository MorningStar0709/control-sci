# Example 5.5

Consider again the simple single-mass mechanical system shown in Fig. 5.1 that was described in Example 5.2. Obtain a complete SSR if the stiffness is modeled by an ideal (linear) spring element. A single sensor measures the translational displacement of the mass.

We are able to develop the SSR only if the state and output equations are linear. Therefore, let us assume a linear spring force and hence $k _ { 1 } = k$ (linear spring constant) and $k _ { 3 } = 0$ . Recall that the state variables are $x _ { 1 } = z$ (position) and $x _ { 2 } = \dot { z } \mathrm { ~ ( v e l o c i t y ) ~ }$ , and the input variable is $u = F _ { a } ( t )$ (applied force). The state vector is a column vector with two elements

$$
\mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

The linear state-variable equations are

$$\dot {x} _ {1} = x _ {2} \tag {5.26}\dot {x} _ {2} = - \frac {k}{m} x _ {1} - \frac {b}{m} x _ {2} + \frac {1}{m} u \tag {5.27}$$

First, let us construct the matrix-vector state equation. The first rows of the A and B matrices will involve the coefficients associated with the first state-variable equation (5.26). Because the first state-variable equation is ${ \dot { x } } _ { 1 } = x _ { 2 } .$ , the first row of the state matrix A consists of a zero coefficient for the first column (which multiplies $x _ { 1 } )$ and a unity coefficient for the second column (which multiplies $x _ { 2 } )$ . The first row of the input matrix B consists of a zero coefficient as the first state-variable equation does not include the input u. The second rows of the A and B matrices will involve the coefficients from the second state-variable equation (5.27). The state equation then takes the form

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - k / m & - b / m \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 / m \end{array} \right] u \tag {5.28}
$$

The reader should be able to perform the matrix-vector multiplication in Eq. (5.28) and arrive at the two statevariables equations (5.26) and (5.27).

In general, the output equation depends on which variable or variables are either measured or defined to be the system output. In this case, a single sensor measures the translational position of the mass. Hence, the output is $y = z = x _ { 1 }$ . The output equation is also a matrix-vector equation, which for this problem takes the form
