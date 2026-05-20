# Example C.3

Consider a dynamic system governed by two coupled, linear ODEs

$$0. 5 \dot {y} + 3 y - 0. 4 z = 0 \tag {C.6}2. 4 \dot {z} + 1 6 z = u (t) \tag {C.7}$$

The system’s initial conditions are $y ( 0 ) = - 0 . 3$ and $z ( 0 ) = 0 . 6 ,$ , and the input is a step function $u ( t ) = 3 . 5 U ( t - 1 )$ . Therefore, the input $u ( t )$ is zero for time $t \leq 1$ s and has a constant magnitude of 3.5 for time t > 1 s. Because the system is linear, we can use an SSR; however, we demonstrate the integrator-block method here. Clearly, the system defined by Eqs. (C.6) and (C.7) is linear and second order because we have two first-order ODEs. Hence, we need two numerical integrations to solve the system, or two integrator blocks: one integrator for Eq. (C.6) and one integrator for Eq. (C.7). Let us begin by rewriting both ODEs with the respective derivative terms on the left-hand side with unity coefficients:

$$\dot {y} = \frac {1}{0 . 5} (- 3 y + 0. 4 z) \tag {C.8}\dot {z} = \frac {1}{2 . 4} (- 1 6 z + u (t)) \tag {C.9}$$

The core of the Simulink model consists of two integrator blocks, where the right-hand sides of Eqs. (C.8) and (C.9) are the respective inputs. Figure C.7 shows a schematic diagram presenting the numerical solutions of Eqs. (C.8) and (C.9). The inputs to the respective integrators are ẏ and ż , which are represented by Eqs. (C.8) and (C.9). The outputs of each integrator are y(t) and z(t), respectively. Note that the initial conditions y(0) and z(0) (i.e., the integration constants) are applied to the appropriate integrators. The key is to develop a block diagram such that the signal paths are summed in a manner to synthesize the appropriate input to each integrator. For example, the input to the ẏ integrator must be a linear sum of y(t) and z(t). Consequently, these two output signals are fed back to a summing junction to create ẏ . The input to the ż integrator is a linear sum of z(t) and system input u(t).
