# Example C.4

Consider a dynamic system governed by two coupled, nonlinear ODEs

$$0. 5 \dot {y} + 0. 6 \operatorname{sgn} (y) - 1. 4 z = 0 \tag {C.10}4 \ddot {z} + 0. 5 \dot {z} ^ {2} + 1 0 z = u (t) \tag {C.11}$$

The system’s initial conditions are $y ( 0 ) = 0 , z ( 0 ) = 1$ , and $\dot { z } ( 0 ) = 0$ , and the input is a pulse function: $u ( t ) = 2 0$ for $0 < t < 1$ s and $u ( t ) = 0$ for $t \geq 1 \mathrm { s }$ . Equations (C.10) and (C.11) are clearly nonlinear as we have a signum (sgn or sign) term and a squared term (of course, only one nonlinear term needs to be present in order to make the entire system nonlinear). The system is third order $( n = 3 )$ , as we have one first-order ODE and one second-order ODE. Because the system is nonlinear we cannot use transfer functions or an SSR. The solution will require three direct numerical integrations, or three integrator blocks. To show this, we can write each ODE with the highest time-derivative term on the left-hand side with a unity coefficient:

$$\dot {y} = \frac {1}{0 . 5} (- 0. 6 \mathrm{sgn} (y) + 1. 4 z) \tag {C.12}\ddot {z} = \frac {1}{4} \left(- 0. 5 \dot {z} ^ {2} - 1 0 z + u (t)\right) \tag {C.13}$$
