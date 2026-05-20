The three-step linearization process is demonstrated by the following example. Suppose we have a nonlinear system with one state variable x, and one input variable u

$$\dot {x} = f (x, u) \tag {5.59}$$

Step 1: The nominal input $u ^ { * }$ (which is likely given in the problem) results in the nominal state solution $x ^ { * }$ , which is the nominal operating point.

Step 2: The perturbation variables are $\delta x = x - x ^ { * }$ and $\delta u = u - u ^ { * }$ . Therefore, we can substitute $x = \delta x + x ^ { * }$ and $\boldsymbol { u } = \delta \boldsymbol { u } + \boldsymbol { u } ^ { * }$ into the nonlinear model (5.59)

$$\delta \dot {x} + \dot {x} ^ {*} = f (\delta x + x ^ {*}, \delta u + u ^ {*}) \tag {5.60}$$

Step 3: Expand the right-hand side of the nonlinear equation (5.60) in Taylor series about $x ^ { * }$ and $u ^ { * }$

$$\delta \dot {x} + \dot {x} ^ {*} = f (x ^ {*}, u ^ {*}) + \left. \frac {\partial f}{\partial x} \right| _ {*} \delta x + \left. \frac {1}{2 !} \frac {\partial^ {2} f}{\partial x ^ {2}} \right| _ {*} \delta x ^ {2} + \dots + \left. \frac {\partial f}{\partial u} \right| _ {*} \delta u + \frac {1}{2 !} \left. \frac {\partial^ {2} f}{\partial u ^ {2}} \right| _ {*} \delta u ^ {2} + \dots \tag {5.61}$$

Because the nominal state solution is $\dot { x } ^ { * } = f ( x ^ { * } , u ^ { * } )$ , these two terms cancel each other in Eq. (5.61). It should be noted that all partial derivatives in Eq. (5.61) are evaluated at the nominal state and input, $x ^ { * }$ and $u ^ { * }$ , respectively. Finally, eliminating all Taylor-series terms higher than first-order yields

$$\delta \dot {x} = \left. \frac {\partial f}{\partial x} \right| _ {*} \delta x + \left. \frac {\partial f}{\partial u} \right| _ {*} \delta u \tag {5.62}$$

Equation (5.62) is the linearized model of the original nonlinear system (5.59). The two first-order derivatives $\partial f / \partial x$ and ??f ∕??u are constants as long as $x ^ { * }$ and $u ^ { * }$ are constants. It is important to note that the linear model (5.62) is in terms of the perturbation variables ??x and $\delta u .$ . Therefore, the solution of the linearized model (5.62) yields ??x(t), which is the time history of the state deviation from the operating point $x ^ { * }$ . If we want to estimate the state history from the linear solution, we use $x ( t ) = \delta x ( t ) + x ^ { * }$ .
