# 5.3 STATE-SPACE REPRESENTATION

If the mathematical modeling equations representing a system are linear, then the resulting state-variable equations (5.1) will be linear first-order ODEs. In this case, we can write the state-variable equations in a convenient matrix-vector format called the state-space representation (SSR). The SSR is well-suited for implementation in a numerical computer simulation using MATLAB or Simulink as discussed in Chapter 6.

A few definitions are in order before the SSR is presented. Recall that an nth-order system will require n state variables $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ . We define the state vector x as the $n \times 1$ column vector composed of the state variables $x _ { i }$

$$
\mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right]
$$

It should be noted that the state vector does not represent a physical vector (such as a three-component force vector in mechanics), but rather a convenient collection of all n state variables. The state space is defined as the n-dimensional “geometric space” that contains the state vector x.

A complete SSR includes two equations in a matrix-vector format: the state equation and the output equation. The output variables are denoted by $y _ { 1 } , y _ { 2 } , \ldots , y _ { m }$ , and they are functions of the state and input variables:

$$y _ {1} = h _ {1} (x _ {1}, x _ {2}, \ldots , x _ {n}, u _ {1}, u _ {2}, \ldots , u _ {r})y _ {2} = h _ {2} (x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r})y _ {m} = h _ {m} \left(x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r}\right) \tag {5.20}$$

The output equations (5.20) may be linear or nonlinear; however, the output equations must be linear in order to use the matrix-vector SSR. Output variables usually represent sensor measurements of a system’s response. For example, if a 1-DOF rotational mechanical system has state variables x = angular position and x2 = angular velocity and a tachometer is measuring angular velocity, the single output equation is $y = x _ { 2 }$ .

For example, if our system is linear time invariant (LTI) and third order $( n = 3 )$ ) with two inputs $( r = 2 )$ , then our state-variable equations will have the general form:
