# Step Response of an Underdamped Second-Order System

A step input is often used as a “test input” in order to establish performance or design specifications for a second-order system, such as its damping level and settling time. In this subsection we derive basic performance equations for an underdamped second-order system based on a constant (step) input.

To begin, consider the second-order LTI system that has been written in our “standard form” for an underdamped system

$$\ddot {y} + 2 \zeta \omega_ {n} \dot {y} + \omega_ {n} ^ {2} y = \omega_ {n} ^ {2} u (t) \tag {7.69}$$

We have assumed that the coefficient multiplying the input $u ( t )$ is equal to the coefficient for y. Therefore, if the input is a constant $u ( t ) = A$ , then the steady-state output is the same constant, $\mathrm { o r } y ( \infty ) = A$ (recall that at steady state $\ddot { y } = \dot { y } = 0$ for a stable system with a constant input). The complete system response will be the sum of the homogeneous and particular solutions, or $y ( t ) = y _ { H } ( t ) + y _ { P } ( t )$ . If the input is a unit-step function, then the particular solution $y _ { P } ( t )$ is also a constant with a value of one. Because we have assumed that the system is underdamped $( 0 < \zeta < 1 )$ , the homogeneous or transient response is a damped sinusoid represented by Eq. (7.57). The complete unit-step response is

$$y (t) = 1 + e ^ {\alpha t} \left[ c _ {3} \cos \beta t + c _ {4} \sin \beta t \right] \tag {7.70}$$

where $\alpha = - \zeta \omega _ { n }$ (real part of the complex roots) and $\beta = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ (imaginary part of the complex roots). For now, let us leave the step response Eq. (7.70) in terms of ?? and $\beta$ and substitute their respective values later.

We can obtain the constants $c _ { 3 }$ and $c _ { 4 }$ in Eq. (7.70) from the initial conditions, which we assume are zero: $y ( 0 ) = \dot { y } ( 0 ) = 0$ . Setting t = 0 in Eq. (7.70) yields

$$y (0) = 1 + c _ {3} = 0$$

and therefore constant $c _ { 3 } = - 1$ . The time derivative of Eq. (7.70) is

$$\dot {y} (t) = \alpha e ^ {\alpha t} c _ {3} \cos \beta t - e ^ {\alpha t} \beta c _ {3} \sin \beta t + \alpha e ^ {\alpha t} c _ {4} \sin \beta t + e ^ {\alpha t} \beta c _ {4} \cos \beta t \tag {7.71}$$

Setting t = 0 in Eq. (7.71) yields

$$\dot {y} (0) = \alpha c _ {3} + \beta c _ {4} = 0$$

Substituting $c _ { 3 } = - 1$ , we find that constant $c _ { 4 } = \alpha / \beta$ . Using Eq. (7.70), the complete unit-step response is
