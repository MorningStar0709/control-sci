# Example 5.6

Obtain a complete SSR of the electromechanical DC motor system that was presented in Chapter 3. A tachometer is used to measure the angular velocity of the rotor (??̇ ), and an ammeter is used to measure current in the armature circuit (I).

The mathematical model of the DC motor was developed in Chapter 3, and the governing system model is repeated below

$$L \dot {I} + R I = e _ {\text { in }} (t) - K _ {b} \dot {\theta} \tag {5.30}J \ddot {\theta} + b \dot {\theta} = K _ {m} I - T _ {L} \tag {5.31}$$

Equation (5.30) is a first-order linear ODE, and Eq. (5.31) is a second-order linear ODE. Consequently, $n = 3$ and the system requires three state variables. We select current I, angular displacement ??, and angular velocity ??̇ as the three state variables. The applied armature voltage $e _ { \mathrm { i n } } ( t )$ and load torque $T _ { L }$ are the two inputs to the system. Therefore, we have states $x _ { 1 } = I , x _ { 2 } = \theta , x _ { 3 } = { \dot { \theta } }$ and inputs $u _ { 1 } = e _ { \mathrm { i n } } ( t ) , u _ { 2 } = T _ { L }$ .

Next, we write the three first-order state equations by taking a time derivative of each state variable, and substitute Eq. (5.30) for the time derivative of current I and Eq. (5.31) for the time derivative of angular velocity ??̇

$$\dot {x} _ {1} = \dot {I} = \frac {1}{L} (- R I + e _ {\text { in }} (t) - K _ {b} \dot {\theta}) \tag {5.32}\dot {x} _ {2} = \dot {\theta} \tag {5.33}\dot {x} _ {3} = \ddot {\theta} = \frac {1}{J} (- b \dot {\theta} + K _ {m} I - T _ {L}) \tag {5.34}$$

We substitute the states $x _ { 1 } = I , x _ { 2 } = \theta , x _ { 3 } = { \dot { \theta } }$ and the inputs $u _ { 1 } = e _ { \mathrm { i n } } ( t ) , u _ { 2 } = T _ { L }$ in the three first-order differential equations to yield

$$\dot {x} _ {1} = - \frac {R}{L} x _ {1} + \frac {1}{L} u _ {1} - \frac {K _ {b}}{L} x _ {3} \tag {5.35}\dot {x} _ {2} = x _ {3} \tag {5.36}\dot {x} _ {3} = - \frac {b}{J} x _ {3} + \frac {K _ {m}}{J} x _ {1} - \frac {1}{J} u _ {2} \tag {5.37}$$

Finally, we put Eqs. (5.35)– (5.37) in the standard matrix-vector format to construct the state equation. The rows of the A and B matrices will involve the coefficients associated with each state-variable equation. The state equation is

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - R / L & 0 & - K _ {b} / L \\ 0 & 0 & 1 \\ K _ {m} / J & 0 & - b / J \end{array} \right] \mathbf {x} + \left[ \begin{array}{c c} 1 / L & 0 \\ 0 & 0 \\ 0 & - 1 / J \end{array} \right] \mathbf {u} \tag {5.38}
$$
